from flask import Flask, Response
import json
import testquery as db

app = Flask(__name__)
@app.route('/test/testapi', methods=['POST'])
def test():
    result = db.querytest()
    return Response(json.dumps(result), mimetype=("application/json"))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=False)
