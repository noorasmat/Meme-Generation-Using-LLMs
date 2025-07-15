import asyncio
from llms.llm_selector import load_llm
from config.prompts import build_meme_task_prompt
from agents.meme_agent import initialize_agent
from utils.extract_url import find_imgflip_direct_link

async def run_meme_generation(user_input: str, selected_model: str, api_key: str) -> str | None:
    print("[INFO] Running meme generation process...")
    llm_instance = load_llm(selected_model, api_key)
    task_description = build_meme_task_prompt(user_input)
    meme_agent = initialize_agent(task_description, llm_instance, selected_model)

    try:
        agent_output = await meme_agent.run()
        return find_imgflip_direct_link(agent_output.final_result())
    except Exception as err:
        print(f"[ERROR] Agent execution failed: {err}")
        return None