#!/usr/bin/env python3
'''Lab 3 Part 1 script - functions'''
#Author ID: ahassanzadeh-langrud

def sum_numbers(number1, number2):
    return int(number1) + int(number2)

def subtract_numbers(number1, number2):
    return int(number1) - int(number2)

def multiply_numbers(number1, number2):
    return int(number1) * int(number2)

if __name__ == '__main__':
    print(int(sum_numbers(10, 5)))
    print(int (subtract_numbers(10, 5)))
    print(int(multiply_numbers(10, 5)))
