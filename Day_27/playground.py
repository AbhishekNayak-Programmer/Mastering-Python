def add(*args):
    total = 0
    for num in args:
        total += num
    print(f'Sum is {total}')


add(1,2,3,4)

def calculate(n, **kwargs) :
    # print(kwargs)
    # for key,value in kwargs.items():
    #     print(key, value)
    n += kwargs["add"]
    print(n)
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

# Creating a Class with Dynamic Arguments
class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")

my_car = Car(make='BMW', model="GT-R")
print(my_car.model)