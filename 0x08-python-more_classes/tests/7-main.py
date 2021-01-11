#!/usr/bin/python3
Rectangle = __import__('7-rectangle').Rectangle

my_rectangle_1 = Rectangle(8, 4)
print(my_rectangle_1)
print("--")
my_rectangle_1.print_symbol = "&"
my_rectangle_1.number_of_instances = 5
print(my_rectangle_1)
print("--")
print(Rectangle.number_of_instances)
print(my_rectangle_1.number_of_instances)
my_rectangle_2 = Rectangle(2, 1)
print(my_rectangle_2)
print("--")
Rectangle.print_symbol = "C"
print(my_rectangle_2)
print("--")
print(Rectangle.number_of_instances)
my_rectangle_3 = Rectangle(7, 3)
print(my_rectangle_3)

print("--")

my_rectangle_3.print_symbol = ["C", "is", "fun!"]
print(my_rectangle_3)

print("--")

my_rectangle_4 = Rectangle(1, 2)
print(my_rectangle_4)
