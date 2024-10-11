''''''
'''
Домашнее задание по уроку "Try и Except".

Задание "Программистам всё можно":
Реализуйте следующую функцию:
add_everything_up, будет складывать числа(int, float) и строки(str)

Пример кода:
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

Вывод в консоль:
123.456строка
яблоко4215
130.456
'''


def add_everything_up(a, b):
    ''''''
    '''add_everything_up, будет складывать числа(int, float) и строки(str)'''
    __q_ty_error = 0
    # число допущенных ошибок
    try:
        '''проверка блока кода на ошибки.'''
        everything = a + b
    except (TypeError) as exc:
        '''обработка ошибки в блоке. Если a или b не является числом, возвращать
        данные как строковое представление вместе'''
        __q_ty_error += 1
        print(F'Необходимо проверить тип данных {TypeError}  {exc}')
        everything = str(a) + str(b)

    else:
        '''обработка кода при отсутствии ошибки. Складываем а и b.
           Округление до 3 разряда'''
        everything = round(a + b, 3)

    finally:
        '''Действие завершения при любом результате'''
        if __q_ty_error == 0:
            print(f'Обработка данных завершена.Ошибок нет')
        else:
            # print(int(str(a)[-1]) == 3)
            if int(str(__q_ty_error)[-1]) == 0 or 9 >= int(str(__q_ty_error)[-1]) >= 5:
                strok = 'ошибок'
            elif int(str(__q_ty_error)[-1]) == 1:
                strok = 'ошибка'
            else:
                strok = 'ошибки'
            print(f'Обработка данных завершена. Обнаружено {__q_ty_error} {strok}')
    return everything


print(f'{"*" * 3} Вывод результата {"*" * 15}\n')
print(add_everything_up(123.456, 'строка'))
print()
print(add_everything_up('яблоко', 4215))
print()
print(add_everything_up(123.456, 7))
