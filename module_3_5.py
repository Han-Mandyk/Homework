def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])

    if len(str_number) > 1:
       return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

result = get_multiplied_digits(40203)
result_1 = get_multiplied_digits(45093)
result_2 = get_multiplied_digits(50506)
print(result)
print(result_1)
print(result_2)