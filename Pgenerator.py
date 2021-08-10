import random

def generate_password(passlen):
    s= "abcdefghjk!$%&+?mnpqrstuvwxyz23456789!$%&+?ABCDEFGHJKMNPQRSTUVWXYZ!$%&+?"
    p = "".join(random.sample(s,passlen ))
    return p

def generate_passwordWithoutXtics(passlen):
    ss= "abcdefghjkmnpqrstuvwxyz23456789ABCDEFGHJKMNPQRSTUVWXYZ"
    pp = "".join(random.sample(ss,passlen ))
    return pp

    
if __name__ == '__main__':
    user = input('Enter number: ')
    print(generate_password(int(user)))