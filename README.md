# slackbot-meme
Easily create memes in Slack with slash commands.

## Setup

1. Navigate to your Slack Integrations page.
2. Create a new Slackbot. Take note of your Slackbot's token. 
3. Create a new Slash command, `/meme`. Configure the command to send a `GET` request to `http://slackbot-meme.herokuapp.com/?slackbot=yourslackbotstoken`, replacing `yourslackbotstoken` with the token of the Slackbot you just created.
4. [View the available template names](http://memegen.link/templates/).
5. Type `/meme template; top; bottom;` into a public or private channel. Slackbots don't work in direct messages. Replace `template` with the name of the template you want to use, and replace `top` and `bottom` with the top and bottom text to display on the meme, respectively. Example: `/meme success; we have; a meme bot;`
6. Communicate like never before.

<img src="http://i.imgur.com/BGkqKgC.png">

## Credits

This uses [memegen](https://github.com/jacebrowning/memegen). Thanks memegen!
