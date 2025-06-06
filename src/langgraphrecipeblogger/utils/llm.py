# langgraphrecipeblogger/utils/llm.py

from langchain_groq import ChatGroq
from src.config.settings import GROQ_API_KEY

# Instantiate a single shared Groq-based LLM instance
llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=GROQ_API_KEY)