import json

import requests
from googleapiclient.discovery import build

from src.implemented import youtube


class Channel:
    """Класс для ютуб-канала"""
    __youtube_api = youtube
    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""

        self.__channel_id = channel_id
        self._channel = self.__youtube_api.channels().list(id=channel_id, part='snippet,statistics').execute()
        self.title = self._channel['items'][0]['snippet']['title']
        self.description = self._channel['items'][0]['snippet']['description']
        self.url = self._channel['items'][0]['snippet']['thumbnails']['default']['url']
        self.subscriber_count = int(self._channel['items'][0]['statistics']['subscriberCount'])
        self.video_count = int(self._channel['items'][0]['statistics']['videoCount'])
        self.view_count = int(self._channel['items'][0]['statistics']['viewCount'])

    def __add__(self, other):
        return self.subscriber_count + other.subscriber_count

    def __sub__(self, other):
        return self.subscriber_count - other.subscriber_count

    def __gt__(self, other):
        return self.subscriber_count > other.subscriber_count

    def __ge__(self, other):
        return self.subscriber_count >= other.subscriber_count
    def __lt__(self, other):
        return self.subscriber_count < other.subscriber_count

    def __le__(self, other):
        return self.subscriber_count <= other.subscriber_count

    def __eq__(self, other):
        return self.subscriber_count == other.subscriber_count

    @property
    def channel(self):
        return self.__channel_id

    def print_info(self):
        """Выводит в консоль информацию о канале в json формате."""


        channel = youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

    @property
    def youtube_api(self):
        return self.__youtube_api


    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с YouTube API."""

        return cls.youtube_api


    def to_json(self, filename):
        channel_data = {
            "channel_id":self.channel_id,
            "title": self.title,
            "description": self.description,
            "url": self.url,
            "subscriber_count": self.subscriber_count,
            "video_count": self.video_count,
            "view_count": self.view_count
        }

        with open(filename, "w") as json_file:
            json.dump(channel_data, json_file, indent=4)






"""Создается экземпляр класса, вызывается его метод, выводящий всю информацию."""
channel1 = Channel("UC-OVMPlMA3-YCIeg4z5z23A")
channel1.print_info()


