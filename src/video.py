import json

from src.implemented import youtube


class Video:
    def __init__(self, video_id):
        try:
            self.video_id = video_id
            self._video = youtube.videos().list(part='snippet,statistics', id=video_id).execute()
            self.title = self._video['items'][0]['snippet']['title']
            self.url = self._video['items'][0]['snippet']['thumbnails']['default']['url']
            self.view_count = self._video['items'][0]['statistics']['viewCount']
            self.likes_count = self._video['items'][0]['statistics']['likeCount']
        except IndexError:
            self._video = None
            self.title = None
            self.url = None
            self.view_count = None
            self.likes_count = None

    def __str__(self):
        return self.title


class PLVideo(Video):

    def __init__(self, video_id, plv_id):
        super().__init__(video_id)
        self.__plv_id = plv_id

    def __str__(self):
        return self.title



