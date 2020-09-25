"""处理FileNotFound异常"""
filenames=['cats.txt','dogs.txt']
for filename in filenames:
    try:
        with open(filename) as file_object:
           lines=file_object.readlines()
           
    except FileNotFoundError:
        pass
    
    else:
        print(filename+": ")
        for line in lines:
            print("\t"+line.title())

        

