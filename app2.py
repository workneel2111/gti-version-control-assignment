from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/submittodoitem', methods=['POST'])
def submit():
if __name__ == '__main__':
    app.run(debug=True)