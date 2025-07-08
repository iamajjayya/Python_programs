mylist = ["geeks","for","geeks","for"]
word = "geeks"
n=2
count = 0

for i in range(0, len(mylist)):
    if(mylist[i] == word):
        count += 1
        if (count == n):
          del mylist[i]
          break
        
print(mylist)
        