import serial
import time
import csv

ser = serial.Serial('/dev/cu.usbmodem146101')
ser.flushInput()

while True:
    ser_bytes = ser.readline()
    print(ser_bytes)
