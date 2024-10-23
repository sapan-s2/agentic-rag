import openai
from document_store import DocumentStore
# from agents.return_agent import ReturnAgent
from agents.shipping_agent import ShippingAgent
from agents.warranty_agent import WarrantyAgent
from agents.payment_agent import PaymentAgent
from agents.support_agent import SupportAgent
from coordinator import Coordinator

def main():
   
    document_store = DocumentStore()
    document_store.store_embeddings()
    
    
    # return_agent = ReturnAgent(document_store)
    shipping_agent = ShippingAgent(document_store)
    warranty_agent = WarrantyAgent(document_store)
    payment_agent = PaymentAgent(document_store)
    support_agent = SupportAgent(document_store)
    
    coordinator = Coordinator([
        # return_agent, 
        shipping_agent, 
        warranty_agent, 
        payment_agent, 
        support_agent
    ])
     
   
    while True:
        print("Menu:")
        print("1. Ask a question")
        print("2. Exit")
        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            query = input("Enter your query: ")
            # agent = AgenticRAG(retrieve_documents)
            # response = agent.respond_to_query(query)
            response = coordinator.route_query(query)
            print("Response:", response)
        elif choice == '2':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
   
   main()
