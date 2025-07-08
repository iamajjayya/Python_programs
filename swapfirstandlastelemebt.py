swap  =  [100,14,232,3,4,5,10,34,56,32]
# print(swap)
# swap[0],swap[-1] = swap[-1], swap[0]

get =  (swap[-1],swap[0])
swap[0],swap[-1] =  get
print(swap)

mylist =  [20,34,56,32,12]
start,*middle,end = mylist
print(start)
print(middle)
print(end)

mylist=[end,*middle,start]
print(mylist)

#approach 5 