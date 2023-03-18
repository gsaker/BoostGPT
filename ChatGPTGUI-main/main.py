import openai
openai.api_key = "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"
from revChatGPT.V3 import Chatbot
chatbot = Chatbot(api_key="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")

result = ''
while True:
    promptcount = 0
    prompt = []
    prompt.append(input("Enter an input"))
    contentcount = 0
    content = []
    #result += "User:"+prompt+"\n"
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a chatbot"},
            {"role": "user", "content": "{prompt[0]}"},
            {"role": "assistant", "content": "{content[0]}"},
            {"role": "user", "content": "{prompt[1]}"},
        ]
)
    for choice in response.choices:
        result += choice.message.content+"\n"
        content.append(choice.message.content)
        
    print("RESPONSE:",result)
    print("CONTENT:",content)