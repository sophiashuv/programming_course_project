import json
import codecs
from json_reading_writing import*

class User:
    def __init__(self):
        self.user_name = str(input("ім'я"))

    def add_user(self, a_dict):
        with open("user.json", encoding='utf-8') as f:
            f.readline()
            lines = json.load(codecs.open("user.json", 'r', 'utf-8-sig'))

            lines.append(a_dict)
            return lines

    def file_name(self):
        """
        The function that returns a name of a file
        """
        if " " in self.user_name:
            self.user_name = self.user_name.replace(" ", "")
        return str(self.user_name).lower()+'.json'

    def create_json(self):
        """
        The function that creates new json
        """
        d = {"events": []}
        with open(self.file_name(), 'w') as outfile:
            json.dump(d, outfile)


if __name__ == "__main__":
    rewrite_json(User().add_insulin(), "user.json")
    User().create_json()


