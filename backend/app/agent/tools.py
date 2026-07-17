import requests
from langchain_core.tools import tool

@tool
def get_weather(location: str) -> str:
    """Gets the current weather for a location to help tailor the treatment plan.
    Uses open-meteo API. If it fails, returns a fallback message."""
    try:
        # Simplification for demo: Hardcoding lat/lon for New Delhi
        lat, lon = 28.6139, 77.2090
        
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        
        data = response.json()
        cw = data.get("current_weather", {})
        temp = cw.get("temperature", "unknown")
        wind = cw.get("windspeed", "unknown")
        
        return f"Current weather in {location} (approx): {temp}C, wind {wind}km/h."
        
    except Exception as e:
        return f"Weather data currently unavailable ({str(e)}). Provide general treatment advice."
