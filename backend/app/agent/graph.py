import os
import json
from typing import TypedDict, List
from langgraph.graph import StateGraph, END
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from app.agent.tools import get_weather
from app.agent.rag import get_retriever

class AdvisoryPlan(TypedDict):
    summary: str
    treatment_steps: List[str]
    weather_note: str
    estimated_cost_inr: str
    follow_up: str
    disclaimer: str

class AgentState(TypedDict):
    diagnosis: str
    location: str
    category: str
    weather_info: str
    plan: AdvisoryPlan

def determine_category(class_name: str):
    name = class_name.lower()
    if "healthy" in name:
        return "healthy"
    elif "blight" in name or "rust" in name or "spot" in name or "mold" in name or "scab" in name:
        return "fungal"
    elif "bacterial" in name:
        return "bacterial"
    elif "virus" in name or "mosaic" in name:
        return "viral"
    else:
        return "nutritional"

def get_weather_context(state: AgentState):
    """Tool node to fetch weather."""
    location = state.get("location", "India")
    weather_info = get_weather.invoke({"location": location})
    return {"weather_info": weather_info}

def fungal_expert(state: AgentState): return generate_plan_with_llm(state, "Fungal Expert")
def bacterial_expert(state: AgentState): return generate_plan_with_llm(state, "Bacterial Expert")
def viral_expert(state: AgentState): return generate_plan_with_llm(state, "Viral Expert")
def nutritional_expert(state: AgentState): return generate_plan_with_llm(state, "Nutritional Expert")

def generate_plan_with_llm(state: AgentState, role: str):
    if not os.environ.get("GROQ_API_KEY"):
        return {"plan": {
            "summary": "API Key missing. Cannot generate full advisory.",
            "treatment_steps": ["1. Check API Key", "2. Ensure GROQ_API_KEY is in .env"],
            "weather_note": "Unknown weather.",
            "estimated_cost_inr": "₹0 - ₹0",
            "follow_up": "Add the key to continue.",
            "disclaimer": "This is a placeholder."
        }}

    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0, max_retries=0)
    
    # RAG lookup
    retriever = get_retriever()
    docs = retriever.invoke(state["diagnosis"])
    context = "\n".join([d.page_content for d in docs])
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", f"You are a {role} and a certified Indian agronomist. Provide a treatment plan for a plant disease. Use this context:\n{context}\n\n"
                   "CRITICAL INSTRUCTIONS:\n"
                   "1. Do not give generic advice, give specific actionable steps a farmer can execute tomorrow morning.\n"
                   "2. Always name at least 2 specific registered pesticides with exact dosage and trade names.\n"
                   "3. Give spray timing relative to the weather data provided.\n"
                   "4. Include a resistance rotation note.\n"
                   "5. End with a cost estimate range in INR.\n\n"
                   "You MUST reply with ONLY valid JSON matching this schema:\n"
                   "{{\n"
                   '  "summary": "string",\n'
                   '  "treatment_steps": ["string", "string"],\n'
                   '  "weather_note": "string (incorporate the weather context)",\n'
                   '  "estimated_cost_inr": "string (e.g. ₹500 - ₹1200)",\n'
                   '  "follow_up": "string",\n'
                   '  "disclaimer": "string (always note this is AI advice)"\n'
                   "}}"),
        ("user", "Diagnosis: {diagnosis}\nWeather Context: {weather_info}")
    ])
    
    try:
        chain = prompt | llm
        response = chain.invoke({
            "diagnosis": state["diagnosis"],
            "weather_info": state["weather_info"]
        })
        
        # Simple JSON extraction
        text = response.content
        if "```json" in text:
            text = text.split("```json")[1].split("```")[0].strip()
        elif "```" in text:
            text = text.split("```")[1].split("```")[0].strip()
            
        plan = json.loads(text)
    except Exception as e:
        plan = {
            "summary": f"Failed to generate plan. Please verify your GROQ_API_KEY. (Error: {str(e)})",
            "treatment_steps": ["1. Check API Key", "2. Ensure the provided key has access to gemini-1.5-flash"],
            "weather_note": state["weather_info"] if state["weather_info"] else "Unknown weather.",
            "estimated_cost_inr": "₹0",
            "follow_up": "Fix API access to continue.",
            "disclaimer": "Fallback response."
        }
        
    return {"plan": plan}

def route_expert(state: AgentState):
    cat = state["category"].lower()
    if cat == "fungal": return "fungal_expert"
    elif cat == "bacterial": return "bacterial_expert"
    elif cat == "viral": return "viral_expert"
    else: return "nutritional_expert"

builder = StateGraph(AgentState)
builder.add_node("weather", get_weather_context)
builder.add_node("fungal_expert", fungal_expert)
builder.add_node("bacterial_expert", bacterial_expert)
builder.add_node("viral_expert", viral_expert)
builder.add_node("nutritional_expert", nutritional_expert)
builder.set_entry_point("weather")
builder.add_conditional_edges("weather", route_expert)
builder.add_edge("fungal_expert", END)
builder.add_edge("bacterial_expert", END)
builder.add_edge("viral_expert", END)
builder.add_edge("nutritional_expert", END)

graph = builder.compile()

def generate_treatment_plan(diagnosis: str, location: str) -> dict:
    initial_state = {
        "diagnosis": diagnosis,
        "location": location,
        "category": determine_category(diagnosis),
        "weather_info": "",
        "plan": {}
    }
    final_state = graph.invoke(initial_state)
    return final_state["plan"]

# --- Chat System ---
# In-memory store for chat sessions (for demo purposes)
chat_sessions = {}

def chat_with_agent(session_id: str, message: str) -> str:
    if not os.environ.get("GROQ_API_KEY"):
        return "I need a GROQ_API_KEY to chat."
        
    if session_id not in chat_sessions:
        chat_sessions[session_id] = [
            SystemMessage(content="You are KisanAI, a helpful agricultural assistant. Answer follow-up questions concisely based on the user's recent crop diagnosis.")
        ]
        
    history = chat_sessions[session_id]
    history.append(HumanMessage(content=message))
    
    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)
    response = llm.invoke(history)
    
    history.append(AIMessage(content=response.content))
    return response.content
