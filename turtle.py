import servo_driver
import math
import time
import steppers
from micropython import const

_ROLL_SPD = const(140)
_CHAIN_SPD = const(75)
_K_CW_CCW = const(2.1)


class Turtle:
    def __init__(self):
        print('turtle module ready to launch')
        # set up servo
        self._ser = servo_driver.Servo(33)
        self._ser.pen_up()
        # set up motor
        self._wheels = steppers.DualA4899(2,  # Left step
                                          16,  # Left direction
                                          4,  # Left enable pin
                                          26,  # Right step
                                          25,  # Right direction
                                          12,  # Right enable pin
                                          sleep=True,  # start in sleep mode
                                          sps=_CHAIN_SPD,  # steps-per-second
                                          smax=10240,  # max step count allowed
                                          smin=-10240  # min step count allowed
                                          )

        self._abs_pos = [0, 0]
        self._face = 0
        time.sleep_ms(50)

    def penup(self):
        self._ser.pen_up()
        time.sleep(0.5)

    def pendown(self):
        self._ser.pen_down()
        time.sleep(0.5)

    def test_ser(self):
        for i in range(0, 181, 10):
            self._ser.rotate_to(i)
            print(i)
            time.sleep(0.5)

    def forward(self, mm, chill=True, sleep=None, dire=1):
        self._wheels.step(dire * mm, _CHAIN_SPD if chill else _ROLL_SPD, sleep)
        time.sleep_ms(500)

    def right(self, ang=90, sleep=None):
        if ang != 0:
            self._wheels.step(ang * _K_CW_CCW, _CHAIN_SPD, sleep, turn=True)
            time.sleep_ms(500)

    def left(self, angle=90):
        self.right(-angle)

    # draw circle in 24 segments
    def circle(self, radius):
        step_angle = int(360 / 24)
        for _ in range(24):
            self.left(step_angle)
            self.forward(int((2 * math.pi * radius) / 24))
            time.sleep_ms(50)
        self.left(step_angle)
        time.sleep_ms(200)

    def done(self):
        self._wheels.sleep()
        self.penup()

    def beep_beep_sing(self):
        try:
            for _ in range(2):
                self._wheels.play(self._wheels.jingle, sleep=True)
                time.sleep_ms(500)
                self._wheels.play(self._wheels.jingle2, sleep=True)
                time.sleep(1)

                self._wheels.play(self._wheels.axelf, sleep=True)
                time.sleep(1)

                self._wheels.play(self._wheels.shave, sleep=True)
                time.sleep(1)

                print('  steps:', self._wheels.step(400, 800, sleep=True))
                time.sleep(1)

                print('  steps:', self._wheels.step(-400, 800, sleep=True))
                time.sleep(1)

                self._wheels.beepbeep(880, sleep=True)
                time.sleep(1)

        except Exception as e:
            import sys
            sys.print_exception(e)
            pass

    # experimental, haven't tested AT ALL
    def _goto(self, x, y):
        if x == 0 and y == 0:
            return -9
        distance = round(math.sqrt(x ^ 2 + y ^ 2))
        self._abs_pos[0] += x
        self._abs_pos[1] += y
        angle_from_x_axis = 0
        quadrant = 0
        if x == 0 or y == 0:
            if x < 0:
                angle_from_x_axis = 180
            elif x > 0:
                angle_from_x_axis = 0
            elif y < 0:
                angle_from_x_axis = 90
            elif y > 0:
                angle_from_x_axis = -90
        else:
            raw_angle = math.degrees(math.atan(y / x))
            if x > 0 and y > 0:
                quadrant = 1
                angle_from_x_axis = -raw_angle
            elif x < 0 and y > 0:
                quadrant = 2
                angle_from_x_axis = -(180 + raw_angle)
            elif x < 0 and y < 0:
                quadrant = 3
                angle_from_x_axis = 180 - raw_angle
            elif x > 0 and y < 0:
                quadrant = 4
                angle_from_x_axis = -raw_angle

        if angle_from_x_axis != self._face:
            rotate_deg = angle_from_x_axis - self._face
            if rotate_deg > 180:
                rotate_deg -= 360
            elif rotate_deg < -180:
                rotate_deg += 360

            if rotate_deg > 0:
                self.right(rotate_deg)
            elif rotate_deg < 0:
                self.left(-rotate_deg)
            time.sleep_ms(500)
            self._face += rotate_deg
