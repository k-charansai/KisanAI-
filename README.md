# KisanAI 🌾

An AI-powered crop disease diagnosis and advisory tool. Built as a portfolio project demonstrating end-to-end machine learning engineering: from dataset curation and transfer learning to agentic LLM orchestration and web deployment.

![KisanAI Demo](docs/demo.gif)
*(Note: Replace this placeholder with a recorded demo of the Vercel frontend in action)*

## What It Does
1. **Diagnose**: Upload a photo of a plant leaf. The system identifies the disease using an EfficientNet-B0 vision model and highlights the affected regions via Grad-CAM.
2. **Advise**: An intelligent LangGraph agent generates a customized treatment plan, pulling real-time local weather context and retrieving domain-specific treatments from a local FAISS index.
3. **Chat**: Ask follow-up questions about the treatment (e.g., "Where can I buy copper fungicide?").

## Architecture
See the detailed [Architecture Diagram](docs/architecture.md) for the complete flow.

- **Vision Model**: EfficientNet-B0, fine-tuned in PyTorch using class-weighted loss to handle dataset imbalances. Exported to ONNX for lightweight inference.
- **Backend**: FastAPI running on Render.
- **Agent Orchestration**: LangGraph routes prompts to specialized expert nodes (Fungal, Bacterial, Viral). Uses Groq (Llama-3.3-70b-versatile) and LangChain for RAG.
- **Frontend**: React (Vite) deployed on Vercel.

## Honest Metrics & Field Validation
This project was evaluated on the **PlantVillage** dataset (lab conditions) and field-validated on the **PlantDoc** dataset (real-world conditions) to demonstrate the domain shift challenge.

| Dataset | Accuracy | Condition |
| --- | --- | --- |
| **PlantVillage** | `99.66%` | Controlled lab environments. |
| **PlantDoc** | `Pending` | Real-world field evaluation pending. |

**Observation:** As documented in `docs/model_metrics.md`, the model achieves exceptional 99.66% accuracy on the lab-controlled PlantVillage dataset. Field validation on PlantDoc is pending, but an accuracy drop is expected.

## Deployment Constraints
- **Render Free Tier**: The backend is hosted on a free Render tier, which spins down after 15 minutes of inactivity. The first API request may take ~50 seconds to cold-start.
- **UptimeRobot**: To mitigate the cold-start issue during portfolio reviews, an UptimeRobot monitor pings the `/health` endpoint every 10 minutes.

## Local Setup

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
# Ensure you have your .env file with GEMINI_API_KEY
uvicorn app.main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## Privacy Note
This is a portfolio demonstration project, not a production tool for active farm management. Any images uploaded are processed entirely in memory by the Render backend and are **never saved or used for retraining**. Do not upload sensitive or personal images.
