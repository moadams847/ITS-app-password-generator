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
        passwordLength = int(request.args.get('passwordLength'))
            
        if passwordLength > 0  and passwordLength <= 54:
            passwordString = generate_password(passwordLength)
            return jsonify({'password': passwordString})

        elif passwordLength <= 0:
            return jsonify({'password':'Password length must be greater 0'})
        
        elif passwordLength > 54:
            return jsonify({'password':'Password length must be less than 55'})

            
    except:
        return jsonify({'password': 'Make a request by passing a password length'})


@app.route("/passwordapi/v2/no-special-characters", methods= ['GET','POST'])
def passwordWithoutXtics():
    try:
        passwordLength = int(request.args.get('passwordLength'))
            
        if passwordLength > 0  and passwordLength <= 54:
            passwordString = generate_passwordWithoutXtics(passwordLength)
            return jsonify({'password': passwordString})

        elif passwordLength <= 0:
            return jsonify({'password':'Password length must be greater 0'})
        
        elif passwordLength > 54:
            return jsonify({'password':'Password length must be less than 55'})

            
    except:
        return jsonify({'password': 'Make a request by passing a password length'})

            
        
               
if __name__ == '__main__':
    app.run(debug = True)