import  serial
import time 
import numpy as np                      # import the numpy library and rename it np
from matplotlib import pyplot as plt    # import from the matplotlib library the fonction pyplot and rename it plt

ser_port = None

def init_uart():
    global ser_port
    ser_port  =  serial.Serial(port  =  "COM3" , baudrate = 9600 , timeout = 2 )
    if  (ser_port.isOpen()  ==  False):
        ser_port. open ()                                       # check and open Serial0

def init_graph():
    fig = plt.figure()                  # Creating an empty figure or plot
    
    ax = plt.axes(projection="3d")      # Defining the axes as a 3D axes so that we can plot 3D data into it. 

    
def read_uart():
    global ser_port
    ser_port.flushInput()                                       # clear the UART Input buffer
    ser_port.flushOutput()                                      # clear the UART output buffer                           
    bs = ser_port.readline().decode('utf-8').strip()
    print(repr(bs))

    return bs

def parse_accel(txt):
    a = txt.split()

    x = int((a[0]))
    y = int((a[1]))
    z = int((a[2]))


def update_graph():
    pass

if __name__ == "__main__":
    init_uart()
    init_graph()

    while(1):
        texto = read_uart()
        parse_accel(texto)
        update_graph()