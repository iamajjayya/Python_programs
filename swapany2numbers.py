# # //Apparoch 1
# # mylist  = [2,3,6,8,9,18]
# # print(mylist)
# # post1,post2 = 2,5
# # mylist[post1],mylist[post2] = mylist[post2],mylist[post1]
# # print(mylist)
# # # 

# #using list.pop function 

# mylist = [10,20,30,40,60]
# post1,post2= 1,3
# first_element = mylist.pop(1) #20
# second_element = mylist.pop(3) #40
# print(mylist)
# mylist.insert(post1,second_element)
# mylist.insert(post2,first_element)
# print(mylist)

mylist = [10,20,30,40,60]
post1,post2= 1,3
get = (mylist[post1],mylist[post2])
mylist[post2],mylist[post1] = get
print(mylist)
