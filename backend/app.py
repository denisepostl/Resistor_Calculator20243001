from flask import Flask, request, jsonify
from flask_cors import CORS
from r_calculator import calculate_series, calculate_parallel

app = Flask(__name__)
CORS(app)

@app.route('/calculate', methods=['POST'])
def calculate():
    """
    Endpoint for calculating the resistance in either series or parallel.

    Expects a JSON payload in the following format:
    {
        "resistances": [list of resistances],
        "calculation_type": "series" or "parallel"
    }

    Returns a JSON response containing the calculated result or an error message.

    Parameters:
    - None

    Returns:
    - JSON response with the calculated result or an error message.
    """
    data = request.get_json()

    resistances = data.get('resistances', [])

    if data['calculation_type'] == 'series':
        result = calculate_series(resistances)
    elif data['calculation_type'] == 'parallel':
        result = calculate_parallel(resistances)
    else:
        return jsonify({'error': 'Invalid calculation type'}), 400

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
