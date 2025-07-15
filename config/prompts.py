def build_meme_task_prompt(user_prompt: str) -> str:
    print("[INFO] Creating task description...")
    return (
        "You are an expert meme generator. Follow these steps:\n"
        "1. Go to https://imgflip.com/memetemplates\n"
        "2. Search for a main action verb in the prompt: '{0}'\n"
        "3. Select a matching meme template\n"
        "4. Add Top and Bottom Text relevant to: '{0}'\n"
        "5. Ensure the meme preview makes sense. Retry if needed.\n"
        "6. Generate meme and return image URL\n"
    ).format(user_prompt)