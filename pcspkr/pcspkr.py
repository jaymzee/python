#!/usr/bin/env python
"""Beep PC Speaker using Linux evdev API.
To make /dev/input/by-path/platform-pcspkr-event-spkr device available, run:
    root# modprobe pcspkr
"""
import ctypes
import math
import os
import time


EV_SND = 0x12  # linux/input-event-codes.h
SND_TONE = 0x2  # ditto
time_t = suseconds_t = ctypes.c_long

class Timeval(ctypes.Structure):
    _fields_ = [('tv_sec', time_t),       # seconds
                ('tv_usec', suseconds_t)] # microseconds

class InputEvent(ctypes.Structure):
    _fields_ = [('time', Timeval),
                ('type', ctypes.c_uint16),
                ('code', ctypes.c_uint16),
                ('value', ctypes.c_int32)]


frequency = 18000 # Hz, A440 in ISO 16
device = "/dev/input/by-path/platform-pcspkr-event-spkr"
pcspkr_fd = os.open(device, os.O_WRONLY)  # root! + modprobe pcspkr
fsec, sec = math.modf(time.time())  # current time
ev = InputEvent(time=Timeval(tv_sec=int(sec), tv_usec=int(fsec * 1000000)),
                type=EV_SND,
                code=SND_TONE,
                value=frequency)

ev.value = 18000 # Hz, A440 in ISO 16
os.write(pcspkr_fd, ev)  # start beep
time.sleep(3)  # 200 milliseconds

ev.value = 16000
os.write(pcspkr_fd, ev)  # start beep
time.sleep(3)  # 200 milliseconds

ev.value = 14000
os.write(pcspkr_fd, ev)  # start beep
time.sleep(3)  # 200 milliseconds

ev.value = 12000
os.write(pcspkr_fd, ev)  # start beep
time.sleep(3)  # 200 milliseconds

ev.value = 10000
os.write(pcspkr_fd, ev)  # start beep
time.sleep(3)  # 200 milliseconds

ev.value = 8000
os.write(pcspkr_fd, ev)  # start beep
time.sleep(3)  # 200 milliseconds

ev.value = 6000
os.write(pcspkr_fd, ev)  # start beep
time.sleep(3)  # 200 milliseconds

ev.value = 0  # stop
os.write(pcspkr_fd, ev)

