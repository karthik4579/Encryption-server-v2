from flask import Flask,request,jsonify
from encrypt import *
from decrypt import dcrypt
app = Flask(__name__)


@app.route('/encrypt', methods=["POST"])
def Encrypt():
        raw_value = str(request.form['raw_value'])
        encrypted_value = ncrypt(raw_value)
        data = {
            "encrypted_value" : f"{encrypted_value}",
            "key" : f"{key.decode()}",
            }

        return jsonify(data)



@app.route('/dcrypt', methods=["POST"])
#This is for login so this will take password decrypt it and return it
def Decrypt(): 
        value = str(request.form['encrytped_value'])
        key = str(request.form['key'])
        key_in_bytes = value.encode()
        value_in_bytes = value.encode()
        decrypted_value = dcrypt(value_in_bytes, key_in_bytes)
        data = {
            "decrypted_value" : f"{decrypted_value}",
            }

        return jsonify(data)
