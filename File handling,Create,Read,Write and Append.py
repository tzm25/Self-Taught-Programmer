f = open("text.txt","a")
f.write("\nThis text will be appended the content of our file")
f = open("text.txt")
print(f.read())
