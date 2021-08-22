import random

def generate_password(passwordLength):
    sampleWithXitcs = "abcdefghjk!$%&+?mnpqrstuvwxyz23456789!$%&+?ABCDEFGHJKMNPQRSTUVWXYZ!$%&+?"
    passwordString = "".join(random.sample(sampleWithXitcs,passwordLength ))
    return passwordString

def generate_passwordWithoutXtics(passwordLength):
    sampleWithoutXitcsList= "abcdefghjkmnpqrstuvwxyz23456789ABCDEFGHJKMNPQRSTUVWXYZ"
    passwordString = "".join(random.sample(sampleWithoutXitcsList,passwordLength ))
    return passwordString

    
if __name__ == '__main__':
    user = input('Enter number: ')
    print(generate_password(int(user)))