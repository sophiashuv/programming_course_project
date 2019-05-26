import json


def rewrite_json(output_data, filename):
    """
    Tre function that rewrites json with user input
    """
    with open(filename, 'w', encoding='utf-8') as outfile:
        json.dump(output_data, outfile, ensure_ascii=False)
        outfile.close()


def file_read(file_name):
    """
    (str)->(list(dict))
    Reads file given and converts it to python dictionaries list
    """
    f = open(file_name, encoding='utf-8')
    file = dict(json.load(f))
    return file

