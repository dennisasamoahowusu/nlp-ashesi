from flask import Flask, request, jsonify
from rasa_nlu.model import Interpreter
import json
import requests
import sys 
import re
from random import choice
from time import sleep
sys.path.append('..')
from custom_actions.actions_gateway import ActionsService
from messenger_templates.generic_templates import MessengerTemplate



app = Flask(__name__)

FB_API_URL = 'https://graph.facebook.com/v2.6/me/messages'
VERIFY_TOKEN = 'o7FR521qSvjokE6rXkti44mzcXpD0zvErpn5BnxRuewz'# <paste your verify token here>
PAGE_ACCESS_TOKEN = 'EAAmMTKrLfLwBAAJZB0clJYItudnqp64HcubZCcRBFQOKHxOKD7MAxJFQyNnPzPZAyls5HPLdK8zrYqODZBCA13WDCsWNkWlxJHBWQ5yT9ZB0JRhjwWqXwtcrGIUZBzxQpN8c72syo1e4cL5PqNLJ1g5ZA6IgZAEkZAUBXsKzkDz4BnS2qrsklewRh'

def webhook_verify_token(req):
    """This function verifies the webhook token inorder to connect to facebook messenger"""
    if req.args.get("hub.verify_token") == VERIFY_TOKEN:
        return req.args.get("hub.challenge")
    else:
        return "incorrect"
#print(webhook_verify_token.__doc__)

def is_message(message_event):
    """This function verifies user message"""
    return ("message" in message_event and "text" in message_event["message"])
#print(is_message.__doc__)

def user_response(message_event):
    """This function checks if the message is a message from the user"""
    return ("postback" in message_event and "payload" in message_event["postback"])

#print(user_response.__doc__)


def response_to_user(sender_id, message_text):
    """This function sends response back to the user using facebook graph API """
    r = requests.post("https://graph.facebook.com/v2.6/me/messages",

        params={"access_token": PAGE_ACCESS_TOKEN},

        headers={"Content-Type": "application/json"},

        data=json.dumps({
        "recipient": {"id": sender_id},
        "message": {"text": message_text}
    }))
    if r.status_code != 200:
        print(r.status_code)
        print(r.text)
    print('send response', r)
#print(response_to_user.__doc__)

def template_message(sender_id, template):
    """Sending response back to the user using facebook graph API"""

    r = requests.post("https://graph.facebook.com/v2.6/me/messages",

        params={"access_token": PAGE_ACCESS_TOKEN},

        headers={"Content-Type": "application/json"},

        data=template)
    if r.status_code != 200:
        print(r.status_code)
        print(r.text)
    print('send response', r)
#print(template_message.__doc__)

def rasa_nlu_response(text):
    """This function finds the domain and intent of the message passed based on training data"""
    interpreter = Interpreter.load("models/current/nlu")
    for specialChar in text.split("\n"):
        newText = re.sub(r"[^a-zA-Z0-9]+", ' ', specialChar)
        newText = newText.lower()
    result = interpreter.parse(newText)
    return json.dumps(result)
#print(rasa_nlu_response.__doc__)    

@app.route("/webhook", methods=['GET', 'POST'])
def listen():
    """Flask uses webhook to listen to the events reactions"""
    if request.method == 'GET':
        return webhook_verify_token(request)

    if request.method == 'POST':
        payload = request.json
        
        event = payload['entry'][0]['messaging']
        print('printing fb event', event)

        for x in event: 
            if is_message(x):
                text = x['message']['text']
                sender_id = x['sender']['id']
                ## removing any special character
                for specialChar in text.split("\n"):
                    text = re.sub(r"[^a-zA-Z0-9]+", ' ', specialChar)
                    text = text.lower()
                nlu_response = json.loads(rasa_nlu_response(text))
                print("RASA NLU RESPONSE", nlu_response)
                intent = nlu_response['intent']['name']
                entities = nlu_response['entities']
                if len(entities) >0:
                    entity_name = entities[0]['entity']
                    print("entity name is here", entity_name)
                else:
                    entity_name = "no_value"

                actions_gateway = ActionsService()
                resp = actions_gateway.routeToIntent(intent, entity_name)
                #be_fun = ["Hold on, lemme check against my knowledge source", "Okay, lemme find that for you", "Wait a second, Will respond to you shortly"]
                ##Will review these later
                # skip_these_intents = ["greet", "affirmative", "negative"]
                # if(intent not in skip_these_intents):
                #     response_to_user(sender_id, choice(be_fun))
                #     sleep(1)
                response_to_user(sender_id, resp)

            elif user_response(x):
                payload = x['postback']['payload']
                sender_id = x['sender']['id']

                if(payload == "GET_STARTED_PAYLOAD"):
                    fb_template = MessengerTemplate()
                    get_started_template = fb_template.getStartedButtonTemplate(sender_id)
                    template_message(sender_id, get_started_template)

                elif(payload == "START_CHATTING_PAYLOAD"):
                    response_to_user(sender_id, "Hello, I am your personal assistant, trained to answer questions about Ashesi. Let's begin chatting")

                
            else:
                sender = x['sender']['id']
                response_to_user(sender, "Oops the requested information could not be found")
                

        return "ok", 200
        
#print(listen.__doc__) 

@app.route('/', methods=['POST', 'GET'])
def index_page():
    toSend = {"status": "Welcome to Ashesi"}
    return jsonify(** toSend)

@app.route('/verify')
def verify_nlu():
    interpreter = Interpreter.load("models/current/nlu")
    message = "Get me admission requirement"
    result = interpreter.parse(message)
    return jsonify(** result)

@app.route('/testserver')
def test_server():
    fb_template = MessengerTemplate()
    get_started_template = json.loads(fb_template.getStartedButtonTemplate("2644295615612095"))
    template_message("2644295615612095", get_started_template)
    return jsonify(get_started_template)

if __name__ == "__main__":
    app.run(debug = True)
