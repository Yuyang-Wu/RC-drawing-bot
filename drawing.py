# drawing.py
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Author        Date            Version         Comment
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Yuyang Wu     Dec 9, 2022     1.0.0           Draw lmao and square
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# All draw functions be stored here

import math

stan_width = 20


def lmao(tu):  # Use turtle to draw a "LMAO"
    def cross_gap():
        tu.penup()
        tu.forward(stan_width)
        tu.pendown()

    # Draw L
    tu.penup()
    tu.left()
    tu.forward(4*stan_width)
    tu.right(180)
    tu.pendown()
    tu.forward(4*stan_width)
    tu.left()
    tu.forward(3*stan_width)
    tu.penup()
    # Draw M
    cross_gap()
    mMajor = math.degrees(math.atan(4 / 1))
    IIII = math.sqrt((stan_width*1)**2+(stan_width*4)**2)
    tu.left(mMajor)
    tu.forward(IIII)
    tu.right(mMajor*2)
    tu.forward(IIII)
    tu.left(mMajor*2)
    tu.forward(IIII)
    tu.right(mMajor*2)
    tu.forward(IIII)
    tu.left(mMajor)
    tu.penup()
    # Draw A
    cross_gap()
    aMajor = math.degrees(math.atan(4/1.5))
    II = math.sqrt((stan_width*1.5)**2+(stan_width*4)**2)
    tu.left(aMajor)
    tu.forward(II)
    tu.right(aMajor*2)
    tu.forward(II)
    tu.penup()
    tu.right(180)
    tu.forward(II/2)
    tu.left(aMajor)
    tu.pendown()
    tu.forward(1.5*stan_width)
    tu.penup()
    tu.right(180)
    tu.forward(1.5*stan_width)
    tu.right(aMajor)
    tu.forward(II/2)
    tu.left(aMajor)
    # Draw O
    cross_gap()
    tu.circle(stan_width*4)
    tu.penup()
    # Draw 口

    halfway_square(tu)
    tu.done()


def halfway_square(tu: Turtle):
    tu.penup()
    tu.left()
    tu.forward(4*stan_width)
    tu.right()
    tu.pendown()
    tu.forward(2*stan_width)
    for _ in range(3):
        tu.left()
        tu.forward(3*stan_width)
    tu.left()
    tu.forward(stan_width)
    tu.penup()


def line_turn(tu):
    for _ in range(4):
        tu.forward(100)
        tu.left()
        tu.right()
        tu.done()
