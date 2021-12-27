import serial
import time
import numpy as np


class TFLuna:

    def __init__(self):
        # mini UART serial device
        self.ser = serial.Serial("/dev/serial0", 115200, timeout=0)
        print('1')
        if self.ser.isOpen() == False:
            self.ser.open()  # open serial port if not open
        print('2')

    def read_tfluna_data(self):
        while True:
            counter = self.ser.in_waiting  # count the number of bytes of the serial port
            print('3')
            if counter > 8:
                bytes_serial = self.ser.read(9)  # read 9 bytes
                print('4')
                self.ser.reset_input_buffer()  # reset buffer
                print('5')
                # distance in next two bytes
                distance = bytes_serial[2] + bytes_serial[3]*256
                # signal strength in next two bytes
                strength = bytes_serial[4] + bytes_serial[5]*256
                # temp in next two bytes
                temperature = bytes_serial[6] + bytes_serial[7]*256
                temperature = (temperature/8.0) - \
                    256.0  # temp scaling and offset
                return distance/100.0, strength, temperature

    def read_distance(self):
        if self.ser.isOpen() == False:
            self.ser.open()  # open serial port if not open
        distance = self.read_tfluna_data()[0]
        self.ser.close()
        return distance
