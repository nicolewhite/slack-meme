# slackbot-meme
Easily post memes to Slack with slash commands.

## Setup

1. Navigate to your Slack Integrations page.
2. Create a new Slackbot. Take note of your Slackbot's token. 
3. Create a new Slash command, `/meme`. Configure the command to send a `GET` request to `http://slackbot-meme.herokuapp.com/?slackbot=yourslackbotstoken`, replacing `yourslackbotstoken` with the token of the Slackbot you just created.
4. [View the available template names](http://memegen.link/templates/).
5. Type `/meme template; top; bottom;` into any Slack channel. Replace `template` with the name of the template you want to use, and replace `top` and `bottom` with the top and bottom text to display on the meme, respectively. Example: `/meme success; we have; a meme bot;`
6. Communicate like never before.

<img src="http://i.imgur.com/BGkqKgC.png">

## Why This Meme Integration Is Better Than Other Meme Integrations

I've seen a few other community-built Slack integrations for memes, but they all require you to set up accounts on meme-generating websites and they also all use Incoming Webhooks, which you need to set up for each channel. Yikes. This integration uses Slackbots, allowing you to post memes to any channel out of the box.

## Credits

This uses [memegen](https://github.com/jacebrowning/memegen). Thanks memegen!
