import logging
from http.client import responses

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

    def chat_with_tools(self, messages: list, tools, tool_map):
        first_call = True
        while True:
            response = self.client.chat.completions.create(
                model='gpt-4o',
                messages=messages,
                tools=tools,
                tool_choice="required" if first_call else "auto",
            )
            first_call = False
            tool_calls = response.choices[0].message.tool_calls
            if tool_calls:
                tool_messages = []
                for tool_call in tool_calls:
                    function_name = tool_call.function.name
                    args = json.loads(tool_call.function.arguments)
                    if function_name in tool_map:
                        function = tool_map[function_name]
                        result = function(**args)
                    else:
                        logging.error(f"Unknown function: {function_name}")
                        result = {"error": f"Unknown function {function_name}"}
                    tool_messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "name": function_name,
                        "content": json.dumps(result)  # Ensure this is JSON formatted
                    })
                messages.append(response.choices[0].message)
                messages.extend(tool_messages)
            else:
                return response.choices[0].message.content


