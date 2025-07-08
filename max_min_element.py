arr = [1,2,3,4,5,6,90,23,45]

max = arr[0]
for i in arr:
    if i >= max:
        max = i

print(f"Maximum value in a array ",max)  

min = arr[0]
for i in arr:
    if i <= min:
        min = i

print("Minimum Value in a array", min)  


arrva = [2,3,4,5,6]
maxv =  arrva[0]
n  = len(arrva)

for i in range(1,n):
    if arrva[i] > maxv:
        maxv = arrva[i]

print(maxv)        
    
 