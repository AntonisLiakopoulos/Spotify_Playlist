from bs4 import BeautifulSoup
import requests

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

response = requests.get("https://www.billboard.com/charts/hot-100/2000-08-12/",headers=header)
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")


song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
print(song_names)