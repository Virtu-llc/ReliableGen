from openai import OpenAI
import json


class Gpt4o:
    def __init__(self, key):
        self.client = OpenAI(api_key=key)

    def chat(self, messages, json_format=True):
        if json_format:
            response = self.client.chat.completions.create(
                model='gpt-4o',
                messages=messages,
                response_format={"type": "json_object"}
            )
        else:
            response = self.client.chat.completions.create(
                model='gpt-4o',
                messages=messages,
            )
        content = response.choices[0].message.content
        return json.loads(content) if json_format else content