print("Alameen")
print(18)
print(
    "I MUST BUILD GOOD PROJECT  AND BE ABLE TO PROVE WHAT I BUILT AS A SOFTWARE ENGINEER"
)

name = "Alameen"
age = 16
price = 30, 000
is_available = True
print(name)
print(age)
print(price)
print(is_available)

my_favourite = " I love coding "
print(my_favourite.upper())
print(len(my_favourite))
print(my_favourite.strip())

name = "khaira"
age = 12
score = 57
print(f"{name} you are {age} years old,you scored {score}very good keep it up")

bag = 2500
amount = 4
discount = 1000
total = bag * amount - discount
print(total)

enter = input("Enter your name: ")
age = int(input("Enter your age: "))
next_year = age + 1
print(
    f"your name is {enter}, your current age is {age}.next year you would be {next_year}"
)

student = input("Enter your name: ")
score = int(input("Enter your score: "))

if score >= 80:
    print(f"{student} your score is {score}, your grade is excellent")
elif score >= 50:
    print(f"{student} your score is {score}, So your grade is pass")
else:
    print("you failed")

students = []
students.append("musa")
students.append("khairah")
students.append("alameen")

lists = [5, 4, 3, 2, 1]
print(50 in lists)
print(lists[::-1])


student = ["cat", "dog", "goat", "bat"]
for item in student:
    print(item)
for item in range(1, 11):
    print(item)


def average(a, b, c):
    return a + b + c / 3


answer = average(9, 5, 4)
print(answer)


def add_all(*numbers):
    return sum(numbers)


print(add_all(5, 7, 8))

product = {"name": "samsung", "price": 150000, "quantity": 3}

print(product["name"])
total = product["price"] * product["quantity"]
print(total)

try:
    age = int(input("enter age: "))
    print(age)

except ValueError:
    print("Enter a number not a letter")

layer = 2


def another():
    global layer
    layer += 2


another()
print(layer)


class Car:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand


car1 = Car("camry", "toyota")
car2 = Car("sharan", "giwagon")

print(car1.name)
print(car2.name)


class Student:
    school = "fajr center"

    def __init__(self, name, age, score, prefect):
        self.name = name
        self.age = age
        self.score = score
        self.prefect = prefect

    def statement(self):
        print(
            f"{self.name}  you are {self.age} years old .You are a student of {self.school} .In your last assesment your score was {self.score}. You are also the  {self.prefect} prefect "
        )


student1 = Student("Alameen", 18, 87, "asseembly")
student2 = Student("muiz", 15, 78, "room")
student3 = Student("lukman", 19, 64, "dinning")
student4 = Student("ashafa", 20, 90, "kitchen")

student1.statement()
student2.statement()
student3.statement()
student4.statement()


class School:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def welcome():
        return "welcome to our school"


print(School.welcome())


class Product:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Product: {self. name}"


product1 = Product("samsung")
print(product1)


class Animal:
    def speak(self):
        print("Animals make sounds.")


class Cat(Animal):
    pass


cat1 = Cat()

cat1.speak()


class Person:
    school = "fajr center"

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"my name is {self.name}")


class Student(Person):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def introduce(self):
        print(
            f"i am {self.name} i am a student of  {self.school}  and i am alkso {self.age} years old"
        )


student1 = Student("alameen", 22)

student1.introduce()


class Writer:
    def write(self):
        print("i am the writer of different books")


class Singer:
    def sing(self):
        print("i am a singer")


class Artist(Writer, Singer):
    pass


artist1 = Artist()
artist1.write()
artist1.sing()


try:
    age = int(input("enter ur first number: "))
    print(f"ur first number is {age}")
    second = int(input("enter ur second number: "))
    print(f"ur second number is {second}")
    total = age / second
    print(f"your total is {total}")
except ValueError:
    print("enter a valid number")

except ZeroDivisionError:
    print(" you can't divide by zero")

numbers = [2, 4, 6, 8, 10]

only = [number * 3 for number in numbers]
print(only)

names = ["Alameen", "Ahmad", "Yusuf"]

any = {name: len(name) for name in names}
print(any)
