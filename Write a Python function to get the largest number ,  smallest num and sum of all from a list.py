lst=[]
num = int(input('how many numbers = '))
 
for n in range(num):
    numbers= int(input('enter numbers = '))
    lst.append(numbers)

print("Maximum element in the list is :", max(lst), "\nMinimum element in the list is :", min(lst))    