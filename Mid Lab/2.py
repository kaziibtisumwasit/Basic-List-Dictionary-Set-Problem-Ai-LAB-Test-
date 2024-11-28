#Remove Duplicate from the list
a=[1,1,1,1,1,3,4,6,2,1,3,4]

new_list=[]

for i in a:
      if i not in new_list:
            new_list.append(i)

for i in range(len(new_list)):
      print(i ,end=" ")



# another way to remove duplicate using set function

b=[2,1,3,4,1,2,3,3,3,3,34,4,5,6,6]

e=set(b)

print(f"\n\nUsing Set Function to remove duplicate")

for i in e:
      print(i , end=" ")