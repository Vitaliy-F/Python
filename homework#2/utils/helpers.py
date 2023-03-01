import json
import re

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


def check_email(email):
    pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.match(pat, email):
        return True
    else:
        return False


def change_items(input_id):
    data = get_all_humans()
    for item in data:
        if item["id"] == int(input_id):
            item["first_name"] = input("Edit your first name: ")
            item["last_name"] = input("Edit your last name: ")
            email = input("Edit your email: ")
    file = open("homework#2\database\persons.json", "w")
    data = json.dumps(data)
    file.write(data)
    file.close()


def is_email_correct(e):
    data = get_all_humans()
    check_list = []
    for item in data:
        check_list.append(item["email"])
    result = check_email(e)
    if e in check_list:
        return result and False
    else:
        return result and True
