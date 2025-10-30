import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Colorful Spiral Pattern")
screen.bgcolor("black")
screen.setup(width=800, height=800)

# Create turtle
t = turtle.Turtle()
t.speed(0)  # Fastest speed
t.width(2)

# List of colors for the pattern
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan"]

# Draw a colorful spiral pattern
def draw_spiral():
    for i in range(360):
        t.pencolor(colors[i % len(colors)])
        t.forward(i * 0.5)
        t.left(59)

# Draw the spiral
draw_spiral()

# Hide turtle and keep window open
t.hideturtle()
screen.mainloop()
