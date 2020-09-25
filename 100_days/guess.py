import random as ran

answer=ran.randint(1,100)
counter=0
while True:
    counter+=1
    number = int(input('请输入1-100之间的一个数：'))
    if number < answer:
        print("猜小了！")
    elif number > answer:
        print("猜大了！")
    else:
        print('恭喜你猜对了！')
        break
print("您一共猜了%d次" % counter)
if counter > 7:
    print("您的智商余额已不足！")