import openai
import os
from dotenv import load_dotenv
from typing import Dict, List, Any

load_dotenv()

openai.api_key = os.environ.get("CHAT_GPT_API_TOKEN")

def get_gpt_response(question: str) -> str | None:
    
    response = openai.Completion.create(
        engine="davinci",
        prompt=question,
        max_tokens=50
    )

    if response:
        choices: List[Dict[str, Any]] = response.get("choices", None)
        if choices and len(choices) > 0:
            text: str = choices[0].get("text", None)
            return text
    return None