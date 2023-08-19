# from flask import Flask, render_template
# from flask_socketio import SocketIO, send

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'your_secret_key'
# socketio = SocketIO(app)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @socketio.on('message')
# def handle_message(message):
#     processed_data = process_message(message)  # Implement your processing logic here
#     send(processed_data, broadcast=True)

# def process_message(message):
#     # Implement your processing logic here
#     # For demonstration, let's just return the reversed message
#     return message[::-1]

# if __name__ == '__main__':
#     socketio.run(app, debug=True)






# from flask import Flask, render_template
# from flask_socketio import SocketIO, send
# from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer
# import secrets
# secret_key = secrets.token_hex(32)  # Generates a 32-byte random key in hexadecimal format
# # app.config['SECRET_KEY'] = secret_key



# app = Flask(__name__)
# app.config['SECRET_KEY'] = secret_key
# socketio = SocketIO(app)

# bot = ChatBot('MyBot')
# trainer = ChatterBotCorpusTrainer(bot)
# trainer.train('chatterbot.corpus.english')

# @app.route('/')
# def index():
#     return render_template('index.html')

# @socketio.on('message')
# def handle_message(message):
#     response = get_chatbot_response(message)
#     send(response, broadcast=True)

# def get_chatbot_response(user_input):
#     response = bot.get_response(user_input)
#     return str(response)

# if __name__ == '__main__':
#     socketio.run(app, debug=True)









# from flask import Flask, render_template, request, jsonify
# from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer

# app = Flask(__name__)

# # Create a chatbot instance
# chatbot = ChatBot('MyBot')

# # Set up the ChatterBotCorpusTrainer
# trainer = ChatterBotCorpusTrainer(chatbot)

# # Train the chatbot on English language data
# trainer.train('chatterbot.corpus.english')

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/get_response', methods=['POST'])
# def get_response():
#     user_message = request.json['message']
#     response = get_chatbot_response(user_message)
#     return jsonify({'response': response})

# def get_chatbot_response(user_message):
#     return chatbot.get_response(user_message).text

# if __name__ == '__main__':
#     app.run(debug=True)





from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, send
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import secrets

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(32)
socketio = SocketIO(app)

bot = ChatBot('MyBot', storage_adapter='chatterbot.storage.SQLStorageAdapter')
bot.train("chatterbot.corpus.english")

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(message):
    response = get_chatbot_response(message)
    send(response, broadcast=True)

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json['message']
    response = get_chatbot_response(user_input)
    return jsonify({'response': str(response)})

def get_chatbot_response(user_input):
    response = bot.get_response(user_input)
    return str(response)

if __name__ == '__main__':
    socketio.run(app, debug=True)

