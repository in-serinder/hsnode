from flask import Flask,template_rendered
from flask_socketio import SocketIO,send

app=Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)