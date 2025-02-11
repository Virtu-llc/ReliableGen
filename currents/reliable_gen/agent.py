import logging

from currents.reliable_gen.llm.o3_mini import O3Mini

from currents.reliable_gen.config.config import Config
from currents.reliable_gen.llm.deepseek import DeepSeek
from currents.reliable_gen.llm.gpt_4o import Gpt4o
from currents.reliable_gen.llm.o1 import O1


class ReliableAgent:
    def _validate(self):
        if self.config.use_llm:
            if not self.config.model or not self.config.llm_key:
                error = 'failed to init agent, parameters missing to create llm client'
                logging.error(error)
                raise Exception(error)

    def _init_llm(self):
        if not self.config.use_llm:
            self.llm_client = None
        elif self.config.model == 'o1':
            self.llm_client = O1(self.config.llm_key,
                                 tools=self.config.tools,
                                 tool_map=self.config.tool_map,
                                 complete_callback=self.config.complete_callback,
                                 log_callback=self.config.log_callback,
                                 exception_callback=self.config.exception_callback)

        elif self.config.model == 'o3-mini':
            self.llm_client = O3Mini(self.config.llm_key,
                                     tools=self.config.tools,
                                     tool_map=self.config.tool_map,
                                     complete_callback=self.config.complete_callback,
                                     log_callback=self.config.log_callback,
                                     exception_callback=self.config.exception_callback)
        else:
            error = 'unknown llm model'
            logging.error(error)
            raise Exception(error)

    def __init__(self, config: Config, ):
        self.config = config
        self._validate()
        self._init_llm()
        self.tools = config.tools,
        self.tool_map = config.tool_map,


    def run(self, prompt):
        messages = [
            {"role": "user", "content": prompt}
        ]
        if self.tools and self.tool_map:
            response = self.llm_client.chat_with_tools(messages)
        else:
            response = self.llm_client.chat(messages)
        return response
