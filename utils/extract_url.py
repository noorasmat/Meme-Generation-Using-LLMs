import re

def find_imgflip_direct_link(agent_output: str) -> str | None:
    print("[INFO] Extracting meme URL...")
    match = re.search(r'https://imgflip\.com/i/(\w+)', agent_output)
    if match:
        return f"https://i.imgflip.com/{match.group(1)}.jpg"
    return None