import os
import json
import random
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from pathlib import Path
import sys
from datetime import datetime

# Adjust path to import from src
sys.path.append(str(Path(__file__).resolve().parent.parent))
from src import config
from src.data.dataset import load_data
from src.models.efficientnet import get_model, freeze_backbone, unfreeze_last_n_blocks

def set_seed(seed=42):
    """Sets seed for reproducibility."""
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)
    print(f"Random seed set to: {seed}")
    return seed

def compute_class_weights(train_labels, num_classes):
    """Computes inverse-frequency class weights."""
    class_counts = np.bincount(train_labels, minlength=num_classes)
    total_samples = len(train_labels)
    # Avoid division by zero
    weights = total_samples / (num_classes * (class_counts + 1e-6))
    return torch.FloatTensor(weights)

def train_epoch(model, loader, criterion, optimizer, device):
    model.train()
    running_loss = 0.0
    correct = 0
    total = 0
    
    for inputs, labels in loader:
        inputs, labels = inputs.to(device), labels.to(device)
        
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        
        loss.backward()
        optimizer.step()
        
        running_loss += loss.item() * inputs.size(0)
        _, predicted = outputs.max(1)
        total += labels.size(0)
        correct += predicted.eq(labels).sum().item()
        
    epoch_loss = running_loss / total
    epoch_acc = correct / total
    return epoch_loss, epoch_acc

def validate_epoch(model, loader, criterion, device):
    model.eval()
    running_loss = 0.0
    correct = 0
    total = 0
    
    with torch.no_grad():
        for inputs, labels in loader:
            inputs, labels = inputs.to(device), labels.to(device)
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            
            running_loss += loss.item() * inputs.size(0)
            _, predicted = outputs.max(1)
            total += labels.size(0)
            correct += predicted.eq(labels).sum().item()
            
    epoch_loss = running_loss / total
    epoch_acc = correct / total
    return epoch_loss, epoch_acc

import argparse

def main():
    parser = argparse.ArgumentParser(description="Train KisanAI Vision Model")
    parser.add_argument("--epochs_stage1", type=int, default=config.PHASE1_EPOCHS)
    parser.add_argument("--epochs_stage2", type=int, default=config.PHASE2_EPOCHS)
    args = parser.parse_args()

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")
    
    # 1. Setup & Reproducibility
    seed = set_seed(42)
    
    # 2. Data Loading
    print("Loading datasets...")
    train_loader, val_loader, class_names, train_labels = load_data(val_split=0.2, random_seed=seed)
    
    # Save class labels for backend
    class_labels_dict = {i: name for i, name in enumerate(class_names)}
    with open(config.CLASS_LABELS_FILE, 'w') as f:
        json.dump(class_labels_dict, f, indent=4)
    print(f"Saved class labels to {config.CLASS_LABELS_FILE}")
    
    # 3. Model & Loss (with class weights)
    print("Initializing model...")
    model = get_model(config.NUM_CLASSES).to(device)
    
    weights = compute_class_weights(train_labels, config.NUM_CLASSES).to(device)
    criterion = nn.CrossEntropyLoss(weight=weights)
    
    training_history = {'phase1': [], 'phase2': []}
    best_val_acc = 0.0
    
    # ---- PHASE 1: Train Head Only ----
    print(f"\n--- Phase 1: Training Head Only (Frozen Backbone) ---")
    print(f"Hyperparameters: LR={config.PHASE1_LR}, Epochs={args.epochs_stage1}, Batch Size={config.BATCH_SIZE}")
    freeze_backbone(model)
    optimizer1 = optim.Adam(model.classifier.parameters(), lr=config.PHASE1_LR)
    
    for epoch in range(args.epochs_stage1):
        train_loss, train_acc = train_epoch(model, train_loader, criterion, optimizer1, device)
        val_loss, val_acc = validate_epoch(model, val_loader, criterion, device)
        
        print(f"Epoch {epoch+1}/{config.PHASE1_EPOCHS} - "
              f"Train Loss: {train_loss:.4f}, Train Acc: {train_acc:.4f} - "
              f"Val Loss: {val_loss:.4f}, Val Acc: {val_acc:.4f}")
              
        training_history['phase1'].append({
            'epoch': epoch + 1, 'train_loss': train_loss, 'train_acc': train_acc,
            'val_loss': val_loss, 'val_acc': val_acc
        })
        
        if val_acc > best_val_acc:
            best_val_acc = val_acc
            torch.save(model.state_dict(), config.CHECKPOINT_DIR / "best_model.pt")

    # ---- PHASE 2: Fine-tune Last 2 Blocks ----
    print(f"\n--- Phase 2: Fine-tuning Last 2 Blocks ---")
    print(f"Hyperparameters: LR={config.PHASE2_LR}, Epochs={args.epochs_stage2}, Batch Size={config.BATCH_SIZE}")
    unfreeze_last_n_blocks(model, n=2)
    
    # Need to collect parameters that require gradients
    trainable_params = [p for p in model.parameters() if p.requires_grad]
    optimizer2 = optim.Adam(trainable_params, lr=config.PHASE2_LR)
    
    for epoch in range(args.epochs_stage2):
        train_loss, train_acc = train_epoch(model, train_loader, criterion, optimizer2, device)
        val_loss, val_acc = validate_epoch(model, val_loader, criterion, device)
        
        print(f"Epoch {epoch+1}/{config.PHASE2_EPOCHS} - "
              f"Train Loss: {train_loss:.4f}, Train Acc: {train_acc:.4f} - "
              f"Val Loss: {val_loss:.4f}, Val Acc: {val_acc:.4f}")
              
        training_history['phase2'].append({
            'epoch': epoch + 1, 'train_loss': train_loss, 'train_acc': train_acc,
            'val_loss': val_loss, 'val_acc': val_acc
        })
        
        if val_acc > best_val_acc:
            best_val_acc = val_acc
            torch.save(model.state_dict(), config.CHECKPOINT_DIR / "best_model.pt")
            
    print("\nTraining Complete.")
    print(f"Best Validation Accuracy: {best_val_acc:.4f}")
    
    # 4. Save Training Summary
    summary = {
        "timestamp": datetime.now().isoformat(),
        "seed": seed,
        "hyperparameters": {
            "batch_size": config.BATCH_SIZE,
            "phase1": {"lr": config.PHASE1_LR, "epochs": config.PHASE1_EPOCHS},
            "phase2": {"lr": config.PHASE2_LR, "epochs": config.PHASE2_EPOCHS}
        },
        "best_val_acc": best_val_acc,
        "history": training_history
    }
    
    with open(config.TRAINING_SUMMARY_FILE, 'w') as f:
        json.dump(summary, f, indent=4)
    print(f"Training summary saved to {config.TRAINING_SUMMARY_FILE}")

if __name__ == "__main__":
    main()
