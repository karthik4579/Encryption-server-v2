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



@app.route('/decrypt', methods=["POST"])

def Decrypt():
        value = str(request.form['encrypted_value'])
        key = str(request.form['key'])
        key_in_bytes = key.encode('ascii')
        value_in_bytes = value.encode('ascii')
        decrypted_value = dcrypt(value_in_bytes,key_in_bytes)
        data = {
            "decrypted_value" : f"{decrypted_value}",
            }

        return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
