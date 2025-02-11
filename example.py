import dotenv
dotenv.load_dotenv()
import os

from currents.reliable_gen.agent import ReliableAgent
from currents.reliable_gen.config.config import Config
from currents.reliable_gen.tools.register import TOOLS, TOOL_MAP
from currents.reliable_gen.llm.prompts import generate_prompt

logs = []


def log_callback(msg):
    logs.append(msg)
    print(msg)


def complete_callback(task_output: dict):
    print(str(task_output.get('task_output', '')))

if __name__ == '__main__':

    config = Config(model='o3-mini', llm_key=os.getenv('OPENAI_API_KEY'), tools=TOOLS, tool_map=TOOL_MAP,
                    log_callback=log_callback, complete_callback=complete_callback)
    agent = ReliableAgent(config)
    interactive = False
    prompt = "list openai's competitors, gather information from your knowledge, reddit and google search, return sorted competitors"
    final_prompt = generate_prompt(prompt, interactive)
    agent.run(final_prompt)
