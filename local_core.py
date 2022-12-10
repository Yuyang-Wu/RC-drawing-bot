# local_core.py
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Author        Date            Version         Comment
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Yuyang Wu     Dec 9, 2022     1.0.0           force local tasking
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import machine
import time
import buzzer
from drawing import halfway_square


class LocalCore:
    def __init__(self, tu, led):
        self._TMR = machine.Timer(0)
        self._tu = tu
        self._buzz = buzzer.Buzzer()
        self._led = led

    def _BLE_desabled_warning(self, _):
        self._led.value(not self._led.value())

    def local_task_blocking(self):
        self._buzz.CBS_frqu()
        self._TMR.init(period=666, callback=self._BLE_desabled_warning)
        halfway_square(self._tu)  # blocking task 1/2
        self._tu.done()  # blocking task 2/2
        time.sleep(3)
        self._TMR.deinit()
        self._led.on()
