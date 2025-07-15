# AI Meme Generator Agent 🤖🎨

This is a Streamlit-based web app that uses browser automation and LLM agents to generate memes based on user input. It can browse ImgFlip, select templates, and generate meme captions!

## 💡 Features

- Choose from Claude, Deepseek, or OpenAI models
- Automates browser steps using `browser_use` agent
- Selects meme templates and fills top/bottom text
- Returns final meme image URL for sharing or embedding

## 🛠️ Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the app:

```bash
streamlit run main.py
```

3. Enter your API key for your chosen model and type a meme idea!

## 🔑 Requirements

- Claude API key (https://console.anthropic.com)
- Deepseek API key (https://platform.deepseek.com)
- OpenAI API key (https://platform.openai.com)

---
Built using [LangChain](https://github.com/langchain-ai/langchain) and [browser_use](https://github.com/Shubhamsaboo/awesome-llm-apps).