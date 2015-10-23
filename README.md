# slack-meme
Post memes to any of your Slack channels with a slash command.

## Usage

### Built-in Templates

`/meme success; we have; a meme bot;`

<img src="http://i.imgur.com/SBLRFSo.png">

`/meme templates` shows you the available built-in templates:

<img src="http://i.imgur.com/JYigq3k.png">

### Custom Templates
Use your own image by passing its URL as the template:

`/meme http://nicolewhite.github.io/static/me.jpg; hello; my name is nicole;`

<img src="http://i.imgur.com/OVhBlmt.png">

### Preview

Hone your meme skills privately until you get it just right:

`/meme preview live; i'll write it; and we'll do it live;`

<img src="http://i.imgur.com/Vd1Rduw.png">

## Setup

### Slack API Token

[Go to the Slack Web API page](https://api.slack.com/web) and scroll down to **Authentication**. If you haven't already, generate a token. This is your `SLACK_API_TOKEN`.

### Incoming Webhook

[Create a new Incoming Webhook](https://my.slack.com/services/new/incoming-webhook/). You can choose any channel; it doesn't matter. 
The channel will be overridden on each request with the channel from which the request originated. After creating, you'll see 
a **Webhook URL** field. This is your `SLACK_WEBHOOK_URL`.

### Slash Command

[Create a new Slash Command](https://my.slack.com/services/new/slash-commands). Call it `/meme`. After creating, you'll see a **Token** field. This is your `SLACK_SLASH_COMMAND_TOKEN`. Keep this page open, as you'll need to configure the Slash Command further after deploying your Heroku App.

### Deploy to Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

Paste your `SLACK_API_TOKEN`, `SLACK_WEBHOOK_URL`, and `SLACK_SLASH_COMMAND_TOKEN` values into the appropriate config variables.

<img src="http://i.imgur.com/reNOSXe.png">

Click **Deploy for Free**. Once finished, the **Name** field will now be populated if you didn't choose a name upfront.

### Finish Slash Command Config

Go back to your Slash Command configuration page, which you left open. Enter your app's URL, which is `https://your-app-name.herokuapp.com`, into the **URL** field. Replace `your-app-name` with the name of your app. Configure it to send a `GET` request to this URL. For example, here is my configuration page:

<img src="http://i.imgur.com/mFtpKDX.png">

Save the Slash Command integration.

## Update Your Deployment

To update your deployment with changes from this repository, visit your app's homepage on Heroku and navigate to the section on deploying with Heroku git at https://dashboard.heroku.com/apps/your-app-name/deploy/heroku-git, replacing `your-app-name` with the name of your app. Follow the instructions there to get the Heroku toolbelt set up. Then:

```
$ heroku login
$ heroku git:clone -a your-app-name
$ cd your-app-name
```

Replace `your-app-name` with the name of your app. Once you have this set up, you can update your app with changes from this repository with the following:

```
$ git remote add slack-meme https://github.com/nicolewhite/slack-meme
$ git pull --rebase slack-meme master
$ git push heroku master
```

## Credits

This uses [memegen](https://github.com/jacebrowning/memegen). Thanks memegen!
