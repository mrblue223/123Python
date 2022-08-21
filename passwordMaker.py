import random
passlen = int(input("Enter the lenght of the password: "))
s="abcdefghijklmnopqrstuvwxyz!@#$%^&*()?"
p = "".join(random.sample(s,passlen ))
print(p)
