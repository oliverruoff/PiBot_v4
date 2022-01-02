import serial


class TFLuna:
    """Class to operate the tf luna mini lidar sensor.
    """

    def __init__(self):
        # mini UART serial device
        self.ser = serial.Serial("/dev/serial0", 115200, timeout=0)
        if self.ser.isOpen() == False:
            self.ser.open()  # open serial port if not open

    def read_tfluna_data(self):
        """Reads the sensor data and returns distance (in m), signal strength and sensor temperature.

        Returns:
            list: Distance in m, signal strength, Temperature in °C.
        """
        if self.ser.isOpen() == False:
            self.ser.open()  # open serial port if not open
        while True:
            counter = self.ser.in_waiting  # count the number of bytes of the serial port
            if counter > 8:
                bytes_serial = self.ser.read(9)  # read 9 bytes
                self.ser.reset_input_buffer()  # reset buffer
                # distance in next two bytes
                distance = bytes_serial[2] + bytes_serial[3]*256
                # signal strength in next two bytes
                strength = bytes_serial[4] + bytes_serial[5]*256
                # temp in next two bytes
                temperature = bytes_serial[6] + bytes_serial[7]*256
                temperature = (temperature/8.0) - \
                    256.0  # temp scaling and offset
                self.ser.close()
                return distance/100.0, strength, temperature

    def read_distance(self):
        """Wraps around function `read_tfluna_data`, crops away all return values, but distance.
        Returns the distance in m. 

        Returns:
            int: Distance in m.
        """
        return self.read_tfluna_data()[0]
