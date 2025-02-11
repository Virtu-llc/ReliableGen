import logging
import sys

from openai import OpenAI
from datetime import datetime
import json


class O3Mini:
    def __init__(self, key, tools=None,
                 tool_map=None,
                 log_callback:callable=None,
                 complete_callback:callable=None,
                 interactive=False):
        self.client = OpenAI(api_key=key)
        self.tools = tools
        self.tool_map = tool_map
        self.interactive = interactive
        self.logs = []
        self.log_callback = log_callback
        self.complete_callback = complete_callback

    def chat(self, messages, json_format=True):
        if json_format:
            response = self.client.chat.completions.create(
                model='o3-mini',
                messages=messages,
                response_format={"type": "json_object"}
            )
        else:
            response = self.client.chat.completions.create(
                model='o3-mini',
                messages=messages,
            )
        content = response.choices[0].message.content
        result = json.loads(content) if json_format else content
        if self.complete_callback:
            self.complete_callback(result)

    def chat_with_tools(self, messages: list):
        try:
            while True:
                response = self.client.chat.completions.create(
                    model='o3-mini',
                    messages=messages,
                    tools=self.tools
                )
                message = response.choices[0].message
                content = response.choices[0].message.content
                tool_calls = response.choices[0].message.tool_calls
                if content:
                    msg = f'\nAgent message:, {content}'
                    self.log(msg)
                    messages.append({"role": "assistant", "content": message.content})
                    if not self.interactive:
                        messages.append({"role": "user", "content": "Please continue to the next step."})
                    else:
                        # todo: retrieve user's reply
                        pass
                if tool_calls:
                    tool_messages = []
                    for tool_call in tool_calls:
                        function_name = tool_call.function.name
                        if function_name in self.tool_map:
                            function = self.tool_map[function_name]
                            args = json.loads(tool_call.function.arguments)
                            result = function(**args)
                            self.log(f'Tool call {function_name}: result: {json.dumps(result)}')
                            if function_name == 'complete_task':
                                msg = f'Agent task completed'
                                self.log(msg)
                                if self.complete_callback:
                                    self.complete_callback(args)
                                return
                        else:
                            msg = f'Unknown function: {function_name}'
                            logging.error(msg)
                            self.log(msg)
                            result = {"error": f"Unknown function {function_name}"}
                        tool_messages.append({
                            "role": "tool",
                            "tool_call_id": tool_call.id,
                            "name": function_name,
                            "content": json.dumps(result)  # Ensure this is JSON formatted
                        })
                    if tool_messages:
                        messages.append(response.choices[0].message)
                        messages.extend(tool_messages)
                    else:
                        messages.append({"role": "user", "content": "Please continue to the next step."})
        except Exception as e:
            msg = f'o3-mini error: {sys.exc_info()[0]}, {e}'
            logging.error(msg)
            self.log(msg)

    def log(self, msg):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log = f'\n{timestamp} {msg}'
        if self.log_callback:
            self.log_callback(log)
