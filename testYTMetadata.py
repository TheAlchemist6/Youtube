import subprocess
import json
from pprint import pprint 
import time

# Plan
"""
Take a list of youtube videos

Get thier JSON Data
Get the title form JSON
Write JSON data to file
Get Transcript
Write to file

"""

result = subprocess.run("""
yt-dlp --skip-download --write-info-json https://www.youtube.com/watch?v=CN_BDrVjWvU -o "youtube-scraping"
""", shell=True, stdout=subprocess.PIPE)

print("Got the transcript, saving it")
time.sleep(2)
with open('youtube-scraping.info.json') as f:
    data = json.load(f)

pprint(data)
