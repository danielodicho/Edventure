from gps import *
import openai

openai.api_key = ''

def get_response(context, prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": context},
            {"role": "user", "content": prompt}
        ]
    )
    # Extract the response
    if response.choices:
        return response.choices[0].message['content']
    else:
        raise Exception("OpenAI GPT didn't provide an answer.")
