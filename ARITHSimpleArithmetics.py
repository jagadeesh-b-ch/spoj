def print_arithmetic_exp(num_one, num_two, symbol):
    num_one_blank_spaces = len(num_two) - len(num_one) + 1
    if num_one_blank_spaces < 0:
        num_one_blank_spaces = 0
    print((" " * num_one_blank_spaces) + num_one)
    num_two_blank_spaces = len(num_one) - len(num_two) - 1
    if num_two_blank_spaces < 0:
        num_two_blank_spaces = 0
    print((" " * num_two_blank_spaces) + symbol + num_two)
    if num_one_blank_spaces > num_two_blank_spaces:
        print("-"*(num_one_blank_spaces + len(num_one)))
        return num_one_blank_spaces + len(num_one)
    else:
        print("-"*(num_two_blank_spaces + len(num_two) + 1))
        return num_two_blank_spaces + len(num_two) + 1


def add(num_one, num_two):
    max_length_in_line = print_arithmetic_exp(num_one, num_two, "+")
    addition = str(int(num_one) + int(num_two))
    print(" "*(max_length_in_line - len(addition)) + addition)


def subtract(num_one, num_two):
    print_arithmetic_exp(num_one, num_two, "-")


def multiply(num_one, num_two):
    print_arithmetic_exp(num_one, num_two, "*")


def perform_arithmetic_operation(expression):
    numbers = expression.split("+")
    if len(numbers) == 1:
        numbers = expression.split("-")
        if len(numbers) == 1:
            numbers = expression.split("*")
            if len(numbers) == 1:
                print("wrong input")
            else:
                multiply(numbers[0], numbers[1])
        else:
            subtract(numbers[0], numbers[1])
    else:
        add(numbers[0], numbers[1])


for i in range(int(input())):
    perform_arithmetic_operation(input())
