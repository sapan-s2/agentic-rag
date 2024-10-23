import openai
import numpy as np

# Initialize OpenAI API with your key
openai.api_key = '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'

class DocumentStore:
    def __init__(self, file_path='documents/docs.txt'):
        self.file_path = file_path
        self.documents = self.load_documents()
        self.embeddings = {}

    def load_documents(self):
        documents = {}
        with open(self.file_path, 'r') as file:
            for line in file:
                if ':' in line:
                    key, doc = line.split(':', 1)
                    documents[key.strip()] = doc.strip()
        return documents

    def store_embeddings(self):
        for key, doc in self.documents.items():
            response = openai.embeddings.create(
                model="text-embedding-ada-002",
                input=doc
            )
            embedding = response.data[0].embedding
            self.embeddings[key] = embedding
    
    def retrieve_documents(self, query, keywords):
        response = openai.embeddings.create(
            model="text-embedding-ada-002",
            input=query
        )
        query_embedding = np.array(response.data[0].embedding)
        relevant_docs = []
        for key, embedding in self.embeddings.items():
            cos_sim = np.dot(query_embedding, embedding) / (np.linalg.norm(query_embedding) * np.linalg.norm(embedding))
            if cos_sim > 0.5 and any(keyword in key for keyword in keywords):
                relevant_docs.append(self.documents[key])
        return relevant_docs
