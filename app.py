from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():
    return jsonify({'status': 'ok', 'message': 'API running'}), 200

@app.route('/saludo', methods=['GET'])
def saludo():
    return jsonify({'mensaje': 'Hola Mundo, como estas, sera, quien sabe pero parece que si'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
