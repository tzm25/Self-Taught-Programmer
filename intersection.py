def intersect(list1,list2):
    list3 = [value for value in list1 if value in list2]
    return list3

list1 = [1,2,3,4,5,6,7,8]
list2 = [7,8,9,10,11,12,13]

print(intersect(list1,list2))

def ret_intersect(list1,list2):
    s1 = set(list1)
    s2 = set(list2)
    return list(s1.intersection(s2))

print(ret_intersect(list1,list2))
<<<<<<< HEAD
=======


>>>>>>> 2b90751ba279723f50d4bf03b87f8505dd8c0eb8
