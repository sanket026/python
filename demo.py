def mylist(list):

   list=['sanket','jay','ravi','jayraj','rajkumar']
   getlength=len(list[0])
   getword=list[0]

   for i in list:

    if getlength < len(i):
        getlength =len(i)
        getword=i

    print("longest length is : ",getlength, '\nLongest word is : ',getword)
mylist(list)           