import turtle

def draw_i(t, size):
        for i in range(5):
                t.forward(size)
                t.left(144)
                
wn = turtle.Screen()
wn.bgcolor("lightgreen")

john = turtle.Turtle()
john.color("pink")
john.pensize(5)
for i in range(5):
        draw_i(john, 50)
        john.penup()
        john.forward(200)
        john.pendown()
        john.penup()
        john.left(144)
        john.forward(200)
        john.pendown()

wn.exitonclick()

