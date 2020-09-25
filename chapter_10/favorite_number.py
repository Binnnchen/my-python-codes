import json

def get_stored_number(filename):
    """获取已存储的数字"""
    try:
        with open(filename) as f_obj:
            number=json.load(f_obj)
    
    except FileNotFoundError:
        return None
    else:
        return number

def get_new_number(filename):
    #获取新数字
    number=input("What's your favorite number? ")

    with open(filename, 'w') as f_obj:
        json.dump(number,f_obj)

def get_favorite_number(filename):
    #问他人最喜欢的数字，并指出
    number=get_stored_number(filename)
    if number:
        print("I remember your favorite number is "+number+".")
    else:
        get_new_number(filename)

filename="favo_number.json"
get_favorite_number(filename)
    
    
    
    
    
    
    


    