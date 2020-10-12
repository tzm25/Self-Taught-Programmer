def count_string(string):
    count_ = {}
    for c in string:
        if c in count_:
            count_[c]+= 1
        else:
            count_[c] = 1
    print(count_)

count_string("heellooee")