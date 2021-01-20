# 0x0A. Python - Inheritance
>These are the files used for solving different tasks involving inheritance in Python.
## Tests :heavy_check_mark::
All main files used to test the functions are located in the [tests](./tests) folder, each file name is preceeded with the number of each task (i.e for task 0 the main file is [0-main.py](./tests/0-main.py)).
## Tasks :page_with_curl::
### Mandatory:
  * **0. Lookup:**\
    Write a function that returns the list of available attributes and methods of an object.
    * Files:
        * **[0-lookup.py](./0-lookup.py)**
  * **1. My list:**\
    Write a class MyList that inherits from list, methods:
    * def print_sorted(self): prints the list, but sorted.
    * Files:
        * **[1-my_list.py](1-my_list.py)**
        * **[tests/1-my_list.txt](./tests/1-my_list.txt)**
  * **2. Exact same object:**\
    Function that returns True if the object is exactly an instance of the specified class; otherwise False.
    * Files:
        * **[2-is_same_class.py](./2-is_same_class.py)**
  * **3. Same class or inherit from:**\
    Function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from the specified class; otherwise False.
    * Files:
        * **[3-is_kind_of_class.py](./3-is_kind_of_class.py)**
  * **4. Only sub class of:**\
    Function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise False.
    * Files:
        * **[4-inherits_from.py](./4-inherits_from.py)**
  * **5. Geometry module:**\
    Write an empty class BaseGeometry.
    * Files:
        * **[5-base_geometry.py](./5-base_geometry.py)**
  * **6. Improve Geometry:**\
    Write a class BaseGeometry (based on 5-base_geometry.py), methods:
    * def area(self): that raises an Exception.
    * Files:
        * **[5-base_geometry.py](./5-base_geometry.py)**
  * **7. Integer validator:**\
    Write a class BaseGeometry (based on 6-base_geometry.py), methods:
    * def area(self): that raises an Exception.
    * def integer_validator(self, name, value): validates value.
    * Files:
        * **[7-base_geometry.py](./7-base_geometry.py)**
        * **[tests/7-base_geometry.txt](./tests/7-base_geometry.txt)**
  * **8. Rectangle:**\
    Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py), methods:
    * def __init__(self, width, height): instanciate with attributes width and height.
    * Files:
        * **[8-rectangle.py](./8-rectangle.py)**
  * **9. Full rectangle:**\
    Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py), methods:
    * def __init__(self, width, height): instanciate with attributes width and height.
    * def __str__(self):string representation of Rectangle.
    * Files:
        * **[9-rectangle.py](./9-rectangle.py)**
  * **10. Square #1:**\
    Write a class Square that inherits from Rectangle (9-rectangle.py), methods:
    * def __init__(self, size): instanciate with attributes size.
    * Files:
        * **[10-square.py](./10-square.py)**
  * **11. Square #2:**\
    Write a class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py), methods:
    * def __init__(self, size): instanciate with attributes size.
    * Files:
        * **[11-square.py](./11-square.py)**
### Advanced:
  * **12. My integer:**\
    Write a class MyInt that inherits from int
    * Files:
        * **[100-my_int.py](./100-my_int.py)**
  * **13. Can I?**\
    Write a function that adds a new attribute to an object if it’s possible.
    * Files:
        * **[101-add_attribute.py](./101-add_attribute.py)**
