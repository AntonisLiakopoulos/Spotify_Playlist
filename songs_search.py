import spotipy
from spotipy.oauth2 import SpotifyOAuth
scope = "user-library-read"
import os
from dotenv import load_dotenv
load_dotenv("ids.env")

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
PLAYLIST_ID = os.getenv("PLAYLIST_ID")
USER_ID = os.getenv("USER_ID")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri="https://example.com",
    scope="playlist-modify-private" ))

class PlaylistManager:
    def __init__(self):

        self.uris_list = []

    def get_track_uri(self,songs):
        for song in songs:
            results = sp.search(q=song, type="track", limit=1)
            tracks = results["tracks"]["items"]
            uri= tracks[0]["uri"]
            self.uris_list.append(uri)
            #print(uri)

    def create_playlist(self):
        playlist_name = "Hot 100 of the 00s"
        playlist_description = "Created with Spotipy"
        playlist = sp.user_playlist_create(user=USER_ID, name=playlist_name, public=False, description=playlist_description)
        return playlist["id"]

    def add_to_playlist(self):
        sp.playlist_add_items(playlist_id=self.create_playlist(), items=self.uris_list)
        print("Songs added to playlist!")

