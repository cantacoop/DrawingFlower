import turtle

window = turtle.Screen();
window.bgcolor("red")

def draw_square(some_turtle, size):
    for i in range(1, 5):
        some_turtle.forward(size)
        some_turtle.right(90)

def draw_petal(some_turtle, size):
    for i in range(1, 5):
        some_turtle.forward(size)
        if i % 2 == 0:
            some_turtle.right(145)
        else:
            some_turtle.right(35)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    
    # Create the turtle Brad - Draws a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(6)

    # Define size
    size = 80

    # Draw square
    for i in range(1, 37):
        draw_square(brad, size)
        brad.right(10)
    brad.forward(size * 3)
    
    # Draw flower
    size = 60
    for i in range (1, 37):
        draw_petal(brad, size)
        brad.right(10)
    brad.right(90)
    brad.forward(size * 3)

    window.exitonclick()

draw_art()
