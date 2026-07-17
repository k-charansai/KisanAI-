import os
from pathlib import Path

# Base Paths
BASE_DIR = Path(__file__).resolve().parent.parent.parent
ML_DIR = BASE_DIR / "ml"
DATA_DIR = ML_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PLANTVILLAGE_DIR = RAW_DATA_DIR / "PlantVillage" # Adjust if dataset extracts differently
PLANTDOC_DIR = RAW_DATA_DIR / "PlantDoc"
CHECKPOINT_DIR = ML_DIR / "checkpoints"
ONNX_MODEL_PATH = CHECKPOINT_DIR / "best_model.onnx"
DOCS_DIR = BASE_DIR / "docs"

# Output Files
TRAINING_SUMMARY_FILE = ML_DIR / "training_summary.json"
MODEL_METRICS_FILE = DOCS_DIR / "model_metrics.md"
CLASS_LABELS_FILE = ML_DIR / "class_labels.json" # Needed for backend
CONFUSION_MATRIX_FILE = ML_DIR / "confusion_matrix.png"

# Kaggle Dataset
KAGGLE_DATASET = "abdallahalidev/plantvillage-dataset"
NUM_CLASSES = 38

# Model & Training
IMAGE_SIZE = 224 # EfficientNet-B0 default
BATCH_SIZE = 32

# Transfer Learning Phase 1 (Head only)
PHASE1_LR = 1e-3
PHASE1_EPOCHS = 5

# Transfer Learning Phase 2 (Unfreeze last 2 blocks)
PHASE2_LR = 1e-4
PHASE2_EPOCHS = 8

# EDA
NEAR_DUPLICATE_THRESHOLD = 5 # Hamming distance for phash

# Ensure directories exist (just in case they were not created yet)
os.makedirs(CHECKPOINT_DIR, exist_ok=True)
os.makedirs(DOCS_DIR, exist_ok=True)
