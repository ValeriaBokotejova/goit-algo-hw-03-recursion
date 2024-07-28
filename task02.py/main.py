import turtle

def koch_curve(t, order, length):
    # Function to draw one side of the Koch fractal
    if order == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_curve(t, order-1, length)
        t.left(60)
        koch_curve(t, order-1, length)
        t.right(120)
        koch_curve(t, order-1, length)
        t.left(60)
        koch_curve(t, order-1, length)

def draw_koch_snowflake(t, order, length):
    # Function to draw the Koch snowflake (three sides of the fractal)
    for _ in range(3):
        koch_curve(t, order, length)
        t.right(120)

def main():
    order = int(input("Enter the recursion level for the Koch snowflake: "))
    length = 300

    screen = turtle.Screen()  # Create the screen object
    screen.setup(800, 600)  # Set the window size
    screen.title("Koch Snowflake")
    screen.bgcolor("#c5d9ff")

    t = turtle.Turtle()  # Create a turtle object for drawing
    t.penup()
    t.goto(-length / 2, length / 3)
    t.pendown()

    t.speed(0)
    t.color("white")
    t.pensize(3)

    draw_koch_snowflake(t, order, length)  # Draw the Koch snowflake

    screen.mainloop()  # Keep the window open and responsive to user actions

if __name__ == "__main__":
    main()