import turtle

def draw_square(some_turtle):
    for i in range(4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_shape():
    window = turtle.Screen()
    window.bgcolor("#eca1a6")

    # create turtle Brad - draw a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(4)

    for i in range(36):
        draw_square(brad)
        brad.right(10)
    
##    # create turtle angie - draw a circle
##    angie = turtle.Turtle()
##    angie.shape("arrow")
##    angie.color('blue')
##    angie.speed(8 )
##    angie.circle(100)

    
    window.exitonclick()


draw_shape()
