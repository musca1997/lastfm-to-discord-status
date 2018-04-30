# Last.fm to Discord Status

You can use it on your local pc to display your "now playing" from last.fm on your discord status.

RPC connection Based on [Snazzah's SublimeDiscordRP](https://github.com/Snazzah/SublimeDiscordRP)

![](https://cdn.discordapp.com/attachments/431482836118274059/440408884537065473/2018-04-30_2.48.16.png)

It displays the song you're playing on Last.fm:

![](https://cdn.discordapp.com/attachments/431482836118274059/440408919811031042/2018-04-30_2.48.11.png)

![](https://cdn.discordapp.com/attachments/431482836118274059/440411721144860672/2018-04-30_3.18.01.png)


## Requirements

- Python 3.6.1+
- pylast (can be directly installed using `pip3 install pylast`)


## How to Use

1. Get an API key and secret from Last.fm API.

2. Register an App on Discord API page, Get your client ID, and set the App's name as "Last.fm Scrobbler".

Edit Rich Presence Assets part.

![](https://cdn.discordapp.com/attachments/431482836118274059/440407681975451648/2018-04-30_3.02.36.png)

3. Open `last.py` file, add your Last.fm API key, API secret and your Last.fm username.

Open `discord_stat.py` file, add your Discord API client ID.

4. run `python3 last.py` .

![](https://cdn.discordapp.com/attachments/431482836118274059/440411698612928513/2018-04-30_3.18.21.png)

It won't clear the presence until you close it.


## TODO list

1. Automatically clear the "Last.fm Scrobbler" presence after music stops playing.

2. Make a GUI so more non-programmers can use it.

3. Being able to display the album cover image, not just simply a boring Last.fm logo.
