from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/', methods=['GET'])
def homeall():
    return jsonify({'data': 'hello world getall'})

@app.route('/byid', methods=['GET'])
def homebyid():
    return jsonify({'data': 'hello world byid'})

@app.route('/<string:namex>', methods=['POST'])
def home2(namex):
    return jsonify({'data': f'hello world post {namex}'})

@app.route('/home/<int:num>', methods=['GET'])
def disp(num):
    return jsonify({'data': num ** 2})

if __name__ == '__main__':
    app.run(debug=True)