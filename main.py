import sys
import requests
#sys.path.insert(0, '/Users/joao_/PycharmProjects/pythonProject4')
from whatsapp_chatbot_python.whatsapp_chatbot_python_teste.whatsapp_chatbot_python_test import GreenAPIBot, Notification

url = "https://7103.api.greenapi.com/waInstance7103935387/setSettings/9cf0e91c537c430ba344df997df81c42689e6934b50d4c119f"

payload = "{ \r\n\t\"delaySendMessagesMilliseconds\": 1000,\r\n\t\"markIncomingMessagesReaded\": \"no\",\r\n\t\"outgoingWebhook\": \"yes\",\r\n\t\"stateWebhook\": \"yes\",\r\n\t\"incomingWebhook\": \"yes\",\r\n\t\"deviceWebhook\": \"no\"\r\n}"
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text.encode('utf8'))

bot = GreenAPIBot(
    "71039357", "9cf0e91c537c430ba344df997df81c42689e6934b50d4c11"
)

@bot.router.message(text_message="message")
def message_handler(notification: Notification) -> None:
    notification.answer("Hello")


bot.run_forever()