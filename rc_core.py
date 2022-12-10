# re_core.py
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Author        Date            Version         Comment
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Yuyang Wu     Dec 9, 2022     1.0.0           RC+sending S/N back
#
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import time
import ble_simple_peripheral
from serialN import *
from drawing import lmao


class RC:
    def __init__(self, tu, local_mode_pin):
        self._ble_server = ble_simple_peripheral.BLEinit()
        self._ble_server.on_write(self._on_rx)
        self._task = 'i'
        self._moveCode = "idle"
        self._tu = tu
        self._local_mode_pin = local_mode_pin

    def _on_rx(self, v):
        self._task = v.decode('utf-8').strip()
        print("RX: ", v)
        print("task: ", self._task)

    def _move_instruction_receiver(self, v):
        self._moveCode = v.decode('utf-8').strip()
        print("instruction received: ", self._moveCode)

    def _rc_move(self):
        self._broadcasting('start RC')
        self._ble_server.on_write(self._move_instruction_receiver)
        self._tu.penup()
        while True:
            if self._local_mode_pin.value():
                self._broadcasting('eject RC')
                self._moveCode = 'idle'
                break

            elif self._moveCode == 'f':  # forward
                self._tu.forward(20)

            elif self._moveCode == 'r':  # turn right
                self._tu.right(15)

            elif self._moveCode == 'l':  # turn left
                self._tu.left(15)

            elif self._moveCode == 'b':  # back
                self._tu.forward(-20)

            elif self._moveCode == 'u':  # pen up
                self._tu.penup()
                self._broadcasting('pen up')
                self._moveCode = 'idle'

            elif self._moveCode == 'd':  # pen down
                self._tu.pendown()
                self._broadcasting('pen down')
                self._moveCode = 'idle'

            elif self._moveCode == 'q':  # exit rc mode
                self._tu.done()
                self._broadcasting('exit RC')
                self._moveCode = 'idle'
                break

    def _broadcasting(self, data):
        if self._ble_server.is_connected():
            data = str(data)
            print("TX: ", data)
            self._ble_server.send(data)
        time.sleep_ms(444)

    def ble_irq_onoff(self, enable: bool): self._ble_server.on_write(self._on_rx if enable else None)

    def rc_task(self):
        if self._task == 'i':  # idle
            pass

        elif self._task == 'd':  # draw
            self._ble_server.on_write(None)
            self._broadcasting('start draw')
            lmao(self._tu)
            self._broadcasting('done')
            self._ble_server.on_write(self._on_rx)
            self._task = 'i'

        elif self._task == 's':  # return S/N
            self._ble_server.on_write(None)
            self._broadcasting(readSN())
            self._ble_server.on_write(self._on_rx)
            self._task = 'i'

        elif self._task == 'r':  # RC
            self._rc_move()
            self._ble_server.on_write(self._on_rx)
            self._task = 'i'

        else:
            self._broadcasting("Invalid symbol")
            self._task = 'i'
