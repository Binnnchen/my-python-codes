import json

def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename="username.json"
    try:
        with open(filename) as file_object:
            username=json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """提示输入用户名"""
    filename="username.json"
    username=input("What is your name? ")
    with open(filename,'w') as file_object:
            json.dump(username,file_object)
    print("We will remember you when you come back, "+username.title()+".")


def greet_user():
    """ 问候用户，并指出其名字"""
    username=get_stored_username()
    if username:
        singal=input("Are you "+username.title()+"?(y/n) ")
        if singal == 'y':
            print("Welcome back, "+username.title()+".")
        else:
            get_new_username()
    else:
        get_new_username()


greet_user()
