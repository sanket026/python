"""a=34
b=90

print("Sum:",A+b)


x=89
y=90
print("Mul:",x*y)"""
 
"""
a= int(input("Enter the value of A :"))
b= int(input("Enter the value of B :"))

try:
    c=a/b 
    print("Division : ",c)
except Exception:
    print("Execption Caught")
    
    
print("Bye")"""

# try finally use

try:
   print(a)
except NameError:
   print("variable a is not defined")
except:
   print("something else ")
else:
   print("Hello user")
finally:
   print("Finally block")