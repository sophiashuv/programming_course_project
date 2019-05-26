import json

"""This is the example of taking user data and 
getting all connected with insulin and level of sugar.
While the next project stage we will use it to estimate 
new dose time,value and send a notification to user."""


def file_read(file_name):
    """
    (str)->(list(dict))
    Reads file given and converts it to python dictionaries list
    """
    f = open(file_name, encoding='utf-8')
    file = dict(json.load(f))
    return file


def file_parse(file):
    """
    (dict)->(dict)
    Takes dictionary of all user events and returns only insulin connected.
    """
    insulin_doses = {}
    for value in file.items():
        events = value[1]
        for event_data in events:
            if event_data['eventType'] == 'insulin':
                insulin_doses[event_data['eventId']] = (event_data['systemTime'], event_data['eventSubType'],
                                                        event_data['value'])
    return insulin_doses


def insulin_doses_inspect(insulin_events):
    """
    (dict)->tuple(str,str,number)
    Returns date, type of insulin and value of medicine taken to this data in
    daily dose estimating.
    """
    for key, value in insulin_events.items():
            dose_time = value[0]
            dose_type = value[1]
            dose_value = value[2]
    return dose_time, dose_type, dose_value
    

if __name__ == '__main__':
    ff = file_read('package.json')
    doses_data = file_parse(ff)
    output = insulin_doses_inspect(doses_data)
    print(doses_data)  



