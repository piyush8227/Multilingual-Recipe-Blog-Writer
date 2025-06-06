import os
from dotenv import load_dotenv

# Conditions where you end-up getting wrong env variable from different envs, so override it to fetch from working directory
load_dotenv(dotenv_path=os.path.join(os.getcwd(), ".env"), override=True)

# Expose your Groq API key to the environment
GROQ_API_KEY = os.getenv("GROQ_API_KEY")