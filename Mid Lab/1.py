a=[1,3,4,6,2,1,3,4]
b=[5,4,3,2,5,6]

combine=[]

for i in a[::-1]:
      combine.append(i)

for i in b[::-1]:
      combine.append(i)

for i in combine:
      print(i ,end=" ")  #,end="" skip new line in print statement