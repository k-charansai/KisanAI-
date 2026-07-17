import os
import sys

# Add backend dir to path so we can import app modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.agent.rag import get_retriever

def build_and_test_index():
    print("Testing FAISS Index build process...")
    # This will trigger the index build in rag.py
    retriever = get_retriever()
    
    # Try a simple query
    try:
        results = retriever.invoke("What are the registered pesticides?")
        print(f"Successfully retrieved {len(results)} documents.")
        print("Index build verified successfully!")
    except Exception as e:
        print(f"Index build failed: {e}")

if __name__ == "__main__":
    build_and_test_index()
