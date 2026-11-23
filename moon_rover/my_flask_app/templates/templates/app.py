import os
import time
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
import serial

load_dotenv()

app = Flask(__name__, template_folder='templates')
CORS(app)

SERIAL_PORT = os.getenv('SERIAL_PORT', '/dev/ttyACM0')
BAUD_RATE = 9600

try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=2)
    time.sleep(2)
    print(f'Connected to Arduino Uno on {SERIAL_PORT}')
except Exception as e:
    ser = None
    print(f'Serial connection warning: {e}')


def send_command(cmd_char):
    if ser and ser.is_open:
        ser.write(cmd_char.encode('utf-8'))
        return True
    return False


# --- Serve Web Dashboard ---
@app.route('/')
def index():
    return render_template('index.html')


# --- API Endpoints ---
@app.route('/api/control', methods=['POST'])
def control():
    data = request.get_json(silent=True) or {}
    action = str(data.get('action', '')).upper()

    COMMAND_MAP = {
        'FORWARD': 'F',
        'BACKWARD': 'B',
        'LEFT': 'L',
        'RIGHT': 'R',
        'STOP': 'S',
        'DRILL_MOTOR_ON': 'D',
        'DRILL_MOTOR_OFF': 'd',
        'DRILL_EXTEND': 'U',
        'DRILL_RETRACT': 'J',
        'DRILL_STOP': 'H',
        'NPK_EXTEND': 'N',
        'NPK_RETRACT': 'M',
        'NPK_STOP': 'K',
        'PAN_LEFT': 'P',
        'PAN_CENTER': 'C',
        'PAN_RIGHT': 'p',
    }

    if action in COMMAND_MAP:
        cmd = COMMAND_MAP[action]
        if send_command(cmd):
            return jsonify({'status': 'success', 'action': action, 'command': cmd}), 200
        return jsonify({'status': 'error', 'message': 'Serial port not available'}), 503

    return jsonify({'status': 'error', 'message': f'Invalid action: {action}'}), 400


@app.route('/api/distance', methods=['GET'])
def get_distance():
    if not (ser and ser.is_open):
        return jsonify({'status': 'error', 'message': 'Serial port not available'}), 503

    ser.reset_input_buffer()
    send_command('W')
    time.sleep(0.1)

    response = ser.readline().decode('utf-8', errors='ignore').strip()
    return jsonify({'status': 'success', 'raw_data': response}), 200


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)