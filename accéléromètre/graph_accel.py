import  serial
import time 
import numpy as np                                              # import the numpy library and rename it np
from matplotlib import pyplot as plt                            # import from the matplotlib library the fonction pyplot and rename it plt
from mpl_toolkits.mplot3d import Axes3D

ser_port = None
ax = None
quiver = None
fig = None

def init_uart():
    global ser_port
    ser_port  =  serial.Serial(port  =  "COM3" , baudrate = 9600 , timeout = 1 )
    if  (ser_port.isOpen()  ==  False):
        ser_port. open ()                                       # check and open Serial0

    ser_port.flushInput()                                       # clear the UART Input buffer
    ser_port.flushOutput()                                      # clear the UART output buffer   

def init_graph():
    global ax
    global quiver
    global fig

    fig = plt.figure()                                          # Creating an empty figure or plot
    ax = fig.add_subplot(111, projection='3d')
    #Set plot limits
    ax.set_xlim([-5000, 5000])
    ax.set_ylim([-5000, 5000])
    ax.set_zlim([-5000, 5000])

    #Labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    #Initialize the quiver plot
    quiver = ax.quiver(0, 0, 0, 0, 0, 0)
    
def read_uart():
    global ser_port                        
    bs = ser_port.readline().decode('utf-8').strip()
    print(repr(bs))

    return bs

def destroy():
    global ser_port
    ser_port.close ()                                          # Closes the serial port
    print ("test complete")

def parse_accel(txt):
    a = txt.split()

    x = int((a[0]))
    y = int((a[1]))
    z = int((a[2]))
    return (x , y , z)


def update_graph(x , y , z):
    """Update the quiver plot with new gravity vector data."""

    # Update the quiver plot with the new vector
    global quiver

    # Clear previous quiver
    quiver.remove()
    quiver = ax.quiver(0, 0, 0, x, y, z, color='r', length=10)


    plt.pause(0.5)
 

if __name__ == "__main__":
    init_uart()
    init_graph()

    while(1):
        try:
            texto = read_uart()
            (x , y , z) = parse_accel(texto)
            update_graph(x , y , z)
        except KeyboardInterrupt:                              # Watches for Ctrl-C
            destroy() 
            break    
        except:
            pass