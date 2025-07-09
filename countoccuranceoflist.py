from collections import Counter

mylist  = [10,20,30,40,20,10,10]

# x = 20
# count = 0

# for ele in mylist:
#     if (ele == x):
#         count += 1
# print("{} has occured {} times".format(x,count))

# x=15
# print("{} has occured {} times".format(x,mylist.count(x)))

x = 10
dict = Counter(mylist)

print(dict[x])






