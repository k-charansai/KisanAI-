import torch
import sys
from pathlib import Path

# Add src to python path so we can import modules
sys.path.append(str(Path(__file__).resolve().parent.parent))
from src import config
from src.models.efficientnet import get_model

def export_to_onnx():
    print("--- Phase 2: Exporting Model to ONNX ---")
    
    if not config.CHECKPOINT_DIR.joinpath("best_model.pt").exists():
        print("Error: best_model.pt not found. Train the model first.")
        sys.exit(1)
        
    print(f"Loading PyTorch model from {config.CHECKPOINT_DIR / 'best_model.pt'}...")
    model = get_model(num_classes=config.NUM_CLASSES)
    model.load_state_dict(torch.load(config.CHECKPOINT_DIR / "best_model.pt", map_location='cpu', weights_only=True))
    model.eval()
    
    # Create dummy input matching the EfficientNet-B0 input shape
    dummy_input = torch.randn(1, 3, config.IMAGE_SIZE, config.IMAGE_SIZE)
    
    onnx_path = config.ONNX_MODEL_PATH
    print(f"Exporting to {onnx_path}...")
    
    torch.onnx.export(
        model, 
        dummy_input, 
        str(onnx_path), 
        export_params=True, 
        opset_version=12,
        do_constant_folding=True,
        input_names=['input'], 
        output_names=['output'], 
        dynamic_axes={'input': {0: 'batch_size'}, 'output': {0: 'batch_size'}}
    )
    
    print("Export successful!")
    print("This ONNX model will be used by the FastAPI backend in Phase 3.")
    
    # Optional: Verify the ONNX model if onnx is installed
    try:
        import onnx
        onnx_model = onnx.load(str(onnx_path))
        onnx.checker.check_model(onnx_model)
        print("ONNX model verified successfully with onnx.checker.")
    except ImportError:
        print("Note: 'onnx' package not installed, skipping verification step.")

if __name__ == "__main__":
    export_to_onnx()
