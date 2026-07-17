import torch
import torch.nn as nn
from torchvision import models
from torchvision.models import EfficientNet_B0_Weights

def get_model(num_classes):
    """
    Returns an EfficientNet-B0 model pre-trained on ImageNet,
    with a modified classifier head for `num_classes`.
    """
    # Load pre-trained model
    weights = EfficientNet_B0_Weights.DEFAULT
    model = models.efficientnet_b0(weights=weights)
    
    # Modify the classifier
    in_features = model.classifier[1].in_features
    model.classifier[1] = nn.Linear(in_features, num_classes)
    
    return model

def freeze_backbone(model):
    """
    Freezes all layers in the model except the classifier head.
    Used for Phase 1 of transfer learning.
    """
    for param in model.parameters():
        param.requires_grad = False
        
    for param in model.classifier.parameters():
        param.requires_grad = True

def unfreeze_last_n_blocks(model, n=2):
    """
    Unfreezes the last 'n' blocks of the features extractor,
    as well as the classifier head.
    For EfficientNet-B0, model.features contains the blocks.
    model.features[-1] is the final Conv2dNormActivation.
    model.features[-2] is the last MBConv block.
    """
    # Ensure classifier remains unfrozen
    for param in model.classifier.parameters():
        param.requires_grad = True
        
    # Unfreeze the last n layers in the features sequential
    num_features = len(model.features)
    for i in range(num_features - n, num_features):
        for param in model.features[i].parameters():
            param.requires_grad = True
