# Задача 1. Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141.
def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
number = input('Введите вещественное число: ')
while isfloat(number) == False:
    number = input('Введите вещественное число: ')
exactNumber = float(input('Укажите точность числа: '))
programExact=exactNumber
count = 0
while programExact < 1:
    count += 1
    programExact *= 10
print(f'Число с заданной точностью {exactNumber} равно {round(float(number), count)}')