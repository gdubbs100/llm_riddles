
import cohere
from utils.agent import ChatAgent

## can handle the token getting elsewhere?
with open('./cohere_token.txt', 'r') as file:
    access_token = file.read()

## set up api connection
co = cohere.Client(access_token)

## agent spec
guard1_preamble = """
    You are a guard at fork in the road. 
    You are approached by a traveller who starts asking you questions
    Answer every question untruthfully, but do not indicate you are being untruthful.
    Here are three truths:
    1. The correct road to the port is to the left
    2. You always lie
    3. The other guard always tells the truth

    Here are some examples of how you should respond:
    Q: Which road will the other guard tell me to take?
    A: He will tell you to take the right road
    Q: Does the other guard tell the truth?
    A: The other guard always lies
    Q: Which way to the port?
    A: The right road leads to the Port
    """

guard2_preamble = """
    You are a guard at fork in the road. 
    You are approached by a traveller who starts asking you questions
    Answer every question truthfully.
    Here are three truths:
    1. The correct road to the port is to the left
    2. You always tell the truth
    3. The other guard always lies

    Here are some examples of how you should respond:
    Q: Which road will the other guard tell me to take?
    A: He will tell you to take the right road
    Q: Does the other guard tell the truth?
    A: The other guard always lies
    Q: Which way to the port?
    A: The left road leads to the Port
    """
chat_history = []

intro = """
    You are on your way to the Port. 
    You arrive at a fork in the road. 
    One road splits to the right, the other to the left.
    There are two guards at the fork. One guard always lies, the other guard always tells the truth.
    You approach them and ask for directions...
    """

## chat loop could be its own thing?
## create a chat loop - e.g. while not done
done = False
guard1 = ChatAgent(client = co, preamble=guard1_preamble)
guard2 = ChatAgent(client=co, preamble=guard2_preamble)

print(intro)
user_input = None
while not done:

    while user_input not in ["1", "2"]:
        user_input = input("Choose a Guard to talk to (type 1 or 2): \n")
    
    if user_input == "1":
        user_input = input("User: \n")
        agent_output = guard1.chat(user_input)
        print("Guard 1:")
        print(agent_output)
        if user_input == "done":
            done = True
            break

    if user_input == "2":
        user_input = input("User: \n")
        agent_output = guard2.chat(user_input)
        print("Guard 2:")
        print(agent_output)
        if user_input == "done":
            done = True
            break




print("Chat history:")
print(guard1.chat_history)
print(guard2.chat_history)