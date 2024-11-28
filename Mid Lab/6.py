l1=[1, 2, 3, 4]
l2=[3,4,1,2]

def is_identical(lst1,lst2):
      if len(lst1) != len(lst2):
            return False
      
      double_list=lst1+lst1
      return lst2 in double_list


      
print(is_identical(l1,l2))