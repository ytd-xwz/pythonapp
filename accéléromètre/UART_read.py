import  serial, time 

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
        time.sleep(0.1)                            
        bs = ser.readline().decode('utf-8').strip()
        print(repr(bs))

def destroy():
    ser.close ()                                          # Closes the serial port
    print ("test complete")

if __name__ == '__main__':                                 # Program entry point
    try:
        echotest()                                         # call echotest function
    except KeyboardInterrupt:                              # Watches for Ctrl-C
        destroy()                                          # call destroy function
    finally:
        destroy()                                          # call destroy function