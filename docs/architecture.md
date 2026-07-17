# KisanAI Architecture

KisanAI uses a modern, decoupled architecture splitting the deep learning pipeline from the advisory agent logic.

## System Diagram

```mermaid
flowchart TD
    %% User & Frontend
    User([Farmer / User])
    Vercel[Frontend - React/Vite<br/>Hosted on Vercel]
    
    User -->|Uploads Leaf Image| Vercel
    User -->|Asks Follow-up| Vercel
    
    %% Backend Services
    subgraph Render [FastAPI Backend - Hosted on Render]
        API_Diag[POST /diagnose]
        API_Adv[POST /advise]
        API_Chat[POST /chat]
        
        %% Vision Component
        subgraph Vision [Vision Service]
            ONNX[ONNX Runtime<br/>EfficientNet-B0]
            GradCAM[OpenCV Grad-CAM Proxy]
        end
        
        %% Agent Component
        subgraph LangGraph_Agent [Advisory Agent]
            Planner{Disease<br/>Planner}
            ExpertF[Fungal Expert]
            ExpertB[Bacterial Expert]
            ExpertV[Viral Expert]
            ExpertN[Nutritional Expert]
            
            Planner --> ExpertF
            Planner --> ExpertB
            Planner --> ExpertV
            Planner --> ExpertN
        end
    end
    
    %% External Services
    subgraph External [External APIs & Data]
        Groq[Groq Llama-3.3-70b]
        Weather[Open-Meteo API]
        FAISS[(FAISS Vector DB<br/>Curated Markdown)]
    end
    
    %% Connections
    Vercel -->|Image| API_Diag
    Vercel -->|Location & Disease| API_Adv
    Vercel -->|Session ID & Text| API_Chat
    
    API_Diag --> Vision
    API_Adv --> LangGraph_Agent
    API_Chat --> Groq
    
    LangGraph_Agent --> Weather
    LangGraph_Agent --> Groq
    LangGraph_Agent --> FAISS
    
    %% Note styling
    classDef frontend fill:#15803D,stroke:#047857,color:white;
    classDef backend fill:#D97706,stroke:#B45309,color:white;
    classDef external fill:#475569,stroke:#334155,color:white;
    
    class Vercel frontend;
    class API_Diag,API_Adv,API_Chat,ONNX,GradCAM,Planner,ExpertF,ExpertB,ExpertV,ExpertN backend;
    class Groq,Weather,FAISS external;
```

## Component Details
1. **Frontend (Vite + React)**: A lightweight SPA enforcing a warm, agricultural aesthetic without heavy component libraries. Separates image upload, results display, and chat.
2. **Vision Service (ONNX Runtime)**: We exported the PyTorch EfficientNet-B0 model to `.onnx` to avoid the massive PyTorch dependency overhead on the free Render tier. Grad-CAM overlays are simulated dynamically via OpenCV color filtering for instant explainability.
3. **LangGraph Advisory Agent**: A directed graph routing the disease classification to specific prompt experts (fungal, bacterial, viral, nutritional). It enriches the prompt with real-time weather from Open-Meteo and specific treatments via FAISS RAG, then structures the output into JSON using Groq's Llama-3.3-70b-versatile model.
