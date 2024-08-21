import turtle as t


def move_forward():
    tinny.forward(10)


def move_back():
    tinny.back(10)


def move_right():
    tinny.right(10)


def move_left():
    tinny.left(10)


def clear_screen():
    screen.reset()
    tinny.home()


tinny = t.Turtle()
screen = t.Screen()

screen.listen()
screen.onkeypress(key='w', fun=move_forward)
screen.onkeypress(key='s', fun=move_back)
screen.onkeypress(key='d', fun=move_right)
screen.onkeypress(key='a', fun=move_left)
screen.onkey(key='c', fun=clear_screen)

screen.exitonclick()
