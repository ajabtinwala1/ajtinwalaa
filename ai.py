from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create ChatBot instance
chatbot = ChatBot('AI Bot')

# Train chatbot with English corpus
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

# Chat with bot
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = chatbot.get_response(user_input)
    print("Bot:", response)
