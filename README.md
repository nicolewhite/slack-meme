# slackbot-meme
Post memes to any of your Slack channels with a slash command.

## Usage

`/meme success; we have; a meme bot;`

<img src="http://i.imgur.com/wWU8Odx.png">

View available templates with `/meme templates`:

<img src="http://i.imgur.com/ohkEr9P.png">

## Setup

* `SLACK_API_TOKEN`

[Go to the Slack Web API page](https://api.slack.com/web) and scroll down to **Authentication**. If you haven't already, generate a token. This is 
your `SLACK_API_TOKEN`.

* `SLACK_WEBHOOK_URL`

[Create a new Incoming Webhook](https://my.slack.com/services/new/incoming-webhook/). You can choose any channel; it doesn't matter. 
The channel will be overridden on each request with the channel from which the request originated. After creating, you'll see 
a **Webhook URL** field. This is your `SLACK_WEBHOOK_URL`.

* `SLACK_SLASH_COMMAND_TOKEN`

[Add a new Slash Command](https://my.slack.com/services/new/slash-commands). Call it `/meme`. After creating, you'll see a **Token** field. This is your `SLACK_SLASH_COMMAND_TOKEN`. Keep this page open, as you'll need to configure the Slash Command further after deploying your Heroku App.

* [![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

* Paste your `SLACK_API_TOKEN`, `SLACK_WEBHOOK_URL`, and `SLACK_SLASH_COMMAND_TOKEN` values into the appropriate config variables.

<img src="http://i.imgur.com/reNOSXe.png">

* Click **Deploy for Free**.

* Once finished, the **Name** field will now be populated if you didn't choose a name upfront.

* Go back to your Slash Command configuration page, which you left open. Enter your app's URL, which is `https://name-of-app.herokuapp.com`, into the **URL** field. Replace `name-of-app` with the name of your app. Configure it to send a `GET` request to this URL. For example, here is my configuration page:

<img src="http://i.imgur.com/mFtpKDX.png">

* Save the Slash Command integration.



## Credits

This uses [memegen](https://github.com/jacebrowning/memegen). Thanks memegen!
