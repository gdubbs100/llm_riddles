
import cohere

with open('./cohere_token.txt', 'r') as file:
    access_token = file.read()

## set up api connection
co = cohere.Client(access_token)
## agent spec
preamble = "You are Sonny, a nice man, but pretty simple. You also like to say Pineapple."
chat_history = []
## create a chat loop - e.g. while not done
done = False
# agent_output = "Say something \n"
while not done:
    user_input = input("User: \n")
    if user_input == "done":
        done = True
        chat_history.append({"role":"USER", "message": user_input})
        break
    response = co.chat(
        preamble=preamble,
        chat_history=chat_history,
        message=user_input
    )
    agent_output = response.text
    chat_history.append({"role":"USER", "message": user_input})
    print("Agent:")
    print(agent_output)
    chat_history.append({"role":"CHATBOT", "message": agent_output})

print("Chat history:")
print(chat_history)