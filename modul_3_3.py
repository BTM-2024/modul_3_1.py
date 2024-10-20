# Практическая работа "Распаковка позиционных параметров"
# Задача "Распаковка"
def print_params(a=1, b="строка", c=True):
    print(a, b, c)

b=25    # пункт №1
c=[1, 2, 3]
print_params()
print_params(1, b, c)
print_params(b, c)
print_params(* c)

values_list = [1, 1.2, 'Urban'] # пункт №2
values_dict = {'a': 1, 'b': 'строка', 'c': True}
print_params(*values_list)
print_params(**values_dict)

values_list_2=[54.32, 'Строка'] # пункт №3
print_params(*values_list_2,42)