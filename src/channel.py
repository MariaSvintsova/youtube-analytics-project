import json

import requests
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    def print_info(self):
        """Выводит в консоль информацию о канале в json формате."""

        api_key = "AIzaSyCg8I_OJBrkfqsq_KihzECdLwGtRhbNMLU"
        youtube = build('youtube', 'v3', developerKey=api_key)

        channel_id = self.channel_id
        channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))


"""Создается экземпляр класса, вызывается его метод, выводящий всю информацию."""
channel1 = Channel("UC-OVMPlMA3-YCIeg4z5z23A")
channel1.print_info()




# Второй возможный вариант, но без вывода статистики
#     def print_info(self):
#         """Выводит в консоль информацию о канале."""
#         api_key = "AIzaSyCg8I_OJBrkfqsq_KihzECdLwGtRhbNMLU"
#         channel_id = self.channel_id
#         url = f"https://www.googleapis.com/youtube/v3/channels?part=snippet&id={channel_id}&key={api_key}"
#
#         response = requests.get(url)
#
#         data = response.json()
#
#
#         print(json.dumps(data, indent=2, ensure_ascii=False))
#
#
# channel1 = Channel("UC-OVMPlMA3-YCIeg4z5z23A")
# channel1.print_info()