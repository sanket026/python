number=int(input("Please enter the Maximum Number : "))
myDict={}

for x in range(1,number+1):
    myDict[x] = x**2
    
print("\nDictionary = ",myDict)