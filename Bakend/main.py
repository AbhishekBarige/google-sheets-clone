from flask import Flask, request, jsonify
from services.formulas import sum_range, average
from services.data_quality import trim, upper, lower, remove_duplicates, find_and_replace

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    formula = data.get("formula")
    cells = data.get("cells")

    if formula == "SUM":
        result = sum_range(cells)
    elif formula == "AVERAGE":
        result = average(cells)
    # Add other formulas as needed
    return jsonify({"result": result})

@app.route('/data_quality', methods=['POST'])
def data_quality():
    data = request.json
    operation = data.get("operation")
    values = data.get("values")

    if operation == "TRIM":
        result = trim(values)
    elif operation == "UPPER":
        result = upper(values)
    # Add other data quality functions as needed
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
