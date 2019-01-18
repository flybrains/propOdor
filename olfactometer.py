import serial
import time
import threading
import numpy as np
import struct

def init_serial(comm_port, baud_rate):
    return serial.Serial(comm_port, baud_rate)

def scale_signal(src_distance, y_val):
    if y_val >= src_distance:
        return 255
    else:
        return int((y_val/src_distance)*255)

def send_signal(ser, setpoint):
    ser.write(struct.pack('>B', setpoint))
    return None
