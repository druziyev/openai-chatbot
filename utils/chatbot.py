import openai
import os
from dotenv import load_dotenv


# Obtaining API KEY from virtual environment
load_dotenv()
openai.api_key=os.environ.get('OPENAI_API')


def chat(prompt):
    """
    Receiving a prompt and getting a response from ChatGPT
    """
    
    print('Retrieving data from OpenAI...')
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )

    return response.choices[0].message.content


# This is a test run of the script
if __name__ == "__main__":
    prompt = 'How to learn Python?'

    response = chat(prompt=prompt)
    print(response)