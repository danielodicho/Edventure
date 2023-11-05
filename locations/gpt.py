from gps import *
import openai

openai.api_key = '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'

def get_response(context, prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
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