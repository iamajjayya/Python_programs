# text  = [1,2,3,4,5]

# count  = 0 

# for _ in text:
#     count += 1

# i = 0

# while i < count // 2:
#     temp  =  text[i]
#     text[i] = text[count - i - 1]
#     text[count - i - 1] =  temp
#     i += 1

# print(text) 
# print(text[1])   

# mylist = [10,23,12,87,32]

# # sort_list= sorted(mylist)


# print(sort_list[-2])

mylist =  [10,23,8,54,23]
# mylist.sort(reverse=True)
# print(mylist[1])

new_list = set(mylist)
new_list.remove(max(new_list))
print(mylist)
print(max(new_list))
