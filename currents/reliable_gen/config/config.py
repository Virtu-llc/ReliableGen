

class Config:
    def __init__(self, **kwargs):
        self.use_llm = kwargs.get('use_llm', False)
        self.model = kwargs.get('model', 'gpt-4o')
        self.llm_key = kwargs.get('llm_key', None)

