def print_params(a = 1, b = 'строка', c = True):
 print(a, b, c)
print_params()
print_params(1, 25, True)
print_params(1, 'строка', [1,2,3])
# print_params(a, b, c)

values_list = 21, False, 'яма'
values_dict = {'Alex': 1, 'Bob': 'строка', 'Den': True}
print_params(*values_list)
print_params(*values_dict)
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
