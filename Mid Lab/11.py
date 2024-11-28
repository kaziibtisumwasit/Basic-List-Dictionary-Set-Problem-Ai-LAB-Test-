# Write a Python script to check whether a given key already exists in a dictionary.

d = {'a': 1, 'b': 2}

def exist(key,di):
      if key in di:
            return f"Yes,Exist ! "
      
      else :
            return f"not Exist ! "
      

print(exist("f",d))