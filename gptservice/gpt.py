from revChatGPT.V1 import Chatbot

chatbot = Chatbot(config={
    "email": "nurlannurlanov612@gmail.com",
    "password": "magzhan2005"
})


def start_chat(prompt):
    response = ""
    for data in chatbot.ask(
            prompt
    ):
        response = data["message"]

    return response
