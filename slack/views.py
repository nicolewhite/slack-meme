from flask import Flask, request, render_template
import requests
from urllib import unquote, quote

app = Flask(__name__)

@app.route("/")
def meme():
    domain = request.args["team_domain"]
    slackbot = request.args["slackbot"]
    text = request.args["text"]
    channel = request.args["channel_id"]

    text = unquote(text)
    text = text[:-1] if text[-1] == ";" else text
    params = text.split(";")
    params = [x.strip().replace(" ", "-") for x in params]
    params = [quote(x) for x in params]

    if not len(params) == 3:
        response = "Your syntax should be in the form: /meme template; top; bottom;"
    else:
        template = params[0]
        top = params[1]
        bottom = params[2]

        response = "http://memegen.link/{0}/{1}/{2}.jpg".format(template, top, bottom)

    url = "https://{0}.slack.com/services/hooks/slackbot?token={1}&channel={2}".format(domain, slackbot, channel)
    requests.post(url, data=response)

    return "ok", 200

@app.route("/templates")
def templates():
    response = requests.get("http://memegen.link/templates").json()

    table = []

    for key, value in response.items():
        d = {}
        d["name"] = value.replace("http://memegen.link/templates/", "")
        d["description"] = key
        d["example"] = "/meme {0}; top text; bottom text;".format(d["name"])
        d["result"] = "http://memegen.link/{0}/top-text/bottom-text.jpg".format(d["name"])
        table.append(d)

    return render_template('templates.html', table=table)