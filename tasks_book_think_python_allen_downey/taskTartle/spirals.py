import turtle


def draw_spiral_archimedian (t, n, length=3, a=0.01, b=0.0002):
    theta = 0.0
    for i in range(n):
        t.forward(length)
        dtheta = 1 / (a + b * theta)
        t.left(dtheta)
        theta += dtheta + (0.1 * i)


def main():
    bob = turtle.Turtle()
    draw_spiral_archimedian(bob, n=500)
    turtle.mainloop()


if __name__ == '__main__':
    main()