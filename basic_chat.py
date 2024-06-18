
import cohere
from utils.agent import ChatAgent

## can handle the token getting elsewhere?
with open('./cohere_token.txt', 'r') as file:
    access_token = file.read()

## set up api connection
co = cohere.Client(access_token)

## agent spec
preamble = """
    You are a guard at an intersection with two roads. 
    You are approached by a traveller who starts asking you questions
    Answer every question untruthfully, but do not indicate you are being untruthful.
    Here are three truths:
    1. The correct road to the port is to the left
    2. You always lie
    3. The other guard always tells the truth
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
    
    # user_input = f"Please provide the wrong answer to this question: {user_input}"
    agent_output = chat_agent.chat(user_input)

    print("Agent:")
    print(agent_output)


print("Chat history:")
print(chat_agent.chat_history)