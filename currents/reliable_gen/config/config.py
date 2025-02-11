

class Config:
    def __init__(self, **kwargs):
        self.use_llm = kwargs.get('use_llm', True)
        self.model = kwargs.get('model', 'o1')
        self.llm_key = kwargs.get('llm_key', None)
        self.tools = kwargs.get('tools', None)
        self.tool_map = kwargs.get('tool_map', None)
        self.log_callback = kwargs.get('log_callback', None)
        self.complete_callback = kwargs.get('complete_callback', None)
        self.exception_callback = kwargs.get('exception_callback', None)


