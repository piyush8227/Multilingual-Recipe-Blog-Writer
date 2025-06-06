import streamlit as st
from src.langgraphrecipeblogger.graph.graph_builder import generate_blog_workflow

# Title
st.title("🍲 Multilingual Recipe Blog Generator")

# Sidebar Inputs
st.sidebar.header("📝 Enter Recipe Details")

recipe_name = st.sidebar.text_input("Recipe Name", "Shahi Paneer Masala")
headcount = st.sidebar.number_input("Serves how many people?", min_value=1, max_value=100, value=4)
language = st.sidebar.selectbox("Preferred Language", ["English", "Hindi", "Marathi", "Tamil", "Gujarati"])

# Submit
if st.button("✍️ Generate Blog"):
    with st.spinner("Cooking up your blog... 🍳"):

        # Send to LangGraph workflow
        inputs = {
            "recipe_name": recipe_name,
            "headcount": headcount,
            "language": language
        }

        try:
            # Invoke your LangGraph workflow (synchronously or asynchronously)
            result = generate_blog_workflow.invoke(inputs)

            # Show output
            st.success("✅ Blog generated!")
            st.write(result["blog_post"])

        except Exception as e:
            st.error(f"Something went wrong: {str(e)}")
