arr =[10,20,30,40]
key = 10

found = False
for i in arr:
    if i == key:
        found = True
        break
print("Found"if found else"not found")
