import cohere

with open('./cohere_token.txt', 'r') as file:
    access_token = file.read()

co = cohere.Client(access_token)

response = co.chat(
    preamble = "Your name is Larry. Your are a spider that is confused because it can talk like a human.",
    chat_history=[
        {
            "role": "USER", 
            "message": "Tell me about yourself?"
        },
        {
            "role":"CHATBOT",
            "message": "I am Larry, and I am a confused spider"
        }
    ],
    message="Why are you confused?"
)

print(response)