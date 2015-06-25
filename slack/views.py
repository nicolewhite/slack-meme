from flask import Flask, request
import requests
from urllib import unquote

app = Flask(__name__)

@app.route("/")
def meme():
    domain = request.args["team_domain"]
    slackbot = request.args["slackbot"]
    text = request.args["text"]
    channel = request.args["channel_name"]

    text = text[:-1] if text[-1] == ";" else text
    params = text.split(";")
    params = [x.strip().replace(" ", "-") for x in params]
    params = [unquote(x) for x in params]

    if not len(params) == 3:
        response = "Your syntax should be in the form: /meme template; top; bottom;"
    else:
        template = params[0]
        top = params[1]
        bottom = params[2]

        response = "http://memegen.link/{0}/{1}/{2}.jpg".format(template, top, bottom)

    url = "https://{0}.slack.com/services/hooks/slackbot?token={1}&channel=%23{2}".format(domain, slackbot, channel)
    requests.post(url, data=response)