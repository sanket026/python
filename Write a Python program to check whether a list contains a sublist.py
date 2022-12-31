Alist = ['Mon','Tue', 5, 'Sat', 9]
Asub_list = ['Tue',5,9]
print("Given list ",Alist)
print("Given sublist",Asub_list)

if (all(x in Alist for x in Asub_list)):
   print("Sublist is part of bigger list")
else:
   print("Sublist is not part of bigger list")

Asub_list = ['Wed',5,9]
print("New sublist",Asub_list)
if (all(x in Alist for x in Asub_list)):
   print("Sublist is part of bigger list")
else:
   print("Sublist is not part of bigger list")