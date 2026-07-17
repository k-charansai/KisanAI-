import os
import sys
from fastapi.testclient import TestClient
import numpy as np
from PIL import Image
import io

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(BASE_DIR, "backend"))

from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
    print("Health check passed.")

def test_diagnose():
    # Create a dummy image
    img = Image.fromarray(np.uint8(np.random.rand(224, 224, 3) * 255))
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='JPEG')
    img_bytes = img_byte_arr.getvalue()
    
    response = client.post(
        "/diagnose",
        files={"file": ("dummy.jpg", img_bytes, "image/jpeg")}
    )
    
    assert response.status_code == 200
    data = response.json()
    print("Diagnosis passed! Response keys:", data.keys())
    print("Class:", data["class_name"])
    print("Confidence:", data["confidence"])
    print("Treatment plan preview:", data["treatment_plan"][:50])

if __name__ == "__main__":
    test_health()
    test_diagnose()
