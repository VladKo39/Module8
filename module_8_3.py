''''''
'''
Домашнее задание по теме "Создание исключений".
Если вы решали старую версию задачи, проверка будет производиться по ней.
Ссылка на старую версию тут.

Цель: освоить навык создания пользовательских исключений и использовать его в решении задачи. 
Повторить тему ООП и принцип инкапсуляции.

Задача "Некорректность":
Пример результата выполнения программы:
Пример выполняемого кода:
try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')
Вывод на консоль:
Model1 успешно создан
Неверный диапазон для vin номера
Неверная длина номера
Файл module_8_3.py и загрузите его на ваш GitHub репозиторий. В решении пришлите ссылку на него.
'''


class IncorrectVinNumber(Exception):
    '''Свое исключение (Exception), вызов при проверке некорректного заполнения vin_number

    '''

    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    '''Класс Свое исключение(Exception), вызов при проверке некорректного заполнения number'''

    def __init__(self, message):
        self.message = message


class Car:
    ''' Класс Car.
        Объект класса обладает:
        Свойства: model название автомобиля (строка).
                   Уровень доступа public.

                  __vin идентификационный номер автомобиля (целое число, от 1000000 до 9999999 вкл).
                   Уровень доступа private.

                  __numbers номера автомобиля (строка, кол-во знаков 6).
                   Уровень доступа private.

        Методы:   __is_valid_vin проверка __vin. Вызывается при создании объекта (в __init__ при объявлении атрибута __vin).
                   Уровень доступа private.
                   Если __vin не целое число - вызывает исключение (raise IncorrectVinNumber)
                    c сообщением 'Некорректный тип vin номер'.
                   Если __vin за диапазоном от 1000000 до 9999999 вкл - вызывает исключение (raise IncorrectVinNumber)
                    c сообщением 'Неверный диапазон для vin номера'.
                   Если исключение (IncorrectVinNumber) не вызвано, возврат True

                 __is_valid_numbers проверка __numbers. Вызывается при создании объекта
                    (в __init__ при объявлении атрибута __numbers).
                   Уровень доступа private.
                   Если __numbers не строка - вызывает исключение (raise IncorrectCarNumbers)
                    c сообщением 'Некорректный тип данных для номеров'.
                   Если __numbers строка, не содержит кол-во знаков 6 - вызывает исключение (raise IncorrectCarNumbers)
                    c сообщением 'Неверная длина номера'.
                   Если исключение (IncorrectCarNumbers) не вызвано, возврат True.
    '''
    def __init__(self, model: str, vin: int, numbers: str):
        self.model = model
        self.__vin = vin
        self.__is_valid_vin(self.__vin)
        #__is_valid_vin вызывается при создании объекта при объявлении атрибута __vin
        self.__numbers = numbers
        self.__is_valid_numbers(self.__numbers)
        # __is_valid_number вызывается при создании объекта при объявлении атрибута __numbers

    def __is_valid_vin(self, vin_number):
        #проверка __vin>>vin_number
        if not isinstance(vin_number, int):
            #Если __vin>>vin_number не целое число
            raise IncorrectVinNumber('Некорректный тип vin номер')
            #- вызывает исключение (raise IncorrectVinNumber) с сообщением 'Некорректный тип vin номер'.

        elif not 1000000 <= vin_number <= 9999999:
            #Если __vin>>vin_number не в диапазоне от 1000000 до 9999999 вкл
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
            #вызывает исключение (raise IncorrectVinNumber) c сообщением 'Неверный диапазон для vin номера'.
        else:
           #Если исключение (IncorrectVinNumber) не вызвано.
            return True
            #возврат True.
    def __is_valid_numbers(self, numbers):
        # проверка __numbers>>numbers
        if not isinstance(numbers, str):
            # Если __numbers>>number не строка.
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
            # - вызывает исключение (raise IncorrectCarNumbers) с сообщением 'Некорректный тип данных для номеров'.
        elif len(numbers) != 6:
            # Если __numbers>>number кол-во знаков не равно 6.
            raise IncorrectCarNumbers('Неверная длина номера')
            # - вызывает исключение (raise IncorrectCarNumbers) с сообщением 'Неверная длина номера'.
        else:
            # Если исключение (IncorrectCarNumbers) не вызвано.
            return True
            # возврат True.

try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
