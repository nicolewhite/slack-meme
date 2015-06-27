import json
import os
from urllib import unquote_plus, quote
import requests


class Memegen:

    def __init__(self):
        self.BASE_URL = "http://memegen.link"

    def get_templates(self):
        response = requests.get(self.BASE_URL + "/templates").json()

        data = []

        for key, value in response.items():
            name = value.replace(self.BASE_URL + "/templates/", "")
            description = key
            data.append((name, description))

        data.sort(key=lambda tup: tup[0])
        return data

    def get_help(self):
        templates = self.get_templates()

        help = ""

        for template in templates:
            help += "`{0}` {1}\n".format(template[0], template[1])

        return help

    def build_url(self, template, top, bottom):
        path = "/{0}/{1}/{2}.jpg".format(template, top or '_', bottom or '_')
        url = self.BASE_URL + path

        return url


class Memeifier:

    def __init__(self):
        self.BASE_URL = "http://memeifier.com"

    def image_exists(self, path):
        r = requests.head(path)
        return r.status_code == requests.codes.ok

    def build_url(self, template, top, bottom):
        return self.BASE_URL + "/{0}/{1}/{2}".format(top or '_', bottom or '_', template)


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
    text = unquote_plus(text)
    text = text[:-1] if text[-1] == ";" else text

    params = text.split(";")

    template = params[0]
    del params[0]

    params = [x.strip() for x in params]
    params = [quote(x) for x in params]

    params += [None] * (2 - len(params))
    return template, params[0], params[1]