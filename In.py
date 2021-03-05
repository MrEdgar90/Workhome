import turtle
import time

posponer = 0.1

xd = turtle.Screen()
xd.title("Test")
xd.bgcolor("black")
xd.setup(width= 600, height=600)
xd.tracer(1)

cosa = turtle.Turtle()
cosa.speed(0)
cosa.shape("square")
cosa.color("white")
cosa.penup()
cosa.goto(0,0)
cosa.direction = "stop"


food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0,-60)
food.direction = "stop"

food2 = turtle.Turtle()
food2.speed(0)
food2.shape("square")
food2.color("red")
food2.penup()
food2.goto(0,60)
food2.direction = "stop"

board = turtle.Turtle()
board.color("red")
board.speed(1)
board.pensize(6)
board.forward(80) # draw base 
board.left(120)
board.forward(80) 
board.left(120)
board.forward(80)

def arriba():
    cosa.direction = "up"
def abajo():
    cosa.direction = "down"
def izquierda():
    cosa.direction = "left"
def derecha():
    cosa.direction = "right"
def stop1():
    cosa.direction = "stop1"

def mov():
    if cosa.direction == "up":
        y = cosa.ycor()
        cosa.sety(y + 30)
    if cosa.direction == "down":
        y = cosa.ycor()
        cosa.sety(y - 30)
    if cosa.direction == "left":
        x = cosa.xcor()
        cosa.setx(x - 30)
    if cosa.direction == "right":
        x = cosa.xcor()
        cosa.setx(x + 30)
    if cosa.direction == "stop1":
        x = cosa.xcor()
        y = cosa.ycor()

xd.listen()
xd.onkeypress(arriba, "w")
xd.onkeypress(abajo, "s")
xd.onkeypress(derecha, "d")
xd.onkeypress(izquierda, "a")
xd.onkeypress(stop1, "space")


while True:
    xd.update()

    mov()
    time.sleep(posponer)


