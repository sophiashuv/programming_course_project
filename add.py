import json
import codecs
from json_reading_writing import*


def add_user(a_dict):
    """
    adds user to user.json
    """
    lines = (json.load(codecs.open("user.json", 'r', 'utf-8-sig')))["user_name"]
    lines.append(a_dict)
    rewrite_json(({"user_name": lines}), "user.json")


def file_name(login):
    """
    returns a file name
    """
    if " " in login:
        login = login.replace(" ", "")
    return str(login).lower() + '.json'


def creating_json(login):
    """
    creates empty json
    """
    d = {"events": []}
    with open(file_name(login), 'w') as outfile:
        json.dump(d, outfile)


def add_user_data(login, a_dict):
    """
    adds data to login.json
    """
    lines = (json.load(codecs.open(file_name(login), 'r', 'utf-8-sig')))["events"]
    lines.append(a_dict)
    rewrite_json(({"events": lines}), file_name(login))




