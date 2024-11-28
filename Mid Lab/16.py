d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

def combine(d1,d2):
      for key,value in d2.items():
            if key in d1:
                  d1[key]+=value
            else:
                  d1[key]=value

combine(d1,d2)

print(d1)
