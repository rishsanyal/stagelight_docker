from mailjet_rest import Client
import os


SMTP_SERVER = "in-v3.mailjet.com" #"smtp.gmail.com"
USEREMAIL = "contactstagelite@gmail.com"
USERPASSWORD = "USFC!12345"
EMAILPORT = 587

class UserInteractions:
    def __init__(self):
        # TODO: Pick these from OS environment variables
        API_KEY = "466f87960616cd45aac376cf96323c43"
        API_SECRET = "fadc395b52966871a88f8f306c5a946b"

        self.mailjet = Client(auth=(API_KEY, API_SECRET))

    def notify_user_of_new_topics(self, user, today_topics):
        # TODO: Check user notification preference

        html_part = "<center><h1>Today's topics are!!</h1>"
        for topic in today_topics:
            html_part += "<h3>" + topic.title + "</h3>"
        html_part += "<a href=\"localhost:3000\"><button type=\"button\">Follow to website!</button></a>"
        html_part += "</center>"

        data = {
            'FromEmail': USEREMAIL,
            'FromName': 'Stagelite Team',
            'Subject': 'Today\'s new topics are finally here!',
            'Text-part': '',
            'Html-part': html_part,
            'Recipients': [{'Email':user.user_email}]
        }
        result = self.mailjet.send.create(data=data)
        print(result.status_code)
        print(result.json())
