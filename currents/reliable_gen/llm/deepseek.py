import json
import logging

from openai import OpenAI


class DeepSeek:
    def __init__(self, key):
        self.client = OpenAI(api_key=key, base_url='https://api.deepseek.com')

    def chat(self, messages, json_format=True):
        if json_format:
            response = self.client.chat.completions.create(
                model='deepseek-chat',
                messages=messages,
                response_format={"type": "json_object"}
            )
        else:
            response = self.client.chat.completions.create(
                model='deepseek-chat',
                messages=messages,
            )
        content = response.choices[0].message.content
        return json.loads(content) if json_format else content

    def chat_with_tools(self, messages, tools):
        error = 'deepseek does not support chat with tools yet, please use other models'
        logging.error(error)
        raise Exception(error)
