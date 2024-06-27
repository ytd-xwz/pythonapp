import  serial
import time 
import numpy as np                      # import the numpy library and rename it np
from matplotlib import pyplot as plt    # import from the matplotlib library the fonction pyplot and rename it plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import random

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

    #Initialize the plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    #Set plot limits
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.set_zlim([-10, 10])
    
    #Labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    #Initialize the quiver plot
    quiver = ax.quiver(0, 0, 0, 0, 0, 0)
    
    def update_gravity_vector():
        """Simulate getting new gravity vector data."""
        # Random gravity vector for simulation purposes
        g_x = random.uniform(-9.8, 9.8)
        g_y = random.uniform(-9.8, 9.8)
        g_z = random.uniform(-9.8, 9.8)
        return np.array([g_x, g_y, g_z])
    
    def update(num):
        """Update the quiver plot with new gravity vector data."""
        g_vector = update_gravity_vector()
    
        # Update the quiver plot with the new vector
        global quiver
    
        # Clear previous quiver
        quiver.remove()
        quiver = ax.quiver(0, 0, 0, g_vector[0], g_vector[1], g_vector[2], color='r', length=10)
    
    #Create the animation
    ani = FuncAnimation(fig, update, interval=500)
    
    plt.show()
    #Main loop for updating the plot
    while True:
        g_vector = update_gravity_vector()
    
    #Remove the previous quiver
        quiver.remove()
    
    #Add the updated quiver
        quiver = ax.quiver(0, 0, 0, g_vector[0], g_vector[1], g_vector[2], color='r')
    
    #Pause to update the plot
        plt.pause(0.5)

if __name__ == "__main__":
    init_uart()
    init_graph()

    while(1):
        texto = read_uart()
        parse_accel(texto)
        update_graph()