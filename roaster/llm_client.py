from groq import Groq
import os
from dotenv import load_dotenv
from roaster.prompt_builder import build_roast_prompt

load_dotenv()    # reads .env file

def generate_roast(report):

    prompt = build_roast_prompt(report)
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

    response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "user", "content": prompt}
    ]
    )

    roast_text = response.choices[0].message.content

    return roast_text