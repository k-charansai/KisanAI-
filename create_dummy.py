import os
from PIL import Image
import numpy as np
from pathlib import Path
import zipfile

def create_dummy_dataset():
    raw_data_dir = Path('ml/data/raw')
    raw_data_dir.mkdir(parents=True, exist_ok=True)
    
    # Create dummy zip so download.py skips downloading
    zip_path = raw_data_dir / 'plantvillage-dataset.zip'
    with zipfile.ZipFile(zip_path, 'w') as z:
        z.writestr('dummy.txt', 'dummy')

    color_dir = raw_data_dir / 'color'
    color_dir.mkdir(exist_ok=True)
    
    # 38 classes
    class_names = [f'Class_{i:02d}' for i in range(38)]
    
    for i, cls in enumerate(class_names):
        cls_dir = color_dir / cls
        cls_dir.mkdir(exist_ok=True)
        
        # Give each class a distinct color so the model can learn something
        # Color based on class index
        color = (
            (i * 10) % 255, 
            (i * 30) % 255, 
            (i * 50) % 255
        )
        
        # 10 images per class for fast training
        for j in range(10):
            img_arr = np.zeros((128, 128, 3), dtype=np.uint8)
            img_arr[:] = color
            
            # Add some random noise
            noise = np.random.randint(0, 20, (128, 128, 3), dtype=np.uint8)
            img_arr = np.clip(img_arr + noise, 0, 255).astype(np.uint8)
            
            img = Image.fromarray(img_arr)
            img.save(str(cls_dir / f'image_{j}.jpg'))
            
    print("Created dummy dataset.")

if __name__ == '__main__':
    create_dummy_dataset()
