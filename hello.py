'''print("hello,this is my first python")
a = -1
if a >= 0:
    print(a)
else:
    print(-a)
    print(not True)

m=ord("陈")
r=chr(m)
print(m)
print(r)
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
str="Hello, {0}. You save {1:.1f}%".format("Jackson",17.125)
print(str)'''

'''s1=72
s2=85
r=(s2-s1)/72
str="Hello, {0}. You promote {1:.3f}%".format("Jackson",r*100)
print(str)

friends=['Jack','Monkey','Okfina','PG']
print(friends)
friends.append('WangLi')
friends.insert(2,"Bob")
friends.pop(2)
print(friends)
'''

'''s=input("birth: ")
birth=int(s)
if birth<2000:
    print('00前')
else:
    print('00后')
height=input('Height: ')
weight=input('Weight: ')
height=float(height)
weight=float(weight)

bmi=weight/(height**2)
print("您的BMI指数为：%.3f" % bmi)
if bmi<18.5:
    print("过轻")
elif bmi<25:
    print("正常")
elif bmi<28:
    print("过重")
elif bmi<32:
    print("肥胖")
else:
    print("严重肥胖")'''

'''L=['Bart','Lisa','Adam']
for name in L:
    print("Hello, " ,name)
sum=0
for x in range(101):
    sum=sum+x
print(sum)

M=tuple(range(101))
print(M)
'''
'''
a=set(['mama',2,'iuiu'])

print(a)

dict={
    'Bob':45,
    'Jack':56,
    'Kobe':90
}
print(dict['Bob'])
print(dict.get('T',0))
dict.pop('Kobe')
print(dict)

L=[
    ['Apple','Google','Microsoft'],
    ['Java','Python','Ruby','PHP'],
    ['Adam','Bart','Lisa']
]
'''
'''
print(L[0][0])
print(L[1][1])
print(L[2][2])

tuple=(1,2,[3,4])
s=set(['BON',900,tuple])
print(s)
'''
'''
dict={'Monkey':90,'Lol':8,'mi':'op'}
print(dict)
dict['jml']=902
print(dict)

s=set('miii2')
print(s)
'''

'''n1=255
n2=1000
i=(n1,n2)
for x in i:
    print(str(x)+'的16进制为：'+hex(x))
'''
'''
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError("Bad Oprand Type--")
    if x>=0:
        return x
    else:
        return -x
print(my_abs('s'))
'''
'''import math

sqrt =math.sqrt

def quadratic(a, b, c):
    m=b**2-4*a*c
    if m<0:
        print("Sorry.No answer")
        return None
    elif a==0:
        x1=x2=-c/b
        return x1,x2
    else:
        x1=(-b+sqrt(m))/(2*a)
        x2=(-b-sqrt(m))/(2*a)
        return x1,x2

print('quadratic(2,3,1)=',quadratic(2,3,1))
print('quadratic(1,3,-4)=',quadratic(1,3,-4))
print(quadratic(0,5,4))
'''


#默认参数，尽量用不可变对象
def enroll(name,sex,gender=6,city='Chengdu'):
    print('name:',name)
    print('sex:', sex)
    print('gender:', gender)
    print('city:', city)

enroll('JIn','F')
enroll('Jin','F',9)










