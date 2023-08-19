from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socket = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socket.on('message')
def handle(message):
    processed_string = processed_data(message)  # Implement your processing logic here
    send(processed_string, broadcast=True)

def processed_data(message):
    
    return "Uppercase of "+message+" is "+message.upper()

if __name__ == '__main__':
    socket.run(app, debug=True)