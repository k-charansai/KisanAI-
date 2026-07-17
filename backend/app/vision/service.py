import os
import json
import base64
import numpy as np
import onnxruntime as ort
from PIL import Image
import io
import cv2

# Hardcoded paths since this is running from backend directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "best_model.onnx")
LABELS_PATH = os.path.join(BASE_DIR, "class_labels.json")

# Load ONNX session
session = None
if os.path.exists(MODEL_PATH):
    session = ort.InferenceSession(MODEL_PATH)

# Load class labels
class_labels = {}
if os.path.exists(LABELS_PATH):
    with open(LABELS_PATH, "r") as f:
        class_labels = json.load(f)

def preprocess_image(image_bytes):
    img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    img = img.resize((224, 224))
    
    # Normalize (ImageNet stats)
    img_arr = np.array(img).astype(np.float32) / 255.0
    mean = np.array([0.485, 0.456, 0.406], dtype=np.float32)
    std = np.array([0.229, 0.224, 0.225], dtype=np.float32)
    img_arr = (img_arr - mean) / std
    
    # HWC to CHW
    img_arr = np.transpose(img_arr, (2, 0, 1))
    
    # Add batch dimension
    img_arr = np.expand_dims(img_arr, axis=0).astype(np.float32)
    return img_arr, np.array(img.resize((224, 224)))

def generate_proxy_gradcam(original_img):
    """
    Since ONNX doesn't support backprop for real Grad-CAM out of the box,
    we generate a proxy heatmap for the portfolio demo based on color contrast 
    to highlight non-green diseased spots.
    """
    hsv = cv2.cvtColor(original_img, cv2.COLOR_RGB2HSV)
    # Highlight areas that are not purely healthy green
    lower_green = np.array([35, 40, 40])
    upper_green = np.array([85, 255, 255])
    mask = cv2.inRange(hsv, lower_green, upper_green)
    
    heatmap = 255 - mask # Invert so non-green is hot
    heatmap = cv2.GaussianBlur(heatmap, (21, 21), 0)
    heatmap_color = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
    
    # Superimpose
    superimposed_img = heatmap_color * 0.4 + original_img * 0.6
    return superimposed_img.astype(np.uint8)

def determine_category(class_name):
    name = class_name.lower()
    if "healthy" in name:
        return "healthy"
    elif "blight" in name or "rust" in name or "spot" in name or "mold" in name or "scab" in name:
        return "fungal" # Simplification for demo
    elif "bacterial" in name:
        return "bacterial"
    elif "virus" in name or "mosaic" in name:
        return "viral"
    else:
        return "nutritional"

def diagnose_image(image_bytes):
    if not session:
        raise RuntimeError("ONNX model not found. Did you run Phase 2 export?")
        
    img_tensor, original_img = preprocess_image(image_bytes)
    
    # ONNX Inference
    input_name = session.get_inputs()[0].name
    outputs = session.run(None, {input_name: img_tensor})
    logits = outputs[0][0]
    
    # Softmax
    exp_logits = np.exp(logits - np.max(logits))
    probs = exp_logits / exp_logits.sum()
    
    pred_idx = np.argmax(probs)
    confidence = float(probs[pred_idx])
    class_name = class_labels.get(str(pred_idx), f"Class_{pred_idx}")
    
    # Generate Grad-CAM (Proxy)
    heatmap_img = generate_proxy_gradcam(original_img)
    
    # Convert to base64
    _, buffer = cv2.imencode('.jpg', cv2.cvtColor(heatmap_img, cv2.COLOR_RGB2BGR))
    b64_str = base64.b64encode(buffer).decode('utf-8')
    
    return {
        "class_name": class_name,
        "confidence": confidence,
        "gradcam_base64": b64_str,
        "category": determine_category(class_name)
    }
