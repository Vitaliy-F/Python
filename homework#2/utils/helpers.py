import json

def get_all_humans():
    f = open("homework#2\database\persons.json", "r")
    data = json.loads(f.read())
    f.close()
    return data

def write_new_human(human):
    data = get_all_humans()
    if len(data) < 1:
        human["id"] = 1
    else:
         human["id"] = len(data) + 1
    data.append(human)
    f = open("homework#2\database\persons.json", "w")
    data = json.dumps(data)
    f.write(data)
    f.close()
