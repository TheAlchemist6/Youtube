from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

transcript = YouTubeTranscriptApi.get_transcript("huCsvD1hog8")

formatter = TextFormatter()
json_formatted = formatter.format_transcript(transcript)

with open('your_filename.json', 'w', encoding='utf-8') as my_file:
    my_file.write(json_formatted)