#function that takes two lists and returns True if they have at least one common member.
list1 = [1, 2, 3, 4]
list2 = [3, 5, 6]

def find_common(lst1,lst2):
      for i in lst1:
            if i in lst2:
                  return True
            

if find_common(list1,list2):
      print("True")

else:
      print("False")




# Another Way To find common in two list
l1=[10, 20, 30, 40, 50]
l2=[1,2,3,2,2]

def is_it_common(lst1,lst2):
      # ls1=set(lst1)
      # ls2=set(lst2)
      
      # if ls1 & ls2:
      #       print("True")

      # else:
      #       print("False")

      # & means intersection in python.its take only common number or digit use it with set function
      return set(lst1) & set(lst2)


if is_it_common(l1,l2):
      print('True')

else:
      print('False')
