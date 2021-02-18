from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():

    return render_template('home.html')

@app.route("/password", methods = ['POST', 'GET'])
def password():

    if request.method == 'POST':

        try:

            passlen = int(request.form['password_length'])
            s= "!#$%&-=+?abcdefghjk!#$%&-=+?mnpqrstuvwxyz23456789!#$%&-=+?ABCDEFGHJKMNPQRSTUVWXYZ!#$%&-=+?"
            str_ = "abcdefghjkmnpqrstuvwxyz23456789ABCDEFGHJKMNPQRSTUVWXYZ"
            

            if passlen > 0  and passlen <= 12:
                
                p = "".join(random.sample(s,passlen ))
                return render_template('home.html', gen_pas = f'Temporary ITS password generated:     {p}')

            elif passlen <= 0:
                return render_template('home.html', gen_pas = f'Password length must be greater 0')

            elif passlen > 12 and  passlen <= 54:

                p = "".join(random.sample(str_,passlen ))
                return render_template('home.html', gen_pas = f'Temporary ITS password generated:     {p}')
            
            elif passlen > 54:
                return render_template('home.html', gen_pas = f'Password length must be less than 55')


        except:
            return render_template('home.html', gen_pas = f'Wrong entry, Provide a number!!')
                    
    else: 
        return render_template('home.html')
               
if __name__ == '__main__':
    app.run(debug = True)