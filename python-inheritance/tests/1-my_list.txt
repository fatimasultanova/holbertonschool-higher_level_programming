#!/usr/bin/python3
>>> MyList = __import__('1-my_list').MyList

>>> my_list = MyList()
>>> my_list.append(1)
>>> my_list.append(4)
>>> my_list.append(2)
>>> my_list.append(3)
>>> my_list.append(5)

>>> print(my_list)
[1, 4, 2, 3, 5]

>>> my_list.print_sorted()
[1, 2, 3, 4, 5]

>>> print(my_list)
[1, 4, 2, 3, 5]

>>> empty_list = MyList()
>>> empty_list.print_sorted()
[]

>>> single_list = MyList([10])
>>> single_list.print_sorted()
[10]

>>> dup_list = MyList([5, 2, 5, 1, 2])
>>> dup_list.print_sorted()
[1, 2, 2, 5, 5]

>>> neg_list = MyList([0, -5, 10, -2, 3])
>>> neg_list.print_sorted()
[-5, -2, 0, 3, 10]

>>> sorted_list = MyList([1, 2, 3])
>>> sorted_list.print_sorted()
[1, 2, 3]

>>> big_list = MyList([1000, 5, 500])
>>> big_list.print_sorted()
[5, 500, 1000]
