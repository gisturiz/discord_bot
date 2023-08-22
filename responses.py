import requests
import os

def handle_response(message) -> str:
    api_url = os.environ['INFERENCE_API']
    headers =  {"Content-Type":"application/json"}
    response = requests.post(api_url, json={'text': message}, headers=headers)
    response = response.json()
    answer = response['answer']
    url = response['url']

    return f"{answer}\n{url}"""
