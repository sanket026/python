list1=[1,3,5,7]
list2=[2,7,8,4]
result = 0
def find_common(list1, list2):
     for x in list1:
         for y in list2:
             if x == y:
                 result = True
                 return result
             else:
               result = False
               return result
print(find_common(list1, list2))