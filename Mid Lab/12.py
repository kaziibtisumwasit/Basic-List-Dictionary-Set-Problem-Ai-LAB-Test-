a = {
    1: 1,
    2: 4,
    55: 5,
    3: 9,
    16: 33,
    5: 63,
    6: 35,
    10: 100,
    20: 400
}

def fun(dic):
      # update_dic={}
      for key,value in dic.items():
            if key>0 and key<=15 :
                  if key*key==value:
                        print(key , value )
            # else:
            #       update_dic[key]=value
      # return update_dic

# print(fun(a))
fun(a)