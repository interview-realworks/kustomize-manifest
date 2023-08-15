from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    message_file = '/etc/config/message.txt'
    if os.path.exists(message_file) and os.path.getsize(message_file) > 0:
        with open(message_file, 'r') as f:
            message = f.read()
    else:
        message = 'Hello interviewers. Please update the message.txt file with your configuration.'
    return message

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
