import random
sampleWithXitcs = "abcdefghjk!$%&+?mnpqrstuvwxyz23456789!$%&+?ABCDEFGHJKMNPQRSTUVWXYZ!$%&+?"
sampleWithoutXitcsList= "abcdefghjkmnpqrstuvwxyz23456789ABCDEFGHJKMNPQRSTUVWXYZ"
print(len(sampleWithXitcs))
print(len(sampleWithoutXitcsList))

def generate_password(passwordLength):
    passwordString = "".join(random.sample(sampleWithXitcs,passwordLength ))
    return passwordString

def generate_passwordWithoutXtics(passwordLength):
    passwordString = "".join(random.sample(sampleWithoutXitcsList,passwordLength ))
    return passwordString

    
if __name__ == '__main__':
    user = input('Enter number: ')
    print(generate_password(int(user)))