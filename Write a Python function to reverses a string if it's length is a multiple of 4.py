from os import name


name=("enter a name:")

if(len(name)%4==0):
    print(name[::-1])
else:
    print("cant")
