mylist = [20,100,20,1,10,2000]

max_val = mylist[0]
min_val = mylist[0]

for x in mylist:
    if x >= max_val:
        max_val = x

for x in mylist:
    if x<= min_val:
        min_val =  x       

maxvalue = max(mylist)
minvalue = min(mylist)



print(maxvalue)  
print(minvalue) 

print(max_val)
print(min_val)