from songs_search import PlaylistManager
from billboard_scraping import get_songs

song_names = get_songs()

playlist_manager = PlaylistManager()
playlist_manager.get_track_uri(song_names)
playlist_manager.create_playlist()
playlist_manager.add_to_playlist()