from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route('/info', methods=['GET'])
def testget():
    return jsonify({'Receiver':'Cisco is the best!'})


@app.route('/ping', methods=['POST'])
def testpost():
     input_json = request.get_json()                        # {"url": "http://api.plos.org/search?q=title:DNA"}
     res = requests.get(input_json['url']).json()           # {"url": "http://ergast.com/api/f1/2004/1/results.json"}
     return jsonify(res)


if __name__ == "__main__":
    app.run(debug=True)
