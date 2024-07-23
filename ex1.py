list1 = [1,2,3,4,5]
list1[2:4] = [6,7,8] 
print(list1)

max_elements = 0

def max_element(arr):
    global max_elements
    max_elements = arr[0]
    for i in arr:
        if i > max_elements:
            max_elements = i
    return max_elements
result = max_element(list1)
print(result)



