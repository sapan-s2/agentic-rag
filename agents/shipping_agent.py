from .base_agent import BaseAgent

class ShippingAgent(BaseAgent):
    def __init__(self, document_store):
        super().__init__(keywords=["shipping_info"], document_store=document_store)
