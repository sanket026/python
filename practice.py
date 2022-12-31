"""for num in range(-2,-5,-1):
    print (num,end="")"""

"""
b=30
def fun(a,b=b):
    return a+b
print(fun(1)) """

"""x = {2,3,4}
x.add(5)
print(x)"""

"""for num in range(-2,-5,-1):
    print(num,end=",")"""

"""
list1=[1,2,3,4,5]
print(list1)

list2=['mango,apple,banana']
print(list2)

print(list1+list2)
print(len(list1))
#list1.insert(1,'7')
list1.sort()"""

def  student(id,name="-"):
   print("student id is : ",id)
   print("student name is : ",name)

id=int(input("Enter id : "))   
name=input("Enter your name : ")

student(id,name)