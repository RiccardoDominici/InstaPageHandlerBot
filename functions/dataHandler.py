import json


#load data from json file
def load_data():
    with open('data.json') as json_file:
        data = json.load(json_file)
    return data

#save data to json file
def save_data(data):
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)

#change data in json file
def change_data(data, key, value):
    data[key] = value
    save_data(data)