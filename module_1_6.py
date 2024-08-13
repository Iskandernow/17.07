my_dict = {'Alex': 1987, 'Olga': 1988}
print(my_dict)
print(my_dict['Alex'])
my_dict['Anton'] = 1990
my_dict.update({'Vitaly': 1962,
                'Anna': 1960})
del my_dict['Olga']
print(my_dict.get('Olga'))
print(my_dict)
my_set = {1, 2, 7, 9, 2, 9, 'button', True, (18, 5, 6)}
print(my_set)
print(my_set.add(3))
print(my_set.add(63))
print(my_set)
print(my_set.remove(2))
print(my_set)