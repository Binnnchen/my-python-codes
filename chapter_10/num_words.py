"""得到Alice in Wonderful 的单词数"""
filename="alice.txt"
try:
    with open(filename) as f_obj:
        content=f_obj.read()
except FileNotFoundError:
    print("Sorry, the file "+filename+" does not exist.")
else:
    words=content.split()
    num_words=len(words)
    print("The file "+filename+" has about "+str(num_words)+" words.")
