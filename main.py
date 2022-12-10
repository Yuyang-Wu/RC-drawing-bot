# mian.py
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Author        Date            Version         Comment
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Yuyang Wu     Dec 9, 2022     1.0.0           Drawing robot BLE remote + toggle SW local control done
#
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import turtle
import rc_core
import local_core
from machine import Pin

local_mode_pin = Pin(34, Pin.IN)  # when ESP32 not connected, GPIO34 stays 0V, so by default mode is BLE remote
mode_indicator = Pin(15, Pin.OUT, 0)

tu = turtle.Turtle()
rc_ctrl = rc_core.RC(tu, local_mode_pin)
local_ctrl = local_core.LocalCore(tu, mode_indicator)

prev_reading = 0
while True:
    new_reading = local_mode_pin.value()

    if new_reading:
        if new_reading != prev_reading:
            rc_ctrl.ble_irq_onoff(False)
            mode_indicator.on()
            print('Switch to local mode, BLE receiver off')
        local_ctrl.local_task_blocking()

    else:
        if new_reading != prev_reading:
            rc_ctrl.ble_irq_onoff(True)
            print('Switch to remote mode, BLE receiver back on')
            mode_indicator.off()
        rc_ctrl.rc_task()  # non-blocking task

    prev_reading = new_reading
