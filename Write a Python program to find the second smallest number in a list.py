li = []
n=int(input('enter the numbers of elements : '))
for i in range(1,n+1):
    elem = int(input('enter the elements : '))
    li.append(elem)
li.sort()
print("The sorted list: ", li) 
print("The second smallest value of this list: ",li[1])