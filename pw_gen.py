import random

cap_ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sma_ = "abcdefghijklmnopqrstuvwxyz"
num_ =  "123456789"
sym_ = ":;#%$&*"

all_= cap_+sma_+num_+sym_
length = 16
passwd = "".join(random.choice(all_,length))

print(passwd)

