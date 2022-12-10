# Load the machine module for GPIO and PWM
# Control servo motor with MicroPython
# Author: George Bantique, TechToTinker at September 15, 2020
# https://techtotinker.blogspot.com/2020/09/006-micropython-tutorial-how-to-control.html?m=1

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# servo_driver.py
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Author        Date            Version         Comment
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Yuyang Wu     Dec 9, 2022     1.0.0           basic servo function for manipulating pen
#
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from machine import Pin, PWM


class Servo:
    def __init__(self, pin):
        self.p = Pin(pin, Pin.OUT)
        self.pwmObj = PWM(self.p, freq=50)
        # Set the pulse every 20ms

    # Creates a function for mapping the 0 to 180 degrees
    # to 20 to 120 pwm duty values
    def __map(self, deg, in_min, in_max, out_min, out_max):
        return int((deg - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

    # Creates another function for turning
    # the servo according to input angle
    def rotate_to(self, angle):
        self.pwmObj.duty(self.__map(angle, 0, 180, 20, 120))
        # self.pwmObj.duty(angle)

    def pen_up(self):
        self.rotate_to(95)

    def pen_down(self):
        self.rotate_to(40)

    # To rotate the servo motor to 0 degrees
    # rotate(pwm, 0)

    # To rotate the servo motor to 90 degrees
    # rotate(pwm, 90)

    # To rotate the servo motor to 180 degrees
    # rotate(pwm, 180)

    # To rotate the servo from 0 to 180 degrees
    # by 10 degrees increment
    # for i in range(0, 181, 10):
    #     servo(pwm, i)
    #     time.sleep(0.5)

    # To rotate the servo from 180 to 0 degrees
    # by 10 degrees decrement
    # for i in range(180, -1, -10):
    #     servo(pwm, i)
    #     time.sleep(0.5)
