import socket
import os
import time
import olfactometer as olf
import serial
import numpy as np

import config

COMM = config.arduino_COMM
BAUD = config.arduino_baud

## Get broadcast port
txtfile = open('con_out.txt', 'r')

while True:
    line = txtfile.readline()
    if "SOCKET BOUND ON PORT" in line:
        target_string = line
    else:
        pass
    try:
        target_string
        break
    except NameError:
         pass

txtfile.close()


list_of_elems = [elem for elem in target_string.split(" ")]
for elem in list_of_elems:
    u_elem = unicode(elem, 'utf-8')
    if u_elem.isnumeric():
        port_num  = int(elem)
        break
    else:
        pass

initial_time = time.time()

print('Port Number is: ', port_num)

HOST, PORT = '127.0.0.1', port_num

ser = olf.init_serial(COMM, BAUD)

tstart = time.time()
loop_cnt = 1
loop_av = 0
while 1:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    reply = sock.recv(128)
    line = reply.decode('UTF-8')

##  strip data vals
    toks = line.split()
    FrameNo = int(toks[0])
    PosY = float(toks[2])
    
    #PosY = int(PosY)
    #PosY = int(np.abs((PosY*60000)/255))
    print(PosY)

    stpt = olf.scale_signal(config.src_distance, PosY)
    olf.send_signal(ser, 0)

    tnow = time.time()
    loop_av += 0.001*((tnow-tstart)*1000-loop_av)

    #print( loop_cnt, FrameNo, PosY)

    loop_cnt += 1
    tstart = tnow

    time.sleep(.02)

