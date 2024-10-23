from .base_agent import BaseAgent

class SupportAgent(BaseAgent):
    def __init__(self, document_store):
        super().__init__(keywords=["customer_support"], document_store=document_store)
