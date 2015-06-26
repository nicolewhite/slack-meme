# slackbot-meme
Post memes to any of your Slack channels with a slash command.

## Setup

1. `SLACK_API_TOKEN`

Go [here](https://api.slack.com/web) and scroll down to *Authentication*. If you haven't already, generate a token. This is 
your `SLACK_API_TOKEN`.

2. `SLACK_WEBHOOK_URL`

[Create a new Incoming Webhook](https://my.slack.com/services/new/incoming-webhook/). You can choose any channel; it doesn't matter. 
The channel will be overridden on each request with the channel from which the request originated. After creating, you'll see 
a *Webhook URL* field. This is your `SLACK_WEBHOOK_URL`.

3. `SLACK_SLASH_COMMAND_TOKEN`

[Add a new Slash Command](https://my.slack.com/services/new/slash-commands). Call it `/meme`. After creating, you'll see a *Token* 
field. This is your `SLACK_SLASH_COMMAND_TOKEN`. Keep this page open, as you'll need to configure the Slash Command further after 
deploying your Heroku App.

4. [![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

5. Paste your `SLACK_API_TOKEN`, `SLACK_WEBHOOK_URL`, and `SLACK_SLASH_COMMAND_TOKEN` values into the appropriate config variables.

<img src="http://i.imgur.com/reNOSXe.png">

6. Click *Deploy for Free*.

7. Once finished, the *Name* field will be populated if you didn't choose a name upfront.

8. Go back to your Slash Command configuration page, which you left open. Copy your app's URL into the URL field. Your app's URL
is https://<name>.herokuapp.com. Replace `<name>` with the name of your app. Configure it to send a `GET` request to this URL. For example, 
here is my configuration page:

<img src="http://i.imgur.com/mFtpKDX.png">

9. Save the Slash Command integration.

## Usage

`/meme success; we have; a meme bot;`

<img src="http://i.imgur.com/wWU8Odx.png">

## Credits

This uses [memegen](https://github.com/jacebrowning/memegen). Thanks memegen!
