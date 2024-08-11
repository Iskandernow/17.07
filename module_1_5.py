immutable_var = 1, 2, 2, 'banana', True
print(immutable_var)
#immutable_var[0] = 23
print(immutable_var)
# Кортеж нельзя изменить так как он является неизменяемым объектом. Используется реже списка. В основном для вывода какого-то списка который должен остаться неизменным. Плюс он занимает меньше памяти.
mutable_list = [ 6, 19, 'g', 'Y', 'Job']
mutable_list[0] = 47
print(mutable_list)
