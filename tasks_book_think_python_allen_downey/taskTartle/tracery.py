import math

import turtle


def square(t, lenght):
    for i in range(4):
        t.fd(lenght)
        t.lt(90)

def polygon(t, lenght, n):
    angle = 360.0 / n
    polyline(t, n, lenght, angle)


def circle(t, r):
    arc(t, r, 360)


def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_lenght = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_lenght, step_angle)


def polyline(t, n, lenght, angle):
    for i in range(n):
        t.fd(lenght)
        t.lt(angle)


def main():
    bob = turtle.Turtle()
    for i in range(4):
        square(bob, 100)
        #polygon(bob, 100, 5)
        circle(bob, 50)
        arc(bob, 100, 90)

    turtle.mainloop()


if __name__ == '__main__':
    main()