# Write a Python program to compute the difference between two lists.

l1=["red", "orange", "green", "blue", "white"]
l2=["black", "yellow", "green", "blue"]
# new_list=[]

# def defferance(l1,l2):
#       for i in l1:
#             if i not in l2:
#                   new_list.append(i)

#       for i in l2:
#             if i not in l2:
#                   new_list.append(i)



def defferance(l1,l2):
 return f"list1={set(l1)-set(l2)}./nlist2={set(l2)-set(l1)}"

print(defferance(l1,l2))

