from .base_agent import BaseAgent

class ReturnAgent(BaseAgent):
    def __init__(self, document_store):
        super().__init__(keywords=["return_policy"], document_store=document_store)
