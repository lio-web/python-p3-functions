#!/usr/bin/env python3

def my_function(param):
    print("Running my_function")
    return param + 1

# Call the function and assign its return value to a variable

def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

def add(num1, num2):
    return num1 + num2

def halve(number):
    if isinstance(number, (int, float)):
        return number/2
    else:
        return None
