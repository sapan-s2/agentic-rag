from .base_agent import BaseAgent

class PaymentAgent(BaseAgent):
    def __init__(self, document_store):
        super().__init__(keywords=["payment_methods"], document_store=document_store)
