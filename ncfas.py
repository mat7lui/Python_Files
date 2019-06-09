"""
This file is designed to manage the process 
of extracting data from the Evello database 
and processing it into a csv.

Structure of the data:
    1. Each domain is stored in a separate dictionary
    2. Key: STR - "UserID" Value: TUPLE or SET with (Intake, Closure) 
"""

list_thing = [1, 2, 3, 1, 2, 3]
tuple_thing = 1, 2, 3, 1, 2, 3

print(tuple_thing)
set_thing = set(tuple_thing)
print(type(set_thing))
