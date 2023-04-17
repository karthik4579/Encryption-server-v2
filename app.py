from flask import Flask,request,jsonify
from encrypt import *
from decrypt import dcrypt
app = Flask(__name__)


@app.route('/encrypt', methods=["POST"])
def Encrypt():
    value0 = str(request.form['activity'])
    if(value0 == "register"):
        valuer1 = str(request.form['password'])
        valuer2 = str(request.form['nfcpassword'])
        a = ncrypt(valuer1)
        e = ncrypt(valuer2)
        data = {
            "password" : f"{a}",
            "nfcpassword" : f"{e}",
            "key" : f"{key}",
            }

        return jsonify(data)
        
    elif(value0 == "nfcreset"):
        valuen1 = str(request.form['newnfcpassword'])
        b = ncrypt(valuen1)
        data1 = {
            "newnfcpassword" : f"{b}",
            "key" : f"{key}",
            }

        return jsonify(data1)

    elif(value0 == "userpassreset"):
        valueu1 = str(request.form['newuserpassword'])
        c = ncrypt(valueu1)
        data2 = {
            "newuserpassword" : f"{c}",
            "key" : f"{key}",
            }

        return jsonify(data2)



@app.route('/dcrypt', methods=["POST"])
#This is for login so this will take password decrypt it and return it
def Decrypt(): 
        valuel1 = str(request.form['password'])
        key = str(request.form['enckey'])
        key_bytes = bytes(key, 'ascii')
        c = bytes(valuel1, 'ascii')
        d = dcrypt(c, key)
        data3 = {
            "password" : f"{d}",
            }

        return jsonify(data3)
