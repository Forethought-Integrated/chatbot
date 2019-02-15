from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
from tf_idf import *
import time
# https://flask-socketio.readthedocs.io/en/latest/
# https://github.com/socketio/socket.io-client

app = Flask(__name__)
bot_reply = {'bot_name': 'Mr. Stud', 'message': '', 'user_name': ''}
app.config[ 'SECRET_KEY' ] = 'jsbcfsbfjefebw237u3gdbdc'
socketio = SocketIO( app )

@app.route( '/' )
def hello():
  return render_template( 'index.html' )

def messageRecived():
  print( 'message was received!!!' )

@socketio.on( 'my event' )
def handle_my_custom_event( json ):
    socketio.emit('my response', json,callback=messageRecived)
    #time.sleep(20)
    print( 'recived my event: ' + str( json ) )
    #currentSocketId = request.namespace.socket.sessid()
    reply = previous_chats(json['message'])
    bot_reply['user_name'] = json['user_name']
    bot_reply['message'] = reply
    print(bot_reply)
    #reply = bytes(reply,"utf8")
    socketio.emit( 'my response', bot_reply, callback=messageRecived )

if __name__ == '__main__':
  socketio.run( app, debug = True )
