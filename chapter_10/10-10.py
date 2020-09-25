def count_words(filename,word):
    """计算特定单词在文件中出现的次数"""
    with open(filename) as f_obj:
        contents=f_obj.read()
    number_word=contents.lower().count(word)
    print("In "+filename+", '"+word+"' appears "+str(number_word))

filenames=['alice.txt','siddhartha.txt','little_woman.txt']
for filename in filenames:
    count_words(filename,'little')
