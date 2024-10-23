# import openai
# import redis

# openai.api_key = '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'
# # Connect to Redis
# # redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)



# class AgenticRAG:
#     def __init__(self, retriever):
#         self.retriever = retriever
    
#     def respond_to_query(self, query):
#         initial_docs = self.retriever(query)
#         refined_docs = self.multi_step_refinement(query, initial_docs)
#         response = self.generate_response(query, refined_docs)
#         return response
    
#     def multi_step_refinement(self, query, docs):
#         refined_docs = [doc for doc in docs if "return" in query.lower() and "return_policy" in doc]
#         if not refined_docs:
#             refined_docs = docs[:2]
#         return refined_docs
    
#     def generate_response(self, query, docs):
#         context = " ".join(docs)
#         response = openai.chat.completions.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": "system", "content": "You are a helpful customer service assistant."},
#                 {"role": "user", "content": f"Query: {query}\nContext: {context}"}
#             ],
#             max_tokens=150,
#             temperature=0.7,
#         )
#         return response.choices[0].message.content
