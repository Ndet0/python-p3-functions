#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")


def greet(name):
    print(f"Hello, {name}!")


def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")


def add(num1, num2):
    return num1 + num2


def halve(number):
    if isinstance(number, int) or isinstance(number, float):
        return number / 2


if __name__ == "__main__":
    greet_programmer()
    greet("Guido")
    greet_with_default()
    add(45, 55)
    # number = int(input("Enter a number to halve: "))
    halve(99)