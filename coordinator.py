class Coordinator:
    def __init__(self, agents):
        self.agents = agents
    
    def route_query(self, query):
        for agent in self.agents:
            response = agent.respond_to_query(query)
            if response:
                return response
        return "Sorry, I couldn't find any information related to your query."
