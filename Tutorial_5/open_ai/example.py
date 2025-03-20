# This script is an example of how to use the OpenAI API to generate text using the GPT-4 model.
# The script sends a request to the OpenAI API to generate a one-sentence bedtime story about a unicorn.
# The response is then printed to the console.
import os

from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": "Write a one-sentence bedtime story about a unicorn.",
        }
    ],
)

print(completion.choices[0].message.content)
