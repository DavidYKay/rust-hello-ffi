# treble.py

import ctypes

libhelloffi = ctypes.CDLL("./libhelloffi.so")

libhelloffi.hello_rust()
