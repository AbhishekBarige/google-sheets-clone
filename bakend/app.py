from flask import Flask, render_template, request, jsonify
from functions import sum_cells, average_cells

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    func = data['function']
    values = data['values']

    result = None
    if func == "SUM":
        result = sum_cells(values)
    elif func == "AVERAGE":
        result = average_cells(values)

    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
