# Модуль_3_5.Задача "Рекурсивное умножение цифр" по уроку "Рекурсия"
def get_multiplied_digits(number):
    str_number = str(number)                    # переводит число в строку
    str_number.replace('0', '')     # убирает нули из строки
    first = int(str_number[0])                  # отделяет первую цифру в числе
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))   # возвращает произведение натуральных чисел
                                                                    # заданного числа
    else:
        return first


result = get_multiplied_digits(40203)
print(result)