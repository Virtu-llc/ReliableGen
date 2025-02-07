

class Config:
    def __init__(self, **kwargs):
        self.use_llm = kwargs.get('use_llm', False)
        self.model = kwargs.get('model', 'o3-mini')
        self.llm_key = kwargs.get('llm_key', None)

