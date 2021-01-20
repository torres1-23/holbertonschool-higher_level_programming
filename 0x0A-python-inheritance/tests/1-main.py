#!/usr/bin/python3
MyList = __import__('1-my_list').MyList

my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
print(my_list)
my_list.print_sorted()
print(my_list)
my_list = MyList()
print(type(my_list))
print(my_list)
my_list = MyList()
my_list.append("Alejo")
my_list.append("Torres")
my_list.append("Holberton")
print(my_list)
print(my_list.print_sorted())
del my_list
print(my_list)
