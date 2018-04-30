import rpc
import time


print("Now displaying your status from last.fm on discord.")
client_id = '438732790410903552' #put your application's client ID here
rpc_obj = rpc.DiscordIpcClient.for_platform(client_id)
print("RPC connection successful.")

def discord_status(track, play_stat):
        activity = {
                "state": track,
                "details": play_stat,

            "assets": {
                "small_text": "Text for small_image",
                "small_image": "now_playing",
                "large_text": "Text for large_image",
                "large_image": "now_playing_big"
            }
        }
        rpc_obj.set_activity(activity)

def clear_stat():
        activity = {
            "assets": {
                "small_text": "Text for small_image",
                "small_image": "now_playing",
                "large_text": "Text for large_image",
                "large_image": "now_playing_big"
                }
        }
        rpc_obj.set_activity(activity)



if __name__ == "__main__":
    main()
