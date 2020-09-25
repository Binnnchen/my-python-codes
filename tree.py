import turtle as T
import random
import time

# 鐢绘ū鑺辩殑韬?骞?(60,t)
def Tree(branch, t):
    time.sleep(0.0005)
    if branch > 3:
        if 8 <= branch <= 12:
            if random.randint(0, 2) == 0:
                t.color('snow')  # 鐧?
            else:
                t.color('lightcoral')  # 娣＄強鐟氳壊
            t.pensize(branch / 3)
        elif branch < 8:
            if random.randint(0, 1) == 0:
                t.color('snow')
            else:
                t.color('lightcoral')  # 娣＄強鐟氳壊
            t.pensize(branch / 2)
        else:
            t.color('sienna')  # 璧?(zh臎)鑹?
            t.pensize(branch / 10)  # 6
        t.forward(branch)
        a = 1.5 * random.random()
        t.right(20 * a)
        b = 1.5 * random.random()
        Tree(branch - 10 * b, t)
        t.left(40 * a)
        Tree(branch - 10 * b, t)
        t.right(20 * a)
        t.up()
        t.backward(branch)
        t.down()

# 鎺夎惤鐨勮姳鐡?
def Petal(m, t):
    for i in range(m):
        a = 200 - 400 * random.random()
        b = 10 - 20 * random.random()
        t.up()
        t.forward(b)
        t.left(90)
        t.forward(a)
        t.down()
        t.color('lightcoral')  # 娣＄強鐟氳壊
        t.circle(1)
        t.up()
        t.backward(a)
        t.right(90)
        t.backward(b)

# 缁樺浘鍖哄煙
t = T.Turtle()
# 鐢诲竷澶у皬
w = T.Screen()
t.hideturtle()  # 闅愯棌鐢荤瑪
t.getscreen().tracer(5, 0)
w.screensize(bg='wheat')  # wheat灏忛害
t.left(90)
t.up()
t.backward(150)
t.down()
t.color('sienna')

# 鐢绘ū鑺辩殑韬?骞?
Tree(60, t)
# 鎺夎惤鐨勮姳鐡?
Petal(200, t)
w.exitonclick()

