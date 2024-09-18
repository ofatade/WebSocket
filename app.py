from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO()

socketio.init_app(app, cors_allowed_origin='*') #set cors to allow all orgins with '*'

# Initialize a global variable to store messages
stored_message = []


@socketio.on('connect') #this wrapper is responsible for triggering the following function, base on the specified event
def handle_connect():
    print('Client Connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client Disconnected')

@socketio.on('message')
def handle_message(message): #When listening for message events, takes in a message as an argument
    global stored_message  # Access the global stored_message variable
    stored_message.append(message)  # Store the incoming message
    print(f"New message received: {message}")

    # Print all stored messages
    print("All messages stored so far:")
    for msg in stored_message:
        print(msg)


    socketio.emit('message', message) #.emit() method broadcasts a specified event, with an accompanying message


@app.route("/")
def home():
    return render_template('base.html')


if __name__ == '__main__':

    app.debug = True
    socketio.run(app)