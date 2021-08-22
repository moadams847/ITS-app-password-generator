import random

def generate_password(passwordLength):
    samplestring= "abcdefghjk!$%&+?mnpqrstuvwxyz23456789!$%&+?ABCDEFGHJKMNPQRSTUVWXYZ!$%&+?"
    passwordString = "".join(random.sample(samplestring,passwordLength))
    return passwordString


    
if __name__ == '__main__':
    user = input('Enter number: ')
    print(generate_password(int(user)))