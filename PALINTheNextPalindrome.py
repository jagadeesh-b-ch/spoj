from math import floor


def add_digit_to_num_in_string_format_at_pos(num_in_list_format, number_to_add, pos):
    while True:
        remainder = number_to_add % 10
        carry_over = floor(number_to_add / 10)
        number_to_add = int(num_in_list_format[pos]) + remainder
        num_in_list_format[pos] = str(number_to_add % 10)
        carry_over = carry_over + floor(number_to_add / 10)
        if carry_over == 0:
            break
        pos = pos - 1
        if pos >= 0:
            number_to_add = carry_over
        else:
            break
    if carry_over > 0:
        num_in_list_format = [str(carry_over)] + num_in_list_format
    return num_in_list_format


def find_next_smallest_palindrome(num_in_string_format):
    start, end = 0, len(num_in_string_format) - 1
    num_in_list_format = add_digit_to_num_in_string_format_at_pos(list(num_in_string_format), 1, end)
    start, end = 0, len(num_in_list_format) - 1
    while start < end:
        start_digit = int(num_in_list_format[start])
        end_digit = int(num_in_list_format[end])
        if start_digit < end_digit:
            num_to_add = 10 + int(start_digit) - int(end_digit)
            num_in_list_format = add_digit_to_num_in_string_format_at_pos(num_in_list_format, num_to_add, end)
        elif start_digit > end_digit:
            num_to_add = start_digit - end_digit
            num_in_list_format = add_digit_to_num_in_string_format_at_pos(num_in_list_format, num_to_add, end)
        start = start + 1
        end = end - 1
    start, end = 0, len(num_in_list_format) - 1
    while start < end:
        num_in_list_format[end] = num_in_list_format[start]
        start = start + 1
        end = end - 1
    print("".join(num_in_list_format))


for i in range(int(input())):
    find_next_smallest_palindrome(input())
