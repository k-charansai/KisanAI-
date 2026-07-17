import os
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DOCS_DIR = os.path.join(BASE_DIR, "rag", "advisory_docs")

_vectorstore = None

def get_retriever():
    global _vectorstore
    
    if _vectorstore is None:
        api_key = os.environ.get("GEMINI_API_KEY", "")
        if not api_key:
            print("GEMINI_API_KEY is missing. Skipping FAISS index build.")
            # Return a mock retriever if no API key
            class MockRetriever:
                def invoke(self, query):
                    return []
            return MockRetriever()

        print("Building FAISS index at deploy time...")
        try:
            # Load docs
            loader = DirectoryLoader(DOCS_DIR, glob="**/*.md", loader_cls=TextLoader)
            docs = loader.load()
            
            # Split
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
            splits = text_splitter.split_documents(docs)
            
            # Embed
            embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004", max_retries=0)
            _vectorstore = FAISS.from_documents(splits, embeddings)
        except Exception as e:
            print(f"Error building FAISS index (likely API key issue): {e}")
            class MockRetriever:
                def invoke(self, query):
                    return []
            return MockRetriever()
            
    return _vectorstore.as_retriever(search_kwargs={"k": 2})
