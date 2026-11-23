import threading
import time
import serial


class ArduinoBridge:

    def __init__(self, port='/dev/ttyACM0', baud_rate=9600, timeout=1.0):
        self.port = port
        self.baud_rate = baud_rate
        self.timeout = timeout
        self.ser = None
        self.lock = threading.Lock()
        self.connect()

    def connect(self):
        """Establishes serial connection to the Arduino."""
        try:
            self.ser = serial.Serial(
                self.port, self.baud_rate, timeout=self.timeout
            )
            time.sleep(2)  # Wait for Arduino reset on serial connection
            print(f'[ArduinoBridge] Successfully connected on {self.port}')
            return True
        except serial.SerialException as e:
            print(f'[ArduinoBridge] Serial Connection Error: {e}')
            self.ser = None
            return False

    def send_command(self, cmd: str) -> bool:
        """Sends a single character command to Arduino."""
        with self.lock:
            if self.ser and self.ser.is_open:
                try:
                    self.ser.write(cmd.encode('utf-8'))
                    return True
                except serial.SerialException as e:
                    print(f'[ArduinoBridge] Write Error: {e}')
                    return False
            return False

    def read_distance(self) -> float:
        """Triggers distance sensor read (Command 'W') and parses output."""
        with self.lock:
            if not (self.ser and self.ser.is_open):
                return -1.0

            try:
                self.ser.reset_input_buffer()
                self.ser.write(b'W')
                time.sleep(0.1)

                response = (
                    self.ser.readline().decode('utf-8', errors='ignore').strip()
                )
                if response.startswith('DIST_CM:'):
                    val = response.split('DIST_CM:')[1]
                    return float(val)
            except (serial.SerialException, ValueError) as e:
                print(f'[ArduinoBridge] Sensor Read Error: {e}')

            return -1.0

    def close(self):
        """Closes the serial port connection."""
        if self.ser and self.ser.is_open:
            self.ser.close()
            print('[ArduinoBridge] Connection closed.')


# Standalone hardware test
if __name__ == '__main__':
    bridge = ArduinoBridge()
    if bridge.ser:
        print('Testing Distance Sensor...')
        dist = bridge.read_distance()
        print(f'Measured Distance: {dist} cm')

        print('Testing Pan Servo Center...')
        bridge.send_command('C')

        bridge.close()