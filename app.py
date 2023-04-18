from flask import Flask,request,jsonify
from encrypt import *
from decrypt import dcrypt
import base64
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



@app.route('/decrypt', methods=["POST"])
#This is for login so this will take password decrypt it and return it
def Decrypt(): 
        value = str(request.form['encrypted_value'])
        key = str(request.form['key'])
        key_in_urlsafe_bytes = base64.urlsafe_b64encode(key.encode()) # we are encoding to bytes first then converting to urlsafe base64
        value_in_bytes = value.encode()
        decrypted_value = dcrypt(value_in_bytes, key_in_urlsafe_bytes)
        data = {
            "decrypted_value" : f"{decrypted_value}",
            }

        return jsonify(data)
