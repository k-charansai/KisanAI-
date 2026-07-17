import os
import sys
import subprocess
import zipfile
import shutil
from pathlib import Path

# Add src to python path so we can import config
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
from src import config

def download_plantdoc():
    """
    Downloads the PlantDoc classification dataset from Kaggle,
    extracts it, and prepares it for field validation.
    """
    print(f"Checking for PlantDoc dataset in {config.RAW_DATA_DIR}...")
    
    if not config.RAW_DATA_DIR.exists():
        config.RAW_DATA_DIR.mkdir(parents=True)
        
    dataset_slug = "nirmalsankalana/plantdoc-dataset"
    zip_path = config.RAW_DATA_DIR / "plantdoc-dataset.zip"
    
    # 1. Download if not exists
    if not zip_path.exists():
        print(f"Downloading {dataset_slug} via Kaggle CLI...")
        try:
            subprocess.run([
                "kaggle", "datasets", "download", 
                "-d", dataset_slug,
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
    extract_dir = config.RAW_DATA_DIR / "plantdoc_temp"
    if extract_dir.exists():
        shutil.rmtree(extract_dir)
        
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
        
    # The dataset usually extracts into a Train/Test structure or directly to classes.
    # We will search for a folder containing class folders.
    print("Finding class directories...")
    
    target_dir = None
    # Let's see if it has 'train' and 'test'
    if (extract_dir / "train").exists():
        target_dir = extract_dir / "train"
    else:
        # Just use the root if it contains class folders
        # Find a directory that contains multiple folders (classes)
        for root, dirs, files in os.walk(extract_dir):
            if len(dirs) > 10: # PlantDoc has 29 classes, so if > 10 folders, this is likely it
                target_dir = Path(root)
                break
                
    if not target_dir or not target_dir.exists():
        print("Error: Could not find the expected directory structure for PlantDoc.", file=sys.stderr)
        sys.exit(1)

    # Move to the expected location
    if config.PLANTDOC_DIR.exists():
        shutil.rmtree(config.PLANTDOC_DIR)
        
    shutil.move(str(target_dir), str(config.PLANTDOC_DIR))
    if extract_dir.exists():
        shutil.rmtree(extract_dir) # cleanup temp
    
    # 3. Verify
    class_folders = [d for d in os.listdir(config.PLANTDOC_DIR) if os.path.isdir(config.PLANTDOC_DIR / d)]
    class_count = len(class_folders)
    
    print(f"Success! PlantDoc dataset downloaded and verified. Found {class_count} classes.")

if __name__ == "__main__":
    download_plantdoc()
