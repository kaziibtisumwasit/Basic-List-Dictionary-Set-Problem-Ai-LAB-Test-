a = [1,4,1,2,4,3,1,5,7,1,5,3]
track={} #a list er element thakbe key hishebe ar oi value er count thakbe value hishebe 

for i in a:
     if i in track.keys():
          track[i]+=1

     else:
          track[i]=1
mx=0
index=None
for key,value in track.items():
     if value > mx:
          mx=value
          index=key

print(f"this item present : {index} : {mx} times")

      