import re

password=input('enter password = ')
password_pattern='[A-Z]+[a-z]+[0-9]+[!@$%]+{6,12}'

x=re.findall(password_pattern,password)

if x:
    print('password is valid')
else:
    print('password is invalid')
