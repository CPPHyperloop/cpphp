import serial
ser = serial.Serial('/dev/ttyACM0', baudrate=115200)  # open serial port
print(ser.name)         # check which port was really used

try:
    while(1):
        ser.flush()
        data = ser.readline()
        print(data)

except KeyboardInterrupt:
    ser.close()             # close port
