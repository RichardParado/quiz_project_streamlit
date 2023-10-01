import requests


class Data:

    def __init__(self):
        self.url = "https://opentdb.com/api.php?amount=10&type=boolean"

    def get_data(self):
        data = requests.get(url=self.url).json()
        question_data = data["results"]
        return question_data


