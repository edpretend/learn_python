"""问候函数库"""
import json


def get_stored_username():
    """old user"""
    filename = 'username.json'
    try: 
        with open(filename) as f_obj: 
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """new user"""
    username = input("Please input your name to creat it: ")
    filename = 'username.json'

    with open(filename, 'w') as file_object:
        json.dump(username,file_object)
    return username


def greet_user():
    """greet user"""
    username = get_stored_username()
    star = input("Do you have a username? Y/N ")

    while True:
        if star == 'Y' or star == 'y':
            username0 = input("Please input your username: ")
            if username != username0:
                print("You don't have permission to access!")
                username0 = get_new_username()
                print("We'll remember you when you come back, " + username0 + "!")
            elif username == username0:
                username0 = get_stored_username()
                print("Welcome back, " + username0 + "!")
            break
        elif (star == 'N') or (star == 'n'):
            username0 = get_new_username()
            print("We'll remember you when you come back, " + username0 + "!")
            break
        else:
            continue

