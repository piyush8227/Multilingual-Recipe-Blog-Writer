import streamlit as st
from src.langgraphrecipeblogger.graph.graph_builder import generate_blog_workflow

# Page Title
st.title("🍲 Multilingual Recipe Blog Generator")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Sidebar Inputs
st.sidebar.header("📝 Enter Recipe Details")

recipe_name = st.sidebar.text_input("Recipe Name", placeholder="Shahi Paneer Masala")
headcount = st.sidebar.number_input("Serves how many people?", min_value=1, max_value=100, placeholder=4)
language = st.sidebar.selectbox("Preferred Language", ["English", "Hindi", "Marathi", "Tamil", "Gujarati"])

# Submit button
if st.sidebar.button("✍️ Generate Blog"):
    with st.spinner("Cooking up your blog... 🍳"):

        # User Input

        inputs = {
            "recipe_name": recipe_name,
            "headcount": headcount,
            "language": language
        }

        try:
            result = generate_blog_workflow.invoke(inputs)

            # Append Recipe blogs to session history
            st.session_state.chat_history.extend([
                {"role": "user", "content": f"🍽️ **Recipe**: `{recipe_name}` | 👥 **Serves**: {headcount} | 🌐 **Language**: {language}"},
                {"role": "assistant", "content": result["blog_post"]}
            ])

            st.success("✅ Blog generated!")

        except Exception as e:
            st.error(f"Something went wrong: {str(e)}")

# Display chat history in current session
st.markdown("---")

for i, msg in enumerate(st.session_state.chat_history):
    if msg["role"] == "user":
        st.markdown(f"👤 **You:** {msg['content']}")
    elif msg["role"] == "assistant":
        st.markdown(f"🤖 **AI:**\n{msg['content']}")
        st.markdown("---")