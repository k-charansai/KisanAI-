import os
import sys
import uuid
from typing import List, Optional
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

# Ensure we can import our modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.vision.service import diagnose_image
from app.agent.graph import generate_treatment_plan, chat_with_agent

app = FastAPI(title="KisanAI Backend API")

# Setup CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*", "https://your-app.vercel.app", "http://localhost:5173", "http://127.0.0.1:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

class DiagnoseResponse(BaseModel):
    disease: str
    display_name: str
    confidence: float
    is_healthy: bool
    gradcam_overlay_base64: str

class AdviseRequest(BaseModel):
    disease: str
    location: Optional[str] = "India"

class AdviseResponse(BaseModel):
    summary: str
    treatment_steps: List[str]
    weather_note: str
    estimated_cost_inr: str
    follow_up: str
    disclaimer: str

class ChatRequest(BaseModel):
    session_id: str
    message: str

class ChatResponse(BaseModel):
    reply: str

@app.get("/health")
def health_check():
    """Lightweight endpoint for UptimeRobot keep-alive."""
    return {"status": "ok"}

@app.post("/diagnose", response_model=DiagnoseResponse)
async def diagnose(file: UploadFile = File(...)):
    """
    Accepts a leaf image, runs ONNX vision model inference, 
    and generates Grad-CAM.
    """
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image.")
        
    image_bytes = await file.read()
    
    try:
        vision_result = diagnose_image(image_bytes)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Vision model error: {str(e)}")
        
    is_healthy = "healthy" in vision_result["class_name"].lower()
    
    return DiagnoseResponse(
        disease=vision_result["class_name"],
        display_name=vision_result["class_name"].replace("_", " ").title(),
        confidence=vision_result["confidence"],
        is_healthy=is_healthy,
        gradcam_overlay_base64=vision_result["gradcam_base64"]
    )

@app.post("/advise", response_model=AdviseResponse)
async def advise(req: AdviseRequest):
    try:
        # Pass the disease to LangGraph
        plan = generate_treatment_plan(req.disease, req.location)
        return AdviseResponse(**plan)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate advisory: {str(e)}")

@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    try:
        reply = chat_with_agent(req.session_id, req.message)
        return ChatResponse(reply=reply)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Chat error: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
