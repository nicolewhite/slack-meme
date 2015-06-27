from flask import Flask, request
from models import Memegen, Memeifier, Slack, parse_text_into_params


app = Flask(__name__)


@app.route("/")
def meme():
    memegen = Memegen()
    memeifier = Memeifier()
    slack = Slack()

    token = request.args["token"]
    text = request.args["text"]
    channel_id = request.args["channel_id"]
    user_id = request.args["user_id"]

    if token != slack.SLASH_COMMAND_TOKEN:
        return "Unauthorized."

    if text[:9] == "templates":
        return memegen.get_help()

    template, top, bottom = parse_text_into_params(text)

    valid_templates = [x["name"] for x in memegen.get_templates()]

    if template in valid_templates:
        meme_url = memegen.build_url(template, top, bottom)
    elif memeifier.image_exists(template):
        meme_url = memeifier.build_url(template, top, bottom)
    else:
        return "That template doesn't exist. Type `/meme templates` to see valid templates or provide your own as a URL."

    payload = {"text": meme_url, "channel": channel_id}
    user = slack.find_user_info(user_id)
    payload.update(user)

    slack.post_meme_to_webhook(payload)

    return "Success!", 200