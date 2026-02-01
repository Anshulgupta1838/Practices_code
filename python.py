arr=[.10,20,30,40]
'''n = len(arr)
for i in range(n//2):
    arr[i],arr[n-i-1]=arr[n-i-1],arr[i]

print(arr)'''

max_element = arr[0]
for i in arr:
    if i > max_element:
       max_element = i 

print("largest elemnt:", max_element)