# swap element two position in list 
a=[10, 20, 30, 40, 50]


def swaping(lst,index1,index2):
      if len(lst) > index1  and len(lst) > index2:
            lst[index1] ,lst[index2] =lst[index2] ,lst[index1]
            return lst

      else:
            return f"Invalid Index !!"
      


my_list = [10, 20, 30, 40, 50]

result=swaping(my_list,2,3)

for i in result:
      print(i,end=" ")
