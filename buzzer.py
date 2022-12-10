# buzzer.py
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Author        Date            Version         Comment
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Yuyang Wu     Dec 9, 2022     1.0.0           Cell broadcasting service
#
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from machine import Pin, PWM
import time

tempo = 5
tones = {
    'c': 262,
    'd': 294,
    'e': 330,
    'f': 349,
    'g': 392,
    'a': 440,
    'b': 494,
    'C': 523,
    ' ': 0,
}
rhythm = [8, 8, 8, 8, 8, 8, 8, 8]


class Buzzer:
    def __init__(self):
        self._beeper = PWM(Pin(32, Pin.OUT), duty=512)
        self._beeper.deinit()

    def melody(self):
        melody = 'cdefgabC'
        self._beeper.init(freq=440)
        for tone, length in zip(melody, rhythm):
            self._beeper.freq(tones[tone])
            time.sleep(tempo/length)
        self._beeper.deinit()

    def CBS_frqu(self):
        for x in range(3):
            self._beeper.init(freq=960)
            for y in range(50):
                self._beeper.freq(853)
                time.sleep_ms(6)
                self._beeper.freq(960)
                time.sleep_ms(6)
            self._beeper.deinit()
            time.sleep(0.5)
