from flask import Flask, request
from models import Memegen, Memeifier, Slack, parse_text_into_params


app = Flask(__name__)


@app.route("/")
def meme():
    if not request.args:
        message = """
        Welcome to Slack Meme!
        Check me out on <a href="https://github.com/nicolewhite/slack-meme">GitHub</a>.
        """

        return message

    memegen = Memegen()
    memeifier = Memeifier()
    slack = Slack()

    token = request.args["token"]
    text = request.args["text"]
    channel_id = request.args["channel_id"]
    user_id = request.args["user_id"]

    if token != slack.SLASH_COMMAND_TOKEN:
        return "Unauthorized."

    if text.strip() == "":
        return memegen.error()

    if text[:9] == "templates":
        return memegen.list_templates()

    preview = True if text[:7] == "preview" else False
    text = text.replace("preview", "", 1) if preview else text

    template, top, bottom = parse_text_into_params(text)

    valid_templates = [x[0] for x in memegen.get_templates()]

    if template in valid_templates:
        meme_url = memegen.build_url(template, top, bottom)
    elif memeifier.image_exists(template):
        meme_url = memeifier.build_url(template, top, bottom)
    else:
        return memegen.error()

    if preview:
        return meme_url

    payload = {"channel": channel_id}
    user = slack.find_user_info(user_id)
    payload.update(user)

    attachments = [{"image_url": meme_url, "fallback": "Oops. Something went wrong."}]
    payload.update({"attachments": attachments})

    try:
        slack.post_meme_to_webhook(payload)
    except Exception as e:
        return e

    return "Success!", 200