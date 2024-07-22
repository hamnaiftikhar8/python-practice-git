list1 = [1,2,3,4,5]
list1[2:4] = [6,7,8] 
print(list1)

max_element = 0

for i in list1:
    if i > max_element:
        max_element = i

print(max_element)
