def count_word(filename):
    try:
        with open(filename) as f_obj:
            content=f_obj.read()
    except FileNotFoundError:
        file_path=r'text_files\missing_files.txt'
        with open(file_path,'a') as f_obj:
            f_obj.write(filename+"\n")
    else:
        words=content.split()
        num_words=len(words)
        print("The file "+filename+" has about "+str(num_words)+" words.")

filenames=['alice.txt','siddhartha.txt','moby_dick.txt','little_woman.txt']

for filename in filenames:
    count_word(filename)