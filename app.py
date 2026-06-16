from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def receive():
    data = request.json
    print('收到消息:', json.dumps(data, ensure_ascii=False, indent=2))
    return 'OK', 200

if __name__ == '__main__':
    app.run()
