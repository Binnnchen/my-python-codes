file_path=r'text_files\guest_book.txt'
with open(file_path,'a') as file_object:
    
    while True:
        guest=input("What's your name? ")
        if guest == 'f':
            break
        else:
            print("Hello, "+guest.title())
            file_object.write(guest+"\n")
        