from flask import Flask,jsonify,request
from classifier import recogniseAlphabet
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route("/getAlphabet", methods = ["POST"])
def getAlphabet():
    res = request.args.get("name")
    alphabet = recogniseAlphabet(res)    
    return jsonify({ "predicted-alphabet":alphabet}),200
        
if __name__ == "__main__": 
    app.run(debug=True)