import json
import os
from urllib import unquote, quote
import requests


class Memegen:

    def __init__(self):
        self.BASE_URL = "http://memegen.link"

    def get_templates(self):
        response = requests.get(self.BASE_URL + "/templates").json()

        data = []

        for key, value in response.items():
            d = {}
            d["name"] = value.replace(self.BASE_URL + "/templates/", "")
            d["description"] = key
            data.append(d)

        return data

    def get_help(self):
        templates = self.get_templates()

        help = ""

        for template in templates:
            help += "*{0}*: {1}\n".format(template["name"], template["description"])

        return help

    def build_url(self, template, top, bottom):
        path = "/{0}/{1}/{2}.jpg".format(template, top or '_', bottom or '_')
        url = self.BASE_URL + path

        return url


class Slack:

    def __init__(self):
        self.BASE_URL = "https://slack.com/api"
        self.API_TOKEN = os.environ.get("SLACK_API_TOKEN")
        self.WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL")
        self.SLASH_COMMAND_TOKEN = os.environ.get("SLACK_SLASH_COMMAND_TOKEN")

    def find_user_info(self, user_id):
        url = self.BASE_URL + "/users.info?token={0}&user={1}".format(self.API_TOKEN, user_id)
        response = requests.get(url)

        user = response.json()["user"]
        username = user["name"]
        icon_url = user["profile"]["image_48"]

        return {"username": username, "icon_url": icon_url}

    def post_meme_to_webhook(self, payload):
        requests.post(self.WEBHOOK_URL, data=json.dumps(payload))


def parse_text_into_params(text):
    text = unquote(text)
    text = text[:-1] if text[-1] == ";" else text
    params = text.split(";")
    params = [x.strip().replace(" ", "-") for x in params]
    params = [quote(x) for x in params]

    params += [None] * (3 - len(params))
    return params[0], params[1], params[2]