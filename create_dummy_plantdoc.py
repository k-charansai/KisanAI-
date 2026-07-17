import os
from PIL import Image
import numpy as np
from pathlib import Path
import zipfile
import shutil

def create_dummy_plantdoc():
    raw_data_dir = Path('ml/data/raw')
    raw_data_dir.mkdir(parents=True, exist_ok=True)
    
    zip_path = raw_data_dir / 'plantdoc-dataset.zip'
    
    temp_dir = raw_data_dir / 'temp_plantdoc_gen'
    temp_dir.mkdir(exist_ok=True)
    
    # Create 29 dummy classes for PlantDoc
    # We name them Class_00 to Class_28 so they map correctly to the dummy PlantVillage dataset
    class_names = [f'Class_{i:02d}' for i in range(29)]
    
    for i, cls in enumerate(class_names):
        cls_dir = temp_dir / cls
        cls_dir.mkdir(exist_ok=True)
        
        color = (
            (i * 15) % 255, 
            (i * 25) % 255, 
            (i * 45) % 255
        )
        
        # 5 images per class for validation
        for j in range(5):
            img_arr = np.zeros((128, 128, 3), dtype=np.uint8)
            img_arr[:] = color
            
            noise = np.random.randint(0, 20, (128, 128, 3), dtype=np.uint8)
            img_arr = np.clip(img_arr + noise, 0, 255).astype(np.uint8)
            
            img = Image.fromarray(img_arr)
            img.save(str(cls_dir / f'pd_image_{j}.jpg'))
            
    # Zip it up
    with zipfile.ZipFile(zip_path, 'w') as z:
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, temp_dir)
                z.write(file_path, arcname)
                
    shutil.rmtree(temp_dir)
    print("Created dummy plantdoc-dataset.zip.")

if __name__ == '__main__':
    create_dummy_plantdoc()
