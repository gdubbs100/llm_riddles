class ChatAgent:

    def __init__(self, client, preamble):
        self.preamble=preamble
        self.chat_history = []
        self.client = client

    def chat(self, message:str):
        ## TODO: might be something funny with your chat history here!
        response = self.client.chat(
            preamble=self.preamble,
            chat_history=self.chat_history[:-1],
            message=message
        )
        agent_output = response.text

        self.chat_history.append({"role":"USER", "message": message})
        self.chat_history.append({"role":"CHATBOT", "message": agent_output})

        return agent_output
