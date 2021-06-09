import datetime
from models import Message
import array
from flask import Flask, jsonify, request
from flask.json.tag import JSONTag
from flask.templating import render_template

app = Flask(__name__)
msgsIdCounter=0


# msgLambda = lambda msg: {'id': msg.id, 'text': msg.text, 'date': msg.date()}

arch = list()
msgs = list([Message(id=msgsIdCounter, text='Init', date=datetime.date(1990, 1, 1)),
Message(id=msgsIdCounter+1, text='Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti aut dolore asperiores consequuntur suscipit officia similique magni, corrupti, ab eaque incidunt consequatur vero fugit. Quidem aliquid unde porro ducimus cupiditate', date=datetime.date(1990, 1, 1))])

@app.route('/')
def index():
    return render_template('index.html', msgs=msgs, arch=arch)

# 
@app.route('/newMessage', methods=['POST'])
def msg_post():
    msgText = request.form.get("msg")
    newMsg = Message(msgsIdCounter,msgText, datetime.datetime.now())
    msgsIdCounter=msgsIdCounter+1
    msgs.append(newMsg)
    return render_template('index.html', msgs=msgs, arch=arch)

# Получение новых сообщений
@app.route('/gm')
def msg_get():
    resDict = {}
    for i in range(len(msgs)):
        resDict[i] = msgs[i].__repr__()
    arch.extend(msgs)
    msgs.clear()
    return resDict

# Проверка есть ли новые сообщения
# status 1 Есть новые сообщения, 0 - нет
@app.route('/check')
def msg_check():
    return {'status': 1} if len(msgs)>0 else {'status': 0}