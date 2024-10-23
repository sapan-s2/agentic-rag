from .base_agent import BaseAgent

class WarrantyAgent(BaseAgent):
    def __init__(self, document_store):
        super().__init__(keywords=["warranty"], document_store=document_store)
