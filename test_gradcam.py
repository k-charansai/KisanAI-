import torch
import cv2
import numpy as np
import os
from PIL import Image
import torchvision.transforms as transforms
from ml.src.models.efficientnet import get_model
from ml.src.gradcam import GradCAM, overlay_heatmap
from ml.src.config import NUM_CLASSES

def test_gradcam():
    print("Testing Grad-CAM...")
    device = torch.device('cpu')
    model = get_model(num_classes=NUM_CLASSES)
    # Don't need to load a real checkpoint if we just want to see if it generates *something*
    # However, if train.py created a checkpoint, we can load it.
    checkpoint_path = 'ml/checkpoints/best_model.pth'
    if os.path.exists(checkpoint_path):
        model.load_state_dict(torch.load(checkpoint_path, map_location=device, weights_only=True))
        print("Loaded checkpoint.")
    
    model.eval()
    
    target_layer = model.features[-1]
    cam = GradCAM(model, target_layer)
    
    img_path = 'ml/data/raw/PlantVillage/Class_00/image_0.jpg'
    image = Image.open(img_path).convert('RGB')
    
    preprocess = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    
    input_tensor = preprocess(image).unsqueeze(0).to(device)
    
    # Get heatmap for class 0
    heatmap, _ = cam(input_tensor, class_idx=0)
    
    # Overlay
    orig_img_cv = cv2.cvtColor(np.array(image.resize((224, 224))), cv2.COLOR_RGB2BGR)
    overlayed = overlay_heatmap(input_tensor[0], heatmap[0] if isinstance(heatmap, tuple) else heatmap)
    
    os.makedirs('docs', exist_ok=True)
    cv2.imwrite('docs/dummy_heatmap.jpg', overlayed)
    
    print("Heatmap shape:", heatmap.shape)
    print("Heatmap max:", heatmap.max(), "min:", heatmap.min())
    print("Saved docs/dummy_heatmap.jpg")

if __name__ == '__main__':
    test_gradcam()
