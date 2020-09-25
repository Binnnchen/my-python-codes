file_path=r'text_files\all_reasons.txt'
with open(file_path,'a') as file_object:
    
    active=True
    while active:
        reason=input("Why you love programming? ")
        if reason == 'f':
            active=False
        else:
            print(reason)
            file_object.write(reason+"\n")
        