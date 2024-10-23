import openai

class BaseAgent:
    def __init__(self, keywords, document_store):
        self.keywords = keywords
        self.document_store = document_store
    
    def respond_to_query(self, query):
        docs = self.document_store.retrieve_documents(query, self.keywords)
        context = " ".join(docs)
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful customer service assistant."},
                {"role": "user", "content": f"Query: {query}\nContext: {context}"}
            ],
            max_tokens=150,
            temperature=0.7,
        )
        return response.choices[0].message.content
