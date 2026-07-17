import torch
import json
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix
import sys

# Adjust path to import from src
sys.path.append(str(Path(__file__).resolve().parent.parent))
from src import config
from src.data.dataset import load_data
from src.models.efficientnet import get_model

def evaluate_model():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")
    
    # Load dataset
    print("Loading validation dataset...")
    _, val_loader, class_names, _ = load_data(val_split=0.2)
    
    # Load model
    print("Loading best model checkpoint...")
    model_path = config.CHECKPOINT_DIR / "best_model.pt"
    if not model_path.exists():
        print("Model checkpoint not found. Run training first.", file=sys.stderr)
        sys.exit(1)
        
    model = get_model(config.NUM_CLASSES)
    model.load_state_dict(torch.load(model_path, map_location=device))
    model.to(device)
    model.eval()
    
    all_preds = []
    all_labels = []
    
    print("Running inference...")
    with torch.no_grad():
        for inputs, labels in val_loader:
            inputs, labels = inputs.to(device), labels.to(device)
            outputs = model(inputs)
            _, preds = outputs.max(1)
            all_preds.extend(preds.cpu().numpy())
            all_labels.extend(labels.cpu().numpy())
            
    # Calculate metrics
    print("Calculating metrics...")
    report_dict = classification_report(all_labels, all_preds, target_names=class_names, output_dict=True)
    report_str = classification_report(all_labels, all_preds, target_names=class_names)
    
    cm = confusion_matrix(all_labels, all_preds)
    
    # Find most confused pairs
    np.fill_diagonal(cm, 0) # Ignore correct predictions
    confused_pairs = []
    for i in range(len(class_names)):
        for j in range(len(class_names)):
            if cm[i, j] > 0:
                confused_pairs.append({
                    'true_label': class_names[i],
                    'predicted_label': class_names[j],
                    'count': cm[i, j]
                })
                
    confused_pairs = sorted(confused_pairs, key=lambda x: x['count'], reverse=True)
    
    # Save Confusion Matrix Plot
    plt.figure(figsize=(20, 20))
    sns.heatmap(cm, annot=False, cmap='Blues', xticklabels=class_names, yticklabels=class_names)
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')
    plt.title('Confusion Matrix (Errors Only)')
    plt.tight_layout()
    plt.savefig(config.CONFUSION_MATRIX_FILE)
    print(f"Saved confusion matrix plot to {config.CONFUSION_MATRIX_FILE}")
    
    # Write to docs/model_metrics.md
    with open(config.MODEL_METRICS_FILE, 'a') as f:
        f.write("\n## Phase 1 Evaluation (PlantVillage)\n\n")
        f.write(f"**Overall Accuracy:** {report_dict['accuracy']:.4f}\n\n")
        
        f.write("### Per-Class Metrics\n")
        f.write("```text\n")
        f.write(report_str)
        f.write("\n```\n\n")
        
        f.write("### Most Confused Pairs\n")
        f.write("| True Label | Predicted Label | Count |\n")
        f.write("| --- | --- | --- |\n")
        for pair in confused_pairs[:10]: # Top 10 most confused
            f.write(f"| {pair['true_label']} | {pair['predicted_label']} | {pair['count']} |\n")
            
    print(f"Appended evaluation metrics to {config.MODEL_METRICS_FILE}")

if __name__ == "__main__":
    evaluate_model()
