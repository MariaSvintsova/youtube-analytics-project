import os
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("YT_API_KEY")
youtube = build('youtube', 'v3', developerKey=api_key)

