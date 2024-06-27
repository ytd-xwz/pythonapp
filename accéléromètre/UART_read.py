import  serial, time 
import numpy as np                      # import the numpy library and rename it np
from matplotlib import pyplot as plt    # import from the matplotlib library the fonction pyplot and rename it plt

ser  =  serial.Serial(port  =  "COM3" , baudrate = 9600 , timeout = 2 )
if  (ser.isOpen()  ==  False):
    ser. open ()                                       # check and open Serial0
ser.flushInput()                                       # clear the UART Input buffer
ser.flushOutput()                                      # clear the UART output buffer

echostring = 'blabla'

def echotest():
    while (True):                                      # loop
        ser.flushInput()                               # Clear UART Input buffer
        ser.flushOutput()                              # Clear UART Output buffer
        time.sleep(0.5)                            
        bs = ser.readline().decode('utf-8').strip()
        print(repr(bs))
        vector = parse(bs)
        print(vector)
        graph(vector)

def destroy():
    ser.close ()                                          # Closes the serial port
    print ("test complete")

def parse(txt):
    """
    @brief receives three numbers into a string and split it into three integer

    @param txt
    """

    a = txt.split()

    x = int((a[0]))
    y = int((a[1]))
    z = int((a[2]))

    return(x, y, z)

def graph(vector_coor):     
    fig = plt.figure()                  # Creating an empty figure or plot
    
    ax = plt.axes(projection="3d")      # Defining the axes as a 3D axes so that we can plot 3D data into it. 

    x=[0,vector_coor[0]]
    y=[0,vector_coor[1]]
    z=[0,vector_coor[2]]
    
    ax.plot3D(x, y, z, 'red')                   # plotting a scatter plot with X-coordinate, Y-coordinate and Z-coordinate respectively and defining the points color as 
    ax.scatter3D(x, y, z, c=z, cmap='cividis')  # cividis and defining c as z which basically is a definition of 2D array in which rows are RGB or RGBA

    plt.show()

if __name__ == '__main__':                                 # Program entry point
    try:
        echotest()                                     # call echotest function
    except KeyboardInterrupt:                              # Watches for Ctrl-C
        destroy()                                          # call destroy function
    finally:
        destroy()                                          # call destroy function