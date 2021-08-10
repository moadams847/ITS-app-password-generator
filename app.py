from flask import Flask, request, jsonify
from Pgenerator import generate_password, generate_passwordWithoutXtics

# https://stackoverflow.com/q/20035101
# flask cors
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({'About':'Welcome'})

@app.route("/passwordapi/v2/special-characters", methods= ['GET','POST'])
def passwordWithXtics():
    try:
        passlen = int(request.args.get('passlen'))
            
        if passlen > 0  and passlen <= 54:
            p = generate_password(passlen)
            return jsonify({'password': p})

        elif passlen <= 0:
            return jsonify({'message':'Password length must be greater 0'})
        
        elif passlen > 54:
            return jsonify({'message':'Password length must be less than 55'})

            
    except:
        return jsonify({'catch error': 'Make a request by passing a password length'})


@app.route("/passwordapi/v2/no-special-characters", methods= ['GET','POST'])
def passwordWithoutXtics():
    try:
        passlen = int(request.args.get('passlen'))
            
        if passlen > 0  and passlen <= 54:
            p = generate_passwordWithoutXtics(passlen)
            return jsonify({'password': p})

        elif passlen <= 0:
            return jsonify({'message':'Password length must be greater 0'})
        
        elif passlen > 54:
            return jsonify({'message':'Password length must be less than 55'})

            
    except:
        return jsonify({'catch error': 'Make a request by passing a password length'})

            
        
               
if __name__ == '__main__':
    app.run(debug = True)