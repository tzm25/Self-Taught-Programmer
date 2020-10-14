def intersect(list1,list2):
    list3 = [value for value in list1 if value in list2]
    return list3

list1 = [1,2,3,4,5,6,7,8]
list2 = [7,8,9,10,11,12,13]

print(intersect(list1,list2))

