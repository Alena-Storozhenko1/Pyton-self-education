print('Привет, я Алена и это моё ДЗ')


print('1. уровень')


print('1) Пользователь вводит число а и число b. Возвести а в степень b')



a = int(input("Введите число: "))
b = int(input("Введите степень: "))
print(a ** b)

print('2) Пользователь вводит 2 числа. Вывести наибольшее из них')



num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число:"))
if num1 > num2:
    print("Наибольшее число:", num1)
else:
    print("Наибольшее число:", num2)

print('3) Пользователь вводит сумму в гривне и курс доллара. Нужно пересчитать сумму в долларе')



sum_hryvnia = float(input("Введите сумму в гривнах: "))
rate_dollar = float(input("Введите курс доллара: "))
sum_dollar = sum_hryvnia / rate_dollar
print("Сумма в долларах:", sum_dollar)

print('4) Пользователь вводит цифру от 1 до 7, нужно вывести соотвествующий день недели')



day_num = int(input("Введите номер дня недели (от 1 до 7): "))
if day_num == 1:
    print("Понедельник")
elif day_num == 2:
    print("Вторник")
elif day_num == 3:
    print("Среда")
elif day_num == 4:
    print("Четверг")
elif day_num == 5:
    print("Пятница")
elif day_num == 6:
    print("Суббота")
elif day_num == 7:
    print("Воскресенье")
else:
    print("Ошибка! Номер дня недели должен быть от 1 до 7.")



print('2. уровень')

print('1) Пользователь вводит число. Если оно четное, вывести "четное". Если оно нечетное, вывести "нечетное"')



num = int(input("Введите число: "))
if num % 2 == 0:
    print("Четное")
else:
    print("Нечетное")


print('2) Пользователь вводит 3 числа. Вывести наименьшее из них')




num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("введите третье число: "))

if num1 < num2 and num1 < num3:
    print("Наименьшее число", num1)
elif num2 < num1 and num2 < num3:
    print("Наименьшее число", num2)
else:
    print("Наименьшее число", num3)

print('3) Из Убудского чата Аня узнала, что рекомендуется спать хотя бы А часов в сутки,')
print('но пересыпать тоже вредно и не стоит спать более В часов.')
print('Сейчас Аня спит Н часов в сутки.')
print('Если режим сна Ани удовлетворяет рекомендациям Сергея, выведите "Это нормально".')
print('Если Аня спит менее А часов, выведите "Недосып",')
print('если же более В часов, то выведите "Пересып" Получаемое число  А всегда меньше либо равно В')
print('(то есть это проверять не надо).')



a = int(input("Введите минимальное рекомендуемое количество часов сна: "))
b = int(input("Введите максимальное рекомендуемое количество часов сна: "))
n = int(input("Введите нормальное количество сна: "))

if n >= a and n <= b:
    print("Это нормально")
elif n < a:
    print("Недосып")
else:
    print("Пересып")


