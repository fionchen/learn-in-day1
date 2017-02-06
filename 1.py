import turtle

def draw_square(t, size):
        for i in range(4):
                t.forward(size)
                t.left(90)
                
wn = turtle.Screen()
wn.bgcolor("lightgreen")

john = turtle.Turtle()
john.color("pink")
john.pensize(5)
for i in range(5):
        draw_square(john, 50)
        john.penup()
        john.forward(80)
        john.pendown()

wn.exitonclick()

