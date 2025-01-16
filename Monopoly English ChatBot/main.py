from chat import ChatBot
print('Welcome to the Monopoly Manual ChatBot')
print('Press q to exit')
while True:
     user_input = input('What is on your mind ?: ')
     if user_input == 'q':
          break
     chatbot = ChatBot(user_input=user_input)
     response = chatbot.response
     print(response)