from functools import wraps
from flask import Flask, request, redirect
from models import Memegen, Slack


app = Flask(__name__)


def ssl_required(fn):
    @wraps(fn)
    def decorated_view(*args, **kwargs):
        if not any([app.debug, request.is_secure, request.headers.get("X-Forwarded-Proto", "") == "https"]):
            return redirect(request.url.replace("http://", "https://"))
        else:
            return fn(*args, **kwargs)

    return decorated_view


@ssl_required
@app.route("/")
def meme():
    meme = Memegen()
    slack = Slack()

    token = request.args["token"]

    if token != slack.SLASH_COMMAND_TOKEN:
        return "Unauthorized."

    text = request.args["text"]

    if text[:9] == "templates":
        return meme.get_help()

    try:
        template, top, bottom = meme.parse_text_into_params(text)
    except:
        return "Your syntax should be in the form `/meme [template]; [top]; [bottom];. Type `/meme templates` to see valid templates."

    valid_templates = [x["name"] for x in meme.get_templates()]

    if template not in valid_templates:
        return "That template doesn't exist. Type `/meme templates` to see valid templates."

    meme_url = meme.build_url(template, top, bottom)
    channel_id = request.args["channel_id"]

    payload = {"text": meme_url, "channel": channel_id}

    user_id = request.args["user_id"]
    user = slack.find_user_info(user_id)

    payload.update(user)
    slack.post_meme_to_webhook(payload)

    return "Success!", 200