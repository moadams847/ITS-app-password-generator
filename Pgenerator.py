import random

def generate_password(passlen):
    s= "abcdefghjk!$%&+?mnpqrstuvwxyz23456789!$%&+?ABCDEFGHJKMNPQRSTUVWXYZ!$%&+?"
    p = "".join(random.sample(s,passlen ))
    return p

def generate_passwordWithoutXtics(passlen):
    s= "abcdefghjkmnpqrstuvwxyz23456789ABCDEFGHJKMNPQRSTUVWXYZ"
    p = "".join(random.sample(s,passlen ))
    return p

    
if __name__ == '__main__':
    user = input('Enter number: ')
    print(generate_password(int(user)))