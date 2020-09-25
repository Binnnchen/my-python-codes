'''
def calc(*numbers):
    sum=0
    for x in numbers:
        sum+=x**2
    return sum
print (calc())
'''
'''
def person(name,age,**kw):
    print('name:',name,'age:',age,'others:',kw)
person('Jack',16)
person('Bob',34,city='Beijing')
'''
'''
def product(*numbers):
    sum=1
    for x in numbers:
        sum*=x
    return sum
print(product())
print(product(4))
print(product(7,2,5))
'''
'''
def person(name,age=19,*,sex='M',city):
    print('name:',name,"age:",age,"sex:",sex,"city:",city)
person('Jackson',sex='F',city='Shanghai')
'''
'''
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(1))
print(fact(5))
print(fact(1000))
'''
#尾递归，但Python解释器没做尾递归优化
'''
def fact(n):
    return fact_iter(n,1)
def fact_iter(num,sum):
    if num==1:
        return sum
    return fact_iter(num-1,num*sum)
print(fact(1))
print(fact(5))
print(fact(10))
'''
'''
L=list(range(10))
print(L)
x='runboo'
for i in range(len(x)):
    print(x[i])
c=0
while c<len(x):
    print(x[c])
    c+=1
'''
'''
#切片slice
def trim(s):
    while s!='' and s[0]==' ':
        s=s[1:]
    while s!='' and s[-1]==' ':
        s=s[:-1]
    return s
print(trim("                                      hello  you        guys   "))

'''
#迭代(Iteration)找最值
'''
def findMinAndMax(L):
    if L==[]:
        return (None,None)
    min=L[0]
    max=L[0]
    for x in L:
        if x<min:
            min=x
        if x>max:
            max=x
    return(min,max)
print(findMinAndMax([]))
print(findMinAndMax([7]))
print(findMinAndMax([7,1]))
print(findMinAndMax([7,2,4,5,1,0]))
'''
#斐波拉切数列
'''def fib1(max):
    n,a,b=0,0,1
    while n<max:
        print(b)
        a,b=b,a+b
        n=n+1
    return 'done'
'''
def fib2(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
f=fib2(6)
next(f)
for x in f:
    print(x)


