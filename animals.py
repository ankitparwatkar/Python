import turtle
import random

def draw_circle_animal(t, color):
    t.color(color)
    t.begin_fill()
    t.circle(50)
    t.end_fill()

def draw_square_animal(t, color):
    t.color(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(100)
        t.right(90)
    t.end_fill()

def draw_triangle_animal(t, color):
    t.color(color)
    t.begin_fill()
    for _ in range(3):
        t.forward(100)
        t.left(120)
    t.end_fill()

def draw_star_animal(t, color):
    t.color(color)
    t.begin_fill()
    for _ in range(5):
        t.forward(100)
        t.right(144)
    t.end_fill()

def draw_rectangle_animal(t, color):
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(150)
        t.right(90)
        t.forward(75)
        t.right(90)
    t.end_fill()

def draw_oval_animal(t, color):
    t.color(color)
    t.begin_fill()
    t.setheading(45)
    for _ in range(2):
        t.circle(50, 90)
        t.circle(50 // 2, 90)
    t.end_fill()

def draw_hexagon_animal(t, color):
    t.color(color)
    t.begin_fill()
    for _ in range(6):
        t.forward(100)
        t.right(60)
    t.end_fill()

def draw_pentagon_animal(t, color):
    t.color(color)
    t.begin_fill()
    for _ in range(5):
        t.forward(100)
        t.right(72)
    t.end_fill()

def draw_diamond_animal(t, color):
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(100)
        t.right(60)
        t.forward(100)
        t.right(120)
    t.end_fill()

def draw_parallelogram_animal(t, color):
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(120)
        t.left(60)
        t.forward(60)
        t.left(120)
    t.end_fill()

def create_random_position(t):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    t.penup()
    t.goto(x, y)
    t.pendown()

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  # Fastest drawing speed
    t.hideturtle()

    colors = ["red", "blue", "green", "purple", "orange", "pink", "brown", "cyan", "magenta", "yellow"]
    draw_functions = [
        draw_circle_animal, draw_square_animal, draw_triangle_animal, draw_star_animal,
        draw_rectangle_animal, draw_oval_animal, draw_hexagon_animal, draw_pentagon_animal,
        draw_diamond_animal, draw_parallelogram_animal
    ]

    for draw_function in draw_functions:
        create_random_position(t)
        color = random.choice(colors)
        draw_function(t, color)

    screen.mainloop()

if __name__ == "__main__":
    main()
