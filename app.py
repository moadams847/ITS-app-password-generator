from flask import Flask, request, jsonify, render_template
from Pgenerator import generate_password

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/password", methods = ['POST', 'GET'])
def password():
    try:
            
        if request.method == 'POST':
            passlen = int(request.form['password_length'])
            
        if passlen > 0  and passlen <= 12:
            p = generate_password(passlen)
            return render_template('password.html', gen_pas = f'{p}')

        elif passlen <= 0:
            return render_template('password.html', gen_pas = f'Password length must be greater 0')

        elif passlen > 12 and  passlen <= 54:
            p = generate_password(passlen)
            return render_template('password.html', gen_pas = f'{p}')
            
        elif passlen > 54:
            return render_template('password.html', gen_pas = f'Password length must be less than 55')
            
    except:
        return render_template('home.html')

            
        
               
if __name__ == '__main__':
    app.run(debug = True)