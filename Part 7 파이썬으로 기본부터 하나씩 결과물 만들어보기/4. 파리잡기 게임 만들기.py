from tkinter import *
import tkinter
import tkinter.messagebox
from PIL import Image
from PIL import ImageTk
import random

next_move = None

def clicked():
    window.after_cancel(next_move)
    tkinter.messagebox.showinfo("미션 성공", "클릭성공!! 축하합니다.")
    window.quit()
    

def move_img():
    global next_move
    random_x = random.randint(50, 480)
    random_y = random.randint(50, 480)
    delay = random.randint(700,1000)
    b.place(x = random_x, y = random_y)
    next_move = window.after(delay, move_img)
    


window = Tk()
window.title("버튼 클릭 게임") # 창 제목
window.minsize(width=500, height=500)


width = 30
height = 30
img = Image.open("Part 7 파이썬으로 기본부터 하나씩 결과물 만들어보기\image\파리.png")
img = img.resize((width,height), Image.ANTIALIAS)
photoImg =  ImageTk.PhotoImage(img)
b = Button(window,image=photoImg , command=clicked)
b.place(x = 250, y =250)


move_img()

window.mainloop()












window.mainloop()