#Check if a list's elements are unique


lst = [1, 2, 3, 4]

def are_unique(l):
     
      if len(set(l))==len(l): #after using set function remove duplicate elements from 
            return f"This List Elements Are Unique !"
      else:
            return f"This List Element Are Not Unique !"
      
result=are_unique(lst)
print(result)