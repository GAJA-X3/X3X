import os, platform, time, sys
bit = platform.architecture()[0]
if bit == '64bit':
 os.system("mv _req.cpython-311.so /data/data/com.termux/files/usr/lib/python3.11/_req.cpython-311.so")
 import Xx
elif bit == '32bit':
 os.system("mv _req.cpython-311.so /data/data/com.termux/files/usr/lib/python3.11/_req.cpython-311.so")
 import Xx
