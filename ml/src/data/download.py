import os
import sys
import subprocess
import zipfile
import shutil
from pathlib import Path

# Add src to python path so we can import config
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
from src import config

def download_dataset():
    """
    Downloads the PlantVillage dataset from Kaggle, extracts it,
    and performs a sanity check on the class count.
    """
    print(f"Checking for dataset in {config.RAW_DATA_DIR}...")
    
    if not config.RAW_DATA_DIR.exists():
        config.RAW_DATA_DIR.mkdir(parents=True)
        
    zip_path = config.RAW_DATA_DIR / "plantvillage-dataset.zip"
    
    # 1. Download if not exists
    if not zip_path.exists():
        print(f"Downloading {config.KAGGLE_DATASET} via Kaggle CLI...")
        try:
            subprocess.run([
                "kaggle", "datasets", "download", 
                "-d", config.KAGGLE_DATASET,
                "-p", str(config.RAW_DATA_DIR)
            ], check=True)
        except subprocess.CalledProcessError as e:
            print("Failed to download dataset. Do you have Kaggle CLI installed and configured (~/.kaggle/kaggle.json)?", file=sys.stderr)
            sys.exit(1)
        except FileNotFoundError:
            print("Kaggle CLI not found. Please 'pip install kaggle' and configure credentials.", file=sys.stderr)
            sys.exit(1)
            
    # 2. Extract
    print("Extracting dataset...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(config.RAW_DATA_DIR)
        
    # The abdallahalidev/plantvillage-dataset typically has folders like 'plantvillage dataset/color'
    # We need to find the directory containing the 38 class folders.
    print("Searching for the color images directory...")
    target_dir = None
    
    # Try common paths
    possible_paths = [
        config.RAW_DATA_DIR / "plantvillage dataset" / "color",
        config.RAW_DATA_DIR / "color",
        config.RAW_DATA_DIR / "PlantVillage",
    ]
    
    for p in possible_paths:
        if p.exists() and p.is_dir():
            target_dir = p
            break
            
    if not target_dir:
        # Fallback search
        for root, dirs, files in os.walk(config.RAW_DATA_DIR):
            if "color" in dirs:
                target_dir = Path(root) / "color"
                break
                
    if not target_dir or not target_dir.exists():
        print("Error: Could not find the expected directory structure (looking for a 'color' folder with 38 classes).", file=sys.stderr)
        sys.exit(1)

    # Move to the expected location if it's not already there
    if target_dir != config.PLANTVILLAGE_DIR:
        print(f"Moving dataset from {target_dir} to {config.PLANTVILLAGE_DIR}...")
        if config.PLANTVILLAGE_DIR.exists():
            shutil.rmtree(config.PLANTVILLAGE_DIR)
        shutil.move(str(target_dir), str(config.PLANTVILLAGE_DIR))
    
    # 3. Sanity check: 38 classes
    class_folders = [d for d in os.listdir(config.PLANTVILLAGE_DIR) if os.path.isdir(config.PLANTVILLAGE_DIR / d)]
    class_count = len(class_folders)
    
    if class_count != config.NUM_CLASSES:
        print(f"SANITY CHECK FAILED: Expected {config.NUM_CLASSES} classes, found {class_count} in {config.PLANTVILLAGE_DIR}.", file=sys.stderr)
        sys.exit(1)
        
    print(f"Success! Dataset downloaded and verified. Found {class_count} classes.")

if __name__ == "__main__":
    download_dataset()
