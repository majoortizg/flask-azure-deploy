from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():
    return jsonify({'status': 'ok', 'routes': ['/saludo','/status']}), 200

@app.route('/saludo', methods=['GET'])
def saludo():
    return jsonify({'mensaje': 'OTRAHola Profeee :)))), Fabricio el profe mas cool B) '}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
