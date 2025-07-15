from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

def load_llm(model_name: str, user_api_key: str):
    if model_name == "Claude":
        print("[INFO] Loading Claude model...")
        return ChatAnthropic(
            model="claude-3-5-sonnet-20241022",
            api_key=user_api_key
        )
    elif model_name == "Deepseek":
        print("[INFO] Loading Deepseek model...")
        return ChatOpenAI(
            base_url='https://api.deepseek.com/v1',
            model='deepseek-chat',
            api_key=user_api_key,
            temperature=0.3
        )
    else:
        print("[INFO] Loading OpenAI GPT-4o model...")
        return ChatOpenAI(
            model="gpt-4o",
            api_key=user_api_key,
            temperature=0.0
        )