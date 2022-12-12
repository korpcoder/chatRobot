from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'Hello, World!'


@app.route('/answer', methods=['POST'])
def answer():
    texts = request.json['texts']
    # 下面是处理 texts 的代码
    # ...
    return jsonify({'result': '处理后的结果'})


if __name__ == '__main__':
    app.run(debug=True, port=10086)
