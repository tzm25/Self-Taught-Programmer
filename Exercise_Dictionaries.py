info={"name":"Thant Zin Moe", "gender":"Male", "age":"22", "address":"No.20, 125th street, 3rd floor, Mingalar Taung Nyunt Township, Yangon", "phone":"(+95)9777789112"}

user=input("Please type the information that you want to know about me: ").lower()

ans=info.get(user, "Invalid information")

print(ans)
