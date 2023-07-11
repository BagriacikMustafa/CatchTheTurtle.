import turtle
from random import randint
import time

bg_turtle = turtle.Screen()
bg_turtle.bgcolor("light blue")
bg_turtle.title("DrawinTurtle")
# score
score_point = 0
score = turtle.Turtle()
score.color("black")
top_height = bg_turtle.window_height() / 2
y = top_height * 0.9
top_width = bg_turtle.window_width() / 2
x = top_width * 0.9
game_over = False


def score_setpos():
    score.hideturtle()
    score.penup()
    score.setpos(0, y)
    score.write(arg="Score : 0", move=False, align="center", font=("Arial", 25, "normal"))


# make turtle
skk = turtle.Turtle()


def make_turtle():
    # onlick turtle
    def handle_click(x, y):
        global score_point
        score_point += 1
        score.clear()
        score.write(arg="Score : {}".format(score_point), move=False, align="center", font=("Arial", 25, "normal"))

    skk.onclick(handle_click)
    skk.penup()
    skk.shape("turtle")
    skk.shapesize(3, 3)


# turtle position
def turtle_position():
    if not game_over:
        for i in range(50):
            skk.penup()
            skk.setpos(randint(-x, y), randint(-x, y))


timer_text = turtle.Turtle()


# countdown
def countdown(time):
    timer_text.hideturtle()
    timer_text.penup()
    timer_text.setpos(-x +20, y )
    global game_over
    if time > 0:
        timer_text.clear()
        timer_text.write(arg="{}".format(time), move=False, align="center", font=("arial", 25, "normal"))
        bg_turtle.ontimer(lambda: countdown(time - 1), 1000)
    else:
        game_over == True
        timer_text.clear()
        timer_text.write(arg="Game Over !", move=False, align="center", font=("arial", 25, "normal"))
        skk.hideturtle()



score_setpos()
countdown(20)
make_turtle()
turtle_position()

turtle.mainloop()
