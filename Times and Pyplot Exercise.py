import matplotlib.pyplot as plt
import time as t

times=[]
mistakes=0

print("This program will help you type faster. You will have to type the word 'programming' as fast as you can for five times")

input("Press enter to ccontinue.")

while len(times)<5:
    start=t.time()
    word=input("Type the given word: ")
    end=t.time()
    time_elapsed=end-start

    times.append(time_elapsed)

    if (word.lower()!= "programming"):
        mistakes += 1


print("You made",str(mistakes),"mistake(s)")
print("Okay!Now let's see your evolution chart.")

t.sleep(5)

x=[1,2,3,4,5]
y=times

plt.plot(x,y)
legends=["1","2","3","4","5"]
plt.xticks(x,legends)
plt.ylabel("Time in seconds")
plt.xlabel("Attempts")
plt.title("Typing Evolution")

plt.show()


