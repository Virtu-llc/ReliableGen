import dotenv
dotenv.load_dotenv()

from currents.reliable_gen.agent import ReliableAgent
from currents.reliable_gen.config.config import Config
from currents.reliable_gen.tools.register import TOOLS, TOOL_MAP


config = Config(model='o3-mini')
agent = ReliableAgent(config, TOOLS, TOOL_MAP)
prompt = "list openai's competitors, gather information from your knowledge, reddit and google search, return sorted competitors"
response = agent.run(prompt)
print("user's prompt: ", prompt)
print("agent's response:", response)
