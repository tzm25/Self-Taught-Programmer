def return_duplicate(lst):
    set_ = set()
    dups = []
    for item in lst:
        lenght_one = len(set_)
        set_.add(item)
        length_two = len(set_)
        if lenght_one == length_two:
            dups.append(item)
    return dups

lst = ["TZM","void","micheal","TZM"]

dups = return_duplicate(lst)
print(dups)
