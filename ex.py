class b:
    __a = 10

    def print_a(self):
        print(self.__a)


s = b()
print(s._b__a)
s.print_a()


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


square = Rectangle(5, 5)
print(square.calculate_area())

print('Using @classmethod')


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    @classmethod
    def new_square(cls, side_length):
        return cls(side_length, side_length)


square = Rectangle.new_square(5)
print(square.calculate_area())


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_data(self):
        print(f"name:{self.name} age:{self.age}")

    @classmethod
    def new__dt(cls, d1, d2):
        return cls(d1, d2)


s = Student.new__dt('mub', '21')
s.print_data()


class Juice:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __str__(self):
        return self.name + ' (' + str(self.capacity) + 'L)'

    def __add__(self, other):
        return Juice(self.name + '&' + other.name, self.capacity + other.capacity)


a = Juice('Orange', 1.5)
b = Juice('Apple', 2.0)

result = a + b
print(result)
