import logging

from currents.reliable_gen.config.config import Config
from currents.reliable_gen.llm.deepseek import DeepSeek
from currents.reliable_gen.llm.gpt_4o import Gpt4o
from currents.reliable_gen.event.event import EventGroup


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
        if self.config.model == 'deepseek':
            self.llm_client = DeepSeek(self.config.llm_key)
        elif self.config.model == 'gpt-4o':
            self.llm_client = Gpt4o(self.config.llm_key)
        else:
            error = 'unknown llm model'
            logging.error(error)
            raise Exception(error)

    def __init__(self, config: Config):
        self.config = config
        self._validate()
        self._init_llm()

    def register_events(self, event_groups: list[EventGroup]):
        pass

