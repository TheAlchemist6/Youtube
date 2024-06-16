from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
from youtube_transcript_api.formatters import JSONFormatter

transcript = YouTubeTranscriptApi.get_transcript("vRIA3a4Jc8U")
text_formatter = TextFormatter()
json_formatter = JSONFormatter()

transcript_text = text_formatter.format_transcript(transcript)
transcript_json = json_formatter.format_transcript(transcript)

print(transcript_text)
print(transcript_json)