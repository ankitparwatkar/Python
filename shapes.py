import turtle
import random

def draw_flower(t, size, petals, color):
    t.color(color)
    for _ in range(petals):
        t.circle(size, 60)
        t.left(120)
        t.circle(size, 60)
        t.left(120)
        t.left(360 / petals)

def create_random_flower():
    size = random.randint(50, 100)
    petals = random.randint(5, 10)
    colors = ["red", "blue", "yellow", "green", "purple", "orange", "pink", "brown", "cyan", "magenta"]
    color = random.choice(colors)
    return size, petals, color

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  # Fastest drawing speed

    for _ in range(10):
        size, petals, color = create_random_flower()
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        t.penup()
        t.goto(x, y)
        t.pendown()
        draw_flower(t, size, petals, color)

    screen.mainloop()

if __name__ == "__main__":
    main()
