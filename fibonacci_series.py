# #sum of the two preceding number 

# # 0  1  1 2 3 5 8 13
# # n1 n2
# n1 =  0
# n2 = 1
# print(n1, n2)

# for i in range(2,10):
#     sum = n1+n2 # 1
#     print(sum)
#     n1 = n2 # 1
#     n2 = sum # 1



def fibonacii_series(n):
    a = 0
    b = 1
    for _ in range(n):
        print(a, end=" ")
        a,b = b,a+b



fibonacii_series(10)          
