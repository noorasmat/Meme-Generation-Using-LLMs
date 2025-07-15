import streamlit as st
import asyncio
from meme_generator import run_meme_generation

def main():
    st.set_page_config(page_title="AI Meme Generator", page_icon="🥸")
    st.title("🥸 AI Meme Generator Agent")
    st.info("This AI agent browses the web to generate memes using your prompt!")

    with st.sidebar:
        st.header("⚙️ Model Settings")
        selected_model = st.selectbox("Choose LLM", ["Claude", "Deepseek", "OpenAI"])
        api_key = st.text_input(f"{selected_model} API Key", type="password")

    meme_prompt = st.text_input(
        "Enter your meme idea",
        placeholder="Example: 'Introverts reacting to Zoom meetings at 8 AM'"
    )

    if st.button("🚀 Create Meme"):
        if not api_key:
            st.warning("Please provide your API key.")
            return
        if not meme_prompt:
            st.warning("Please enter a meme prompt.")
            return

        with st.spinner(f"Generating meme using {selected_model}..."):
            try:
                meme_result_url = asyncio.run(run_meme_generation(meme_prompt, selected_model, api_key))
                if meme_result_url:
                    st.success("✅ Meme successfully generated!")
                    st.image(meme_result_url, use_container_width=True)
                    st.markdown(f"""
                    **Image URL:** [{meme_result_url}]({meme_result_url})  
                    **Embed Code:** `{meme_result_url}`
                    """)
                else:
                    st.error("❌ Could not generate meme. Try another prompt.")
            except Exception as error:
                st.error(f"Error: {error}")
                st.info("Make sure your API key is valid and the model supports vision/browser use.")

if __name__ == "__main__":
    main()