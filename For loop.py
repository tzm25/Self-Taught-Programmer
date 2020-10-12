blog_post=["","The 10 coolest math functions in Python","", "How to make HTTP requests in Python", "A tutorial about data types in python"]
for post in  blog_post:
    if post == "":
        continue
    else:
        print(post)

myString="This is a string"
for char in myString:
    print(char)


for x in range(0,20):
    print(x)


my_info={"Name":"TZM", "Age":"22", "Gender":"Male"}

for key in my_info:
    print(key, ":", my_info[key])
    
blog_post={"Python":["The 10 coolest math functions in Python", "How to make HTTP requests in Python", "A tutorial about data types in python"], "Javascript":["Namespaces in Javascript","New functions available in ES6"]}
for category in blog_post:
    print("Posts about", category)
    for post in blog_post[category]:
        print(post)
