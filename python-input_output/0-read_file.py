#!/usr/bin/python3
def read_file(file_name=''):
    with open(file_name, 'r') as file:
        print(file.read())
