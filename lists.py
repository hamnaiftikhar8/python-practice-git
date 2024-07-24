def find_Common(*lists):
    if not lists:
        return []
    common = set(lists[0])

    for i in lists[1:]:
        common.intersection_update(i)


    return list(common)


list1 = [1,2,3,4,5,6,7,8]
list2 = [2,3,4,9,10,12]
list3 = [22, 3,4,23,10,5]

print(find_Common(list1,list2,list3))