def print_params(a= 1, b= "Строка", c= True):
    print(a, b, c)

print_params()
print_params(10)
print_params(10, "Програмист")
print_params(b= 25)
print_params(c=[1, 2, 3])


values_list = [42, 'example', False]
values_dict = {'a': 3.14, 'b': 'hello', 'c': None}

print_params(*values_list)
print_params(**values_dict)


values_list2 = [54.32, 'Строка']
print_params(*values_list2, 42)