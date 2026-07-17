import torch
import json
import os
import sys
from pathlib import Path
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
from sklearn.metrics import accuracy_score, classification_report
import numpy as np

# Add src to python path so we can import modules
sys.path.append(str(Path(__file__).resolve().parent.parent))
from src import config
from src.models.efficientnet import get_model

def evaluate_field():
    print("--- Phase 2: Field Validation on PlantDoc ---")
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")
    
    if not config.PLANTDOC_DIR.exists():
        print(f"Error: PlantDoc directory {config.PLANTDOC_DIR} not found. Run download_plantdoc.py first.")
        sys.exit(1)
        
    if not config.CHECKPOINT_DIR.joinpath("best_model.pt").exists():
        print("Error: best_model.pt not found. Please train the model in Phase 1 first.")
        sys.exit(1)
        
    if not config.CLASS_LABELS_FILE.exists():
        print("Error: class_labels.json not found.")
        sys.exit(1)
        
    # Load PlantVillage labels
    with open(config.CLASS_LABELS_FILE, "r") as f:
        pv_idx_to_name = json.load(f)
    pv_name_to_idx = {name: int(idx) for idx, name in pv_idx_to_name.items()}
    
    # Setup model
    model = get_model(num_classes=config.NUM_CLASSES)
    model.load_state_dict(torch.load(config.CHECKPOINT_DIR / "best_model.pt", map_location=device, weights_only=True))
    model = model.to(device)
    model.eval()
    
    # Setup data
    val_transforms = transforms.Compose([
        transforms.Resize((config.IMAGE_SIZE, config.IMAGE_SIZE)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    
    dataset = datasets.ImageFolder(root=config.PLANTDOC_DIR, transform=val_transforms)
    dataloader = DataLoader(dataset, batch_size=config.BATCH_SIZE, shuffle=False, num_workers=2)
    
    # Create mapping from PlantDoc classes to PlantVillage classes
    pd_class_to_idx = dataset.class_to_idx
    pd_idx_to_pv_idx = {}
    
    print("\nMapping PlantDoc classes to PlantVillage classes...")
    mapped_count = 0
    for pd_name, pd_idx in pd_class_to_idx.items():
        pd_norm = pd_name.lower().replace(" ", "_").replace("-", "_")
        
        match_found = False
        for pv_name, pv_idx in pv_name_to_idx.items():
            pv_norm = pv_name.lower().replace(" ", "_").replace("-", "_")
            if pd_norm == pv_norm or pd_norm in pv_norm or pv_norm in pd_norm:
                pd_idx_to_pv_idx[pd_idx] = pv_idx
                match_found = True
                mapped_count += 1
                break
                
        if not match_found:
            print(f"  Warning: No match found for '{pd_name}'. Images in this class will be ignored.")
            pd_idx_to_pv_idx[pd_idx] = -1
            
    print(f"Successfully mapped {mapped_count}/{len(pd_class_to_idx)} PlantDoc classes.")
    
    # Evaluate
    all_preds = []
    all_labels = []
    
    print("\nEvaluating on PlantDoc...")
    with torch.no_grad():
        for inputs, labels in dataloader:
            inputs = inputs.to(device)
            
            # Map labels
            mapped_labels = torch.tensor([pd_idx_to_pv_idx[l.item()] for l in labels])
            
            # Filter out ignored classes
            valid_mask = mapped_labels != -1
            if valid_mask.sum() == 0:
                continue
                
            inputs = inputs[valid_mask]
            mapped_labels = mapped_labels[valid_mask]
            
            outputs = model(inputs)
            _, preds = torch.max(outputs, 1)
            
            all_preds.extend(preds.cpu().numpy())
            all_labels.extend(mapped_labels.numpy())
            
    accuracy = accuracy_score(all_labels, all_preds)
    print(f"\n--- Field Validation Results ---")
    print(f"Accuracy on PlantDoc: {accuracy * 100:.2f}%")
    
    print("\nNote: A drop to 60-75% accuracy is expected and normal for this domain shift (lab -> field).")
    
    # Append to model_metrics.md
    with open(config.MODEL_METRICS_FILE, "a") as f:
        f.write(f"\n## Phase 2: Field Validation (PlantDoc)\n")
        f.write(f"- **Accuracy:** {accuracy * 100:.2f}%\n")
        f.write("- **Observation:** Expected accuracy drop due to domain shift from lab conditions (PlantVillage) to field conditions (PlantDoc).\n")
        
    print(f"Saved field validation results to {config.MODEL_METRICS_FILE}")

if __name__ == "__main__":
    evaluate_field()
