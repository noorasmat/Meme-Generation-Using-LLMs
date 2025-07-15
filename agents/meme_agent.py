from browser_use import Agent

def initialize_agent(task_prompt: str, llm_model, model_name: str) -> Agent:
    print("[INFO] Initializing agent...")
    return Agent(
        task=task_prompt,
        llm=llm_model,
        max_actions_per_step=5,
        max_failures=25,
        use_vision=(model_name != "Deepseek")
    )