#Convert Two List into dictonary

keys = ['a', 'b', 'c']
values = [1, 2, 3]
di={}

def convrt(l1,l2,new_di):
      if len(l1) != len(l2) :
            print('This Two List Lenght Are Not same!')
            return
      
      else:
            for i in range(len(l1)):
                  new_di[l1[i]]=l2[i]

convrt(keys,values,di)
print(di)
