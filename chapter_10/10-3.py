file_path=r'text_files\guest.txt'
with open(file_path,'a') as file_object:
    name=input("Enter your name: ")
    name+="\t"
    file_object.write(name)