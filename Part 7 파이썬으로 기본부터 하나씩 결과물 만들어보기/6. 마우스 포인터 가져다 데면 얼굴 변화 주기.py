from tkinter import *

def chg_to_face1(event):
    img_label.config(image=face1)
    
def chg_to_face2(event):
    img_label.config(image=face2)
    

window = Tk()
window.title("마우스로 이미지 변경하기")
window.geometry("300x300")
window.config(bg="yellow")

face1 = PhotoImage(file = "Part 7 파이썬으로 기본부터 하나씩 결과물 만들어보기/image/face1.png")
face2 = PhotoImage(file = "Part 7 파이썬으로 기본부터 하나씩 결과물 만들어보기/image/face2.png")

img_label = Label(window, image=face1, bg="yellow")
img_label.pack(pady=70)

img_label.bind("<Enter>",chg_to_face2)
img_label.bind("<Leave>",chg_to_face1)

window.mainloop()