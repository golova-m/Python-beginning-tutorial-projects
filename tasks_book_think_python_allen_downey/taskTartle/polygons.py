import math
import turtle
import tracery

def draw_isosceles(t, r, angle):
    y = r * math.sin(angle * math.pi / 180)

    t.right(angle)
    t.forward(r)
    t.left(90+angle)
    t.forward(2*y)
    t.left(90+angle)
    t.forward(r)
    t.left(180-angle)


def draw_triangles(t, num_triangle, r):
    angle = 360.0 / num_triangle
    for i in range(num_triangle):
        draw_isosceles(t, r, angle/2)
        t.left(angle)


def draw_polygon(t, num_triangle, r):
    draw_triangles(t, num_triangle, r)
    t.up()
    t.forward(r*2 + 10)
    t.down()


def main():
    bob = turtle.Turtle()
    bob.up()
    bob.backward(250)
    bob.down()

    size = 70
    draw_polygon(bob, 4, size)
    draw_polygon(bob, 5, size)
    draw_polygon(bob, 6, size)
    draw_polygon(bob, 7, size)

    turtle.mainloop()


if __name__ == '__main__':
    main()