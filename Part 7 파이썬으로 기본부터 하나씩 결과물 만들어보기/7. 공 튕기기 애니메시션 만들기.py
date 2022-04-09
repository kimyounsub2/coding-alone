from tkinter import *
import random
import time

from matplotlib.pyplot import fill

window = Tk()
window.title("공 튕기기")

def move():
    try:
        global x_speed,y_speed
        ball_coor = canvas.coords(ball)

        # X1,Y2,X2,Y2의 순이다
        if ball_coor[0] <= 0 or ball_coor[2] >= WIDTH:
            x_speed = -x_speed
        if ball_coor[1] <= 0 or ball_coor[3] >= HEIGHT:
            y_speed = -y_speed
            
        canvas.move(ball, x_speed,y_speed )

    except TclError:
        pass
        
        
def move_1():
    try:
        global x_speed_1,y_speed_1
        ball_coor_1 = canvas.coords(ball_1)
        
        if ball_coor_1[0] <= 0 or ball_coor_1[2] >= WIDTH:
            x_speed_1 = -x_speed_1
        if ball_coor_1[1] <= 0 or ball_coor_1[3] >= HEIGHT:
            y_speed_1 = -y_speed_1
            
        canvas.move(ball_1, x_speed_1, y_speed_1)
    except TclError:
        pass
    
def move_2():
    try:
        global x_speed_2,y_speed_2
        ball_coor_2 = canvas.coords(ball_2)
        
        if ball_coor_2[0] <= 0 or ball_coor_2[2] >= WIDTH:
            x_speed_2 = -x_speed_2
        if ball_coor_2[1] <= 0 or ball_coor_2[3] >= HEIGHT:
            y_speed_2 = -y_speed_2
            
        canvas.move(ball_2, x_speed_2, y_speed_2)
    except TclError:
        pass
    
def move_3():
    try:
        global x_speed_3,y_speed_3
        ball_coor_3 = canvas.coords(ball_3)
        
        if ball_coor_3[0] <= 0 or ball_coor_3[2] >= WIDTH:
            x_speed_3 = -x_speed_3
        if ball_coor_3[1] <= 0 or ball_coor_3[3] >= HEIGHT:
            y_speed_3 = -y_speed_3
            
        canvas.move(ball_3, x_speed_3, y_speed_3)
    except TclError:
        pass
    
def boom():
    global x_speed,y_speed
    global x_speed_1,y_speed_1
    
    if ball == ball_1: 
        x_speed = -x_speed
        y_speed = -y_speed
        x_speed_1 = -x_speed_1
        y_speed_1 = -y_speed_1

WIDTH = 400
HEIGHT = 400
canvas = Canvas(window, width=WIDTH , height=HEIGHT, bg="lightblue" )
canvas.pack()

ball = canvas.create_oval(10,10,50,50, fill="pink") # X1,Y1,X2,Y2의 순이다
ball_1 = canvas.create_oval(350,350,390,390, fill="yellow")
ball_2 = canvas.create_oval(10,390,50,350, fill="red")
ball_3 = canvas.create_oval(390,10,350,50, fill="green")


x_speed = random.randint(3,20)
y_speed = random.randint(3,20)

x_speed_1 = random.randint(3,20)
y_speed_1 = random.randint(3,20)

x_speed_2 = random.randint(3,20)
y_speed_2 = random.randint(3,20)

x_speed_3 = random.randint(3,20)
y_speed_3 = random.randint(3,20)

while True:
    # move()
    # move_1()
    # move_2()
    # move_3()
    boom()
    window.update()
    time.sleep(0.1)
    

window.mainloop()