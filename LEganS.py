import turtle
import sys

def LEganS_build(width=480, height=480):
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.setheading(180)
    t.penup()
    t.backwards(200)
    t.left(90)
    t.forward(200)
    t.right(90)
    t.pendown()

    t.getscreen()._root.mainloop()

def main():
    pass

if __name__ == "__main__": main()
