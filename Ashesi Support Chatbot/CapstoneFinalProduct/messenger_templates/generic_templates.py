import json
class MessengerTemplate():
	"""docstring for ClassName"
	"""
	def __init__(self):
	  self.arg = "template"

	def getStartedButtonTemplate(self, sender_id):
		temple = { "recipient": {"id": sender_id},
		    "message": {"attachment": {
		      "type": "template",
		      "payload": {
		        "template_type": "generic",
		        "elements": [{
		          "title": "Welcome!",
		          "image_url": "https://jumiademo.000webhostapp.com/ashesi.jpg",
		          "subtitle": "Ashesi University Bot",
		          "default_action": {
		            "type": "web_url",
		            "url": "https://www.ashesi.edu.gh",
		            "webview_height_ratio": "tall"
		          },
		          "buttons": [{
		            "type": "web_url",
		            "url": "www.ashesi.edu.gh",
		            "title": "View Website"
		          }, {
		            "type": "postback",
		            "title": "Start Chatting",
		            "payload": "START_CHATTING_PAYLOAD"
		          }]
		        }]
		      }
		    }
		}}
		return json.dumps(temple)

	def startChattingButtonTemplate(self, sender_id):
		temple = { "recipient": {"id": sender_id},
		    "message": {"attachment": {
		      "type": "template",
		      "payload": {
		        "template_type": "generic",
		        "elements": [{
		          "title": "Welcome!",
		          "image_url": "https://www.ashesi.edu.gh/images/logo-mobile_colored.png",
		          "subtitle": "Ashesi University",
		          "default_action": {
		            "type": "web_url",
		            "url": "https://www.ashesi.edu.gh",
		            "webview_height_ratio": "tall"
		          },
		          "buttons": [{
		            "type": "web_url",
		            "url": "www.ashesi.edu.gh",
		            "title": "View Website"
		          }, {
		            "type": "postback",
		            "title": "Start Chatting",
		            "payload": "START_CHATTING_PAYLOAD"
		          }]
		        }]
		      }
		    }
		}}
		return json.dumps(temple)