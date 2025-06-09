# 🍲 Recipe Blog Generator (Multilingual)

Generate engaging, SEO-friendly, and humorous recipe blogs in multiple languages using AI and LangGraph-based workflows. Built with Streamlit and Langchain.

---

## 🚀 Features

- 📝 Accepts recipe name, headcount, and preferred language as input.
- 🤖 Automatically generates ingredients, instructions, and metadata via LangGraph worker nodes.
- ✍️ Outputs a well-structured blog in Markdown with humor and SEO best practices.
- 🌐 Multilingual support: English, Hindi, Marathi, Tamil, Gujarati.
- 🔁 **Chat session memory**: View past generated blogs with inputs for reference and comparison.
- 🧠 Built using LangChain, LangGraph, and Streamlit.
- 🧪 Orchestrator-Worker Workflow for modular AI task management.

---

## 💬 Chat Session History

The app uses Streamlit's session state (`st.session_state`) to maintain a **chat-like history of blog generations**. Every time a user submits a new recipe, their inputs and the generated blog are stored and displayed as part of the session history.

This allows users to:
- View and compare multiple recipe blogs without refreshing the page.
- Maintain context for multiple generations during a session.

This history can be extended for multi-turn memory in future using **LangGraph's persistent state flow**.

---

## 📁 Project Structure

```

recipe\_blog\_generator/
├── app.py                           # Streamlit frontend app
├── main.py                          # Optional main entry point
├── requirements.txt                 # Python dependencies
├── src/
    ├── config/
    │   └── settings.py                  # Configuration (API keys, etc.)
    ├── langgraphrecipeblogger/
    │   ├── graph/                       # LangGraph workflow builder
    │   ├── nodes/                       # Worker nodes for each task
    │   ├── state/                       # State schema
    │   └── utils/
    │       └── llm.py                   # LLM wrapper (e.g., Groq, OpenAI)
    ├── prompts/                         # Prompt templates for each node
    └── README.md                        # This file

````

---

## 🛠️ Prerequisites

- Python 3.9+
- An LLM API key (e.g., [Groq](https://console.groq.com/) or OpenAI)
- Optional: Hugging Face CLI and token (for deployment)

---

## 🔧 Installation

1. **Clone the repository**
```bash
git clone https://github.com/piyush8227/Multilingual-Recipe-Blog-Writer.git
cd Multilingual-Recipe-Blog-Writer
````

2. **Create and activate a virtual environment**

```bash
python -m venv <environment name>
source <environment name>/bin/activate  # On Windows use: <environment name>\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set your API key**

Edit `src.config/settings.py` and add your LLM key:

```python
GROQ_API_KEY = "your-groq-api-key"
```

---

## ▶️ Run the Streamlit App

```bash
streamlit run app.py
```

Your app will open in a browser at `http://localhost:8501`.

---

## 🧪 Sample Input

> **Recipe Name:** Chicken Butter Masala
> **Serves:** 2
> **Language:** English

App will auto-generate:

* Ingredients
* Cooking instructions
* Metadata
* Final blog in Markdown

---

## 👩‍🍳 Credits

Built with ❤️ using:

* [LangGraph](https://www.langchain.com/langgraph)
* [Streamlit](https://streamlit.io/)
* [Groq LLMs](https://console.groq.com/)
* [LangChain](https://www.langchain.com/)

---
