import pylast
from discord_stat import discord_status
from discord_stat import clear_stat
import time


#put your last.fm api keys here
API_KEY = ""
API_SECRET = ""

#put your last.fm username here
username = "cangying1997"

network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET)
user = network.get_user(username)


def song_from_lastfm():



    current_track = user.get_now_playing()
    if current_track is not None:
        track = current_track

        print ("Your discord status is Now Playing: " + str(track))

        play_stat = "Now Playing: "
        discord_status(str(track), play_stat)

    else:
        print ("No songs detected. Idling for another 200s.")
        clear_stat()


if __name__ == "__main__":
    while True:
        song_from_lastfm()
        time.sleep(200)
