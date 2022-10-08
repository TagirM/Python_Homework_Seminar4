# Задача 4.
# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 10) многочлена и записать в файл полученный многочлен не менее 3х раз.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint


def isint(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


degreeK = input('Введите натуральную степень k: ')
while isint(degreeK) == False:
    degreeK = input('Введите натуральную степень k: ')
degreeK = int(degreeK)
multiX = []
count = 3
data=open('file_for_zadacha4.txt','a')
print("Полученные многочлены:")
while count != 0:
    count -= 1
    oper = degreeK
    for elem in range(degreeK+1):
        A = randint(0, 9)
        if oper == 0 and A!=0:
            multiX.append(A)
            multiX.append(' = 0')
            break
        elif oper == 0 and A == 0:
            multiX.pop()
            multiX.append(' = 0')
            break
        if A > 0:
            multiX.append(A)
            multiX.append('* X ^')
            multiX.append(oper)
            multiX.append(' + ')
        oper -= 1
    data.writelines(''.join(map(str,multiX)))
    data.writelines('\n')
    print(''.join(map(str,multiX)))
    multiX.clear()
data.close()
