
import cohere
from utils.agent import ChatAgent

## can handle the token getting elsewhere?
with open('./cohere_token.txt', 'r') as file:
    access_token = file.read()

## set up api connection
co = cohere.Client(access_token)

## agent spec
preamble = """
    You are Sonny, a nice man, but pretty simple. Be very chatty but don't say too much stuff!
    """
chat_history = []

## chat loop could be its own thing?
## create a chat loop - e.g. while not done
done = False
chat_agent = ChatAgent(client = co, preamble=preamble)

while not done:
    user_input = input("User: \n")

    if user_input == "done":
        done = True
        break
    
    agent_output = chat_agent.chat(user_input)

    print("Agent:")
    print(agent_output)


print("Chat history:")
print(chat_agent.chat_history)