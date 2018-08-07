from flask import Flask, request
from flask_restful import Resource, Api
#from sqlalchemy import create_engine
#from json import dumps
from flask.json import jsonify
from flask_cors import CORS
from flask import request
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from chatterbot.preprocessors import convert_to_ascii


#db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__)
CORS(app)
api = Api(app)

global train
train = True
global chatterbot
chatterbot=ChatBot(
        'Alpha',
        trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
    )
chatterbot.train("chatterbot.corpus.english")

def getresponse(text):
    global train
    print(type(text))
    response_text = chatterbot.get_response(text)
    print(type(response_text))
    return (response_text.text)

    #SendEmailSMTP.send_Email()

class MyChatbot(Resource):
    train=True
    def get(self):
        text = request.args.get('text')
        return {'response': getresponse(text)}


api.add_resource(MyChatbot, '/chat')  # Route_3

if __name__ == '__main__':
    app.run(port='5002')