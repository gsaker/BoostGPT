from revChatGPT.V3 import Chatbot
chatbot = Chatbot(api_key="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")
while True:
    prompt = input("User:")
    print("AI:",end="")
    for data in chatbot.ask_stream(prompt):
        print(data, end="", flush=True)