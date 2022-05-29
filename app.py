from flask import Flask, render_template, jsonify
import random
from datetime import datetime

app = Flask('app')

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/api/datapoint')
def api_datapoint():
    random_number = random.randint(1, 100)
    double_random_number = random_number * 2
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    dictionary_to_return = {
        'random_number': random_number,
        'double_random_number': double_random_number,
        'timestamp': timestamp
    }

    return jsonify(dictionary_to_return)


app.run(host='0.0.0.0', port=8080, debug=True)