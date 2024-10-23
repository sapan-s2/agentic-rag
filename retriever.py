# # src/retriever.py
# def retrieve_documents(query):
#     documents = {
#         "return_policy": "To return a product, you must contact customer support within 30 days...",
#         "shipping_info": "Our shipping times vary based on location. Typically, it takes 5-7 business days...",
#         "warranty": "All products come with a 1-year warranty covering manufacturing defects..."
#     }
#     relevant_docs = [doc for key, doc in documents.items() if any(word in query.lower() for word in key.split('_'))]
#     return relevant_docs
