import time
import serial

print("Starting program")

ser = serial.Serial('/dev/ttyACM0', baudrate=115200)

time.sleep(1)
try:
    print('Data Echo Mode Enabled')
    while True:
        ser.flush()
        data = ser.readline()
        print(data + "\n")

except KeyboardInterrupt:
    print("Exiting Program")

except:
    print("Error Occurs, Exiting Program")

finally:
    ser.close()
    pass
