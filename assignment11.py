lst = [1,2,2,3,3,4,4,5,5,6,6]
one_ = {}
for i in lst:
    if i in one_:
        one_[i] += 1
    else:
        one_[i] = 1

for key,value in one_.items():
    if value == 1:
        print(key)