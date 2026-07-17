import torch
import torch.nn.functional as F
import numpy as np
import cv2

class GradCAM:
    """
    Grad-CAM (Gradient-weighted Class Activation Mapping) implementation.
    
    Target layer choice:
    For EfficientNet-B0, we use `model.features[-1]` as the target layer.
    This corresponds to the final Conv2dNormActivation block before the pooling
    and classifier head. This layer captures the highest-level semantic features
    while retaining spatial information, making it ideal for visualizing where
    the model is looking (e.g., leaf lesions vs background).
    """
    def __init__(self, model, target_layer):
        self.model = model
        self.target_layer = target_layer
        self.gradients = None
        self.activations = None
        
        # Register hooks
        self.target_layer.register_forward_hook(self.save_activation)
        self.target_layer.register_full_backward_hook(self.save_gradient)
        
    def save_activation(self, module, input, output):
        self.activations = output
        
    def save_gradient(self, module, grad_input, grad_output):
        # grad_output is a tuple
        self.gradients = grad_output[0]
        
    def __call__(self, x, class_idx=None):
        """
        Generates the Grad-CAM heatmap for the given input and class index.
        Returns a normalized numpy heatmap.
        """
        # Forward pass
        self.model.eval()
        output = self.model(x)
        
        if class_idx is None:
            # If no class specified, use the highest scoring class
            class_idx = output.argmax(dim=1).item()
            
        # Zero gradients
        self.model.zero_grad()
        
        # Target for backprop
        target = output[0, class_idx]
        target.backward()
        
        # Get gradients and activations
        gradients = self.gradients.detach().cpu().numpy()[0]
        activations = self.activations.detach().cpu().numpy()[0]
        
        # Global average pooling on the gradients
        weights = np.mean(gradients, axis=(1, 2))
        
        # Weight the channels by the gradients
        cam = np.zeros(activations.shape[1:], dtype=np.float32)
        for i, w in enumerate(weights):
            cam += w * activations[i]
            
        # ReLU (only positive influences)
        cam = np.maximum(cam, 0)
        
        # Normalize
        cam_max = np.max(cam)
        if cam_max > 0:
            cam = cam / cam_max
            
        return cam, class_idx

def overlay_heatmap(img_tensor, heatmap, alpha=0.5, colormap=cv2.COLORMAP_JET):
    """
    Helper to overlay the heatmap on the original image.
    img_tensor should be normalized in [0, 1] range of shape (3, H, W)
    Returns a numpy array representing the overlay image (RGB, [0, 255]).
    """
    # Resize heatmap to match image size
    img_np = img_tensor.cpu().numpy().transpose(1, 2, 0)
    
    # Un-normalize image if it was normalized for model input
    # Assuming standard ImageNet normalization was applied
    mean = np.array([0.485, 0.456, 0.406])
    std = np.array([0.229, 0.224, 0.225])
    img_np = std * img_np + mean
    img_np = np.clip(img_np, 0, 1)
    
    img_np = np.uint8(255 * img_np)
    
    heatmap = cv2.resize(heatmap, (img_np.shape[1], img_np.shape[0]))
    heatmap = np.uint8(255 * heatmap)
    heatmap = cv2.applyColorMap(heatmap, colormap)
    
    # OpenCV uses BGR, we want RGB
    heatmap = cv2.cvtColor(heatmap, cv2.COLOR_BGR2RGB)
    
    overlay = cv2.addWeighted(img_np, 1 - alpha, heatmap, alpha, 0)
    return overlay
