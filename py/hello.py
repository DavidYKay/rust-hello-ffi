# treble.py

import ctypes
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
lib_path = "%s/%s" % (base_dir, "libhelloffi.so")
libhelloffi = ctypes.CDLL(lib_path)

print libhelloffi.square(9)
