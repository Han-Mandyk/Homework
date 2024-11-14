def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

values_list = ['Dinis', False, 21.3]
values_list_2 = [56.78, 'Appel']
values_dist = {'a' : 32, 'b' : 'tree', 'c' : True}

print_params()
print_params(*values_list)
print_params(*values_list_2, 45)
print_params(**values_dist)