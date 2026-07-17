import os
from pathlib import Path
from PIL import Image
import torch
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
from sklearn.model_selection import train_test_split
import sys

# Adjust path to import config
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
from src import config

class PlantVillageDataset(Dataset):
    """
    Custom Dataset for PlantVillage to allow for explicit train/val splits
    at the image level, and applying different transforms depending on the split.
    
    Why explicit paths instead of ImageFolder + random_split?
    PyTorch's random_split wraps a single dataset, meaning train and val
    would share the same transform pipeline. We explicitly need different 
    transforms (augmented for train, clean for eval).
    """
    def __init__(self, image_paths, labels, transform=None):
        self.image_paths = image_paths
        self.labels = labels
        self.transform = transform

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, idx):
        img_path = self.image_paths[idx]
        label = self.labels[idx]
        
        # Load image (convert to RGB in case of some grayscale or alpha channels)
        image = Image.open(img_path).convert("RGB")
        
        if self.transform:
            image = self.transform(image)
            
        return image, label

def get_transforms():
    """
    Returns the train and validation transform pipelines.
    Train uses augmentation, eval uses clean resizes.
    """
    train_transform = transforms.Compose([
        transforms.RandomResizedCrop(config.IMAGE_SIZE),
        transforms.RandomHorizontalFlip(),
        transforms.RandomRotation(15),
        transforms.ColorJitter(brightness=0.2, contrast=0.2),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    
    val_transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(config.IMAGE_SIZE),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    
    return train_transform, val_transform

def load_data(val_split=0.2, random_seed=42):
    """
    Scans the PlantVillage directory, extracts paths and labels,
    splits them into train and val, and returns DataLoaders and class mapping.
    """
    if not config.PLANTVILLAGE_DIR.exists():
        raise FileNotFoundError(f"Dataset directory not found: {config.PLANTVILLAGE_DIR}")
        
    class_names = sorted([d.name for d in config.PLANTVILLAGE_DIR.iterdir() if d.is_dir()])
    class_to_idx = {cls_name: i for i, cls_name in enumerate(class_names)}
    
    all_image_paths = []
    all_labels = []
    
    for class_name in class_names:
        class_dir = config.PLANTVILLAGE_DIR / class_name
        for img_path in list(class_dir.glob('*.JPG')) + list(class_dir.glob('*.jpg')):
            all_image_paths.append(img_path)
            all_labels.append(class_to_idx[class_name])
            
    # Stratified split to ensure balance across train/val
    train_paths, val_paths, train_labels, val_labels = train_test_split(
        all_image_paths, all_labels, 
        test_size=val_split, 
        random_state=random_seed, 
        stratify=all_labels
    )
    
    train_transform, val_transform = get_transforms()
    
    train_dataset = PlantVillageDataset(train_paths, train_labels, transform=train_transform)
    val_dataset = PlantVillageDataset(val_paths, val_labels, transform=val_transform)
    
    train_loader = DataLoader(train_dataset, batch_size=config.BATCH_SIZE, shuffle=True, num_workers=4, pin_memory=True)
    val_loader = DataLoader(val_dataset, batch_size=config.BATCH_SIZE, shuffle=False, num_workers=4, pin_memory=True)
    
    return train_loader, val_loader, class_names, train_labels
