def print_params(a=1,b='строка', c=True):
    print(a,b,c)


print_params()
print_params(1)
print_params('Вася',True)
print_params(b = 25)
print_params(c = [1,2,3])
values_list = [2, 'Pit', True]
print_params(*values_list)
values_dist = {'a':1, 'b': 'Вася', 'c': True}
print_params(**values_dist)
values_list = [2]
values_dist = {'b': 'Вася','c': True}
print_params(*values_list, **values_dist)
values_list_2 = [2.32, "'Вася'"]
print_params(*values_list_2,42)
