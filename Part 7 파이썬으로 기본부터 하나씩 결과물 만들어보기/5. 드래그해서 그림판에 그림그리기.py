from tkinter import *
from tkinter import font

window = Tk()
window.title("그림판")

x1 = y1 = x2 = y2 =0

# 마우스를 먼저 클릭한 좌표를 x1,y1 마지막 클릭을 땐 부분을 x2,y2로 지정한다
def clicked(event):
    global x1,y1
    x1,y1 = event.x,event.y
    
def released(event):
    global x2,y2
    x2,y2 = event.x, event.y
    canvas.create_line(x1,y1,x2,y2, width=3)

def relidf():# relief 사용 예제 참조 캔버스 테두리모양을 6가지로 비교하여 보여주는 예제이다.
    relidf_list = ["flat","groove","raised","ridge","solid","sunken"]
    for i in range(len(relidf_list)):
        Label(window, text =relidf_list[i], relief=relidf_list[i],font=("나눔바른펜","20","bold"),bd=5).pack()

label = Label(window, text = "캠버스 그림판",font=("나눔바른펜","30","bold"))
label.pack(pady=30) 


canvas = Canvas(window, width= 500 , height=500, bg="yellow", relief="ridge", bd=5)
canvas.pack()

canvas.bind("<Button>",clicked)
canvas.bind("<ButtonRelease>",released)

window.mainloop()