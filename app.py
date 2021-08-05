from flask import Flask, request
from Pgenerator import generate_password

app = Flask(__name__)

@app.route("/")
def home():
    return 'Welcome'

@app.route("/password")
def password():
    try:
        passlen = int(request.args.get('passlen'))
            
        if passlen > 0  and passlen <= 12:
            p = generate_password(passlen)
            return f'The generated password is: {p}'

        elif passlen <= 0:
            return f'Password length must be greater 0'

        elif passlen > 12 and  passlen <= 54:
            p = generate_password(passlen)
            return f'The generated password is: {p}'
            
        elif passlen > 54:
            return f'Password length must be less than 55'
            
    except:
        return f'Make a request'

            
        
               
if __name__ == '__main__':
    app.run(debug = True)