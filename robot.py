import turtle

def draw_rectangle(t, width, height, color):
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

def draw_circle(t, radius, color):
    t.begin_fill()
    t.fillcolor(color)
    t.circle(radius)
    t.end_fill()

def draw_robot():
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(1)  # Adjust speed as needed

    # Draw body
    t.penup()
    t.goto(-50, -50)
    t.pendown()
    draw_rectangle(t, 100, 150, "gray")

    # Draw head
    t.penup()
    t.goto(-30, 100)
    t.pendown()
    draw_rectangle(t, 60, 60, "lightgray")

    # Draw eyes
    t.penup()
    t.goto(-20, 130)
    t.pendown()
    draw_circle(t, 10, "white")
    t.penup()
    t.goto(0, 130)
    t.pendown()
    draw_circle(t, 10, "white")

    # Draw mouth
    t.penup()
    t.goto(-20, 110)
    t.pendown()
    t.forward(40)

    # Draw left arm
    t.penup()
    t.goto(-50, 50)
    t.pendown()
    draw_rectangle(t, 20, 70, "gray")

    # Draw right arm
    t.penup()
    t.goto(50, 50)
    t.pendown()
    draw_rectangle(t, 20, 70, "gray")

    # Draw left leg
    t.penup()
    t.goto(-30, -200)
    t.pendown()
    draw_rectangle(t, 20, 100, "gray")

    # Draw right leg
    t.penup()
    t.goto(10, -200)
    t.pendown()
    draw_rectangle(t, 20, 100, "gray")

    screen.mainloop()

if __name__ == "__main__":
    draw_robot()
