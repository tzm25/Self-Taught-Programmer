


def fahr2celcius(fahr):
    celcius=(5 * (fahr-32))/9
    return celcius
print("Celcius: ", round(fahr2celcius(100),2))
print("Kelvin: ", round((fahr2celcius(100)+273),2))

def say_hello(person1, person2):
    print("Hello", person1 , "where have you been?", person2, "is waiting for you.")


say_hello("John","Anna")
say_hello("Mary","Louis")
say_hello("Arthur","Olympia")
