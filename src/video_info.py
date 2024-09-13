from youtube_transcript_api import YouTubeTranscriptApi 
from bs4 import BeautifulSoup
import requests
import re

class GetVideo:
    @staticmethod
    def Id(link):
        """Extracts the video ID from a YouTube video link."""
        if "youtube.com" in link:
            pattern = r'youtube\.com/watch\?v=([a-zA-Z0-9_-]+)'
            video_id = re.search(pattern, link).group(1)
            return video_id
        elif "youtu.be" in link:
            pattern = r"youtu\.be/([a-zA-Z0-9_-]+)"
            video_id = re.search(pattern, link).group(1)
            return video_id
        else:
            return None

    @staticmethod
    def title(link):
        """Gets the title of a YouTube video."""
        r = requests.get(link) 
        s = BeautifulSoup(r.text, "html.parser") 
        try:
            title = s.find("meta", itemprop="name")["content"]
            return title
        except TypeError:
            title = "⚠️ There seems to be an issue with the YouTube video link provided. Please check the link and try again."
            return title
        
    @staticmethod
    def transcript(link):
        """Gets the transcript of a YouTube video."""
        video_id = GetVideo.Id(link)
        try:
            transcript_dict = YouTubeTranscriptApi.get_transcript(video_id)
            final_transcript = " ".join(i["text"] for i in transcript_dict)
            return final_transcript
        except Exception as e:
            print(e)

    @staticmethod
    def transcript_time(summary, video_url):
        lines = summary.splitlines()
        formatted_lines = []
        
        for line in lines:
            if "(" in line and ")" in line:  # Detect lines with timestamps
                text, timestamp = line.rsplit("(", 1)
                timestamp = timestamp.rstrip(")**")  # Remove any unwanted characters
                try:
                    minutes, seconds = map(int, timestamp.split(":"))
                    time_in_seconds = minutes * 60 + seconds
                    timestamp_url = f"{video_url}&t={time_in_seconds}"
                    clickable_timestamp = f"[{timestamp}]({timestamp_url})"
                    formatted_line = f"{text}({clickable_timestamp})"
                except ValueError:
                    # If timestamp format is incorrect, leave the line as is
                    formatted_line = line
            else:
                formatted_line = line
            formatted_lines.append(formatted_line)
            # print(formatted_lines)
        
        return "\n".join(formatted_lines)
