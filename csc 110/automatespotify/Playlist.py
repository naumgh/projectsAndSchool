import json
import requests
from secrets import spotify_user_id


class Playlist:

	def __init__(self):
		pass
	
	def get_youtube_client(self):
		pass

	def get_liked_videos(self):
		pass

	def create_playlis(self):
		
		request_body = json.dumps({
			"name":"liked_youtube_videos",
			"description":"all liked youtube videos"
			"public":True


		})

		query = "https://api.spotify.com/v1/users/{user_id}/playlists".format(self.user_id)
		response = requsets.post{
			query,
			data=request_body,
			headers = {
				"Content-Type":"application/json",
				"Authorization":"Bearer {}".format(spotify_token)
			}
		}

		response_json = respones.json()

		return response_json("id")
	

	def get_spotify_url(self, song_name, artist):
		
		query = "".format(spotify_token)

	def add_song_to_playlist(self):
		pass


