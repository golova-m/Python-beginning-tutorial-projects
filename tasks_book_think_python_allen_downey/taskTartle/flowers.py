import math

import turtle
from tracery import arc


def pain_petal(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        t.left(180-angle)


def pain_flower(t, num_petals, r, angle):
    for i in range(num_petals):
        pain_petal(t, r, angle)
        t.left(360.0/num_petals)

def moving(t, step):
    t.up()
    t.forward(step)
    t.down()


def main():
    bob = turtle.Turtle()
    moving(bob, -200)
    pain_flower(bob, 7, 100.0, 60.0)

    moving(bob, 200)
    pain_flower(bob, 10, 70.0, 80.0)

    moving(bob, 200)
    pain_flower(bob, 20, 260.0, 20.0)

    turtle.mainloop()


if __name__ == '__main__':
    main()