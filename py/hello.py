# treble.py

import ctypes

libhelloffi = ctypes.CDLL("./libhelloffi.so")

print libhelloffi.square(9)
