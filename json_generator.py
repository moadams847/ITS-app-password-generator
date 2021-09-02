# something i want to try
from flask import Flask, request, jsonify
from password_generator import generate_password, generate_passwordWithoutXtics

def generateJsonData(passwordLength):
    passwordLength = int(request.args.get(passwordLength))
    try:        
        if passwordLength > 0  and passwordLength <= 54:
            passwordString = generate_password(passwordLength)
            return jsonify({'password': passwordString})

        elif passwordLength <= 0:
            return jsonify({'password':'Password length must be greater 0'})
        
        elif passwordLength > 54:
            return jsonify({'password':'Password length must be less than 55'})
    except:
        return jsonify({'password': 'Make a request by passing a password length'})