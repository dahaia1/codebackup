from tkinter import *
import random
root = Tk()
root.geometry("300x200")
root.title('猜数字游戏')

guess= IntVar()
answer = IntVar()
ms = StringVar()
e = IntVar()

answer = random.randint(0,100)

def clear(event):
    entry.delete(0,'end')
    ms.set('')

def judge():
    guess = int(e.get())
    if 0<=guess<=100:
        if guess == answer:
            ms.set('恭喜你猜对了! ')
        elif guess > answer:
            ms.set('你猜大了, 再试一次吧! ')
        else:
            ms.set('你猜小了, 再试一次吧！')
    else:
        ms.set('请输入0-100之间的整数')

label_1 = Label(root,text='猜数字游戏',font=("隶书",20))
label_1.pack(pady=5)

label_2 =Label(root,text='请输入0-100之间的整数')
label_2.pack(pady=5)

entry = Entry(root,textvariable=e)
entry.delete(0)
entry.pack(pady=5)
entry.bind('<Button-1>',clear)

button=Button(root,text='猜一猜',command=judge)
button.pack(pady=5)

message = Message(root,textvariable=ms,width=200)
message.pack(pady=5)

mainloop()
























