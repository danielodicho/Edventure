from gps import *
import openai

openai.api_key = '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'

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
