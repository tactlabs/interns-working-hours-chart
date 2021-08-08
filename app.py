from flask import Flask,render_template, jsonify, request
import random
import json
import data


app  = Flask(__name__)
PORT = 3000

@app.route("/", methods=["GET","POST"])
def startpy():
    
    result = {

        "Greetings" : "Tactlabs welcomes you"
    }


    return render_template("index.html") 




@app.route("/aj", methods=["GET","POST"])
def aj():
    return render_template('aj.html')



@app.route("/ana", methods=["GET","POST"])
def ana():
    return render_template('ana.html')

@app.route("/sateesh", methods=["GET","POST"])
def sateesh():
    return render_template('sateesh.html')

@app.route("/ish", methods=["GET","POST"])
def ish():
    return render_template('ish.html')

@app.route("/akash", methods=["GET","POST"])
def akash():
    return render_template('akash.html')



@app.route("/noor", methods=["GET","POST"])
def noor():
    return render_template('noor.html')

@app.route("/kash", methods=["GET","POST"])
def kash():
    return render_template('kash.html')

@app.route("/prav", methods=["GET","POST"])
def prav():
    return render_template('prav.html')

@app.route("/suda", methods=["GET","POST"])
def suda():
    return render_template('suda.html')

@app.route("/tal", methods=["GET","POST"])
def tal():
    return render_template('tal.html')

@app.route("/ved", methods=["GET","POST"])
def ved():
    return render_template('ved.html')    


'''
http://0.0.0.0:3091/api/data
'''

@app.route("/api/data", methods=["GET"])
def api_get_data():

    result = data.get_data()

    return jsonify(result)

'''
http://0.0.0.0:3091/api/add
http://0.0.0.0:3091/api/add?year=2017&ontario_tourist=20345&quebec_tourist=200
http://0.0.0.0:3000/api/add?year=2021&pytorch=180&tensorFlow=90
'''




if __name__ == "__main__":
    app.run(debug = True,host="0.0.0.0",port = PORT)