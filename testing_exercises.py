#x = "There are %d types of people"%10
#binary = "binary"
#do_not = "don't"
#y = "Those who know %s and those who %s"%(binary,do_not)

#print(x)
#print(y)

#print("I said %r"%x)
#print ("I also said %s"%y)


#formatter = "%r %r %r %r"

#print (formatter % (1,2,3,4))

#months = "Jan \n Feb"
#print (months)

#t = "\tHello"
#print(t)

#g = "\t*Hi\n \t*Hello\n \t*Fuck u"
#print (g)

#age = input("Please type your age: ")
#height = input ("Please type your height: ")
#weight = input ("Please type your weight: ")

#print("Your age is %r, your height is %r, your weight is %r" %(age,height,weight))



#script, first, second, third = argv
#print("The script is",script)
#print("The firsr var is",first)
#print("The second var is",second)
#print("The third var is",third)



#print("Hello %s, I'm %s"%(user_name,script))
#print("I'd like to ask you a few questions.")
#print("Do you like me %s?"%user_name)
#likes = input(">")

#print("Where do u live? %s"%user_name)
#live = input(">")

#print("What kind of computer do you have?")
#computer = input(">")

#print ("So u said %r, u live in %r and u have %r computer"%(likes,live,computer))

from sys import argv

script, filename = argv

txt = open(filename, "w")

print("Your filename is %r"%filename)

print(txt.read())