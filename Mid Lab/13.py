d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}


def commbine_dicts(di1,di2):
      result=di1.copy()
      
      for key,value in di2.items():
            if key in result:
                  result[key]+=value

            else:
                  result[key]=value

      return result

print(commbine_dicts(d1,d2))







