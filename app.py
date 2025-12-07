from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():
    return jsonify({'status': 'ok', 'routes': ['/saludo','/status']}), 200

@app.route('/status', methods=['GET'])
def status():
    return jsonify({'status': 'running', 'version': '1.0', 'author': 'Majo Ortiz'}), 200

@app.route('/saludo', methods=['GET'])
def saludo():
    return jsonify({'mensaje': 'Mundo, como estas, sera, quien sabe pero parece que si'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)