## A reliable AI agent framework.
build your ai agent in 5 minutes.


## Architecture 
![architecture](https://github.com/user-attachments/assets/0da1ce78-6318-4aac-af4e-6bad04dae72c)

## How to create your own agent in 5 minutes:
1. Define tools
2. Init an Agent with tools
3. Call agent with a prompt

Example:

```
config = Config()
agent = ReliableAgent(config, TOOLS, TOOL_MAP)
prompt = "list openai's competitors, return sorted competitors"
response = agent.run(prompt)
print("user's prompt: ", prompt)
print("agent's response:", response)

### 
user's prompt:  list openai's competitors, return sorted competitors
agent's response: The sorted list of OpenAI's competitors is: competitor4, competitor3, competitor2, competitor1.
```
