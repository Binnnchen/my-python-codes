file_path=r'text_files\programming.txt'
with open(file_path,'a') as file_object:
    message='I love programming.\n'
    file_object.write(message)
    file_object.write("I also love find meaning in large datasets.\n")
    file_object.write("I love creating app that can run in a browser.\n")
