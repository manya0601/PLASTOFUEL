from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from ml_model import estimate_yield
from simulator import start_simulation, get_latest_reading

app = Flask(__name__)
CORS(app)

# Start IoT data simulation thread
start_simulation()

@app.route('/')
def home():
    return jsonify({"message": "PlastoFuel Backend API running"})

@app.route('/api/estimate', methods=['POST'])
def estimate():
    data = request.get_json(force=True)
    plastic_type = data.get('plastic_type')
    mass_kg = float(data.get('mass_kg', 0))
    method = data.get('method', 'pyrolysis')

    result = estimate_yield(plastic_type, mass_kg, method)
    sensors = get_latest_reading()

    return jsonify({
        'estimate': result,
        'sensors': sensors
    })

@app.route('/api/sensors', methods=['GET'])
def sensors():
    return jsonify(get_latest_reading())

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
