"""读取文件练习"""
file_path=r'text_files\learning_python.txt'
with open(file_path) as file_object:
    
    lines=file_object.readlines()

for line in lines:
    line=line.replace('Python','C')
    print(line.rstrip())