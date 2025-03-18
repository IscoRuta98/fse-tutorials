import os
from dotenv import load_dotenv
from pathlib import Path
from openai import OpenAI


dotenv_path = Path('path/to/.env')
load_dotenv(dotenv_path=dotenv_path)


client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": "Write a one-sentence bedtime story about a unicorn."
        }
    ]
)

print(completion.choices[0].message.content)