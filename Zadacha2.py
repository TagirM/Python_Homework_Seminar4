# Задача 2. Задайте натуральное число N. Напишите программу, которая составит список
# простых множителей числа N.
def isfloat(value):
    try:
        int(value)
        return True
    except ValueError:
        return False
numberN = input('Введите целое число: ')
while isfloat(numberN) == False:
    numberN = input('Введите целое число: ')
numberN=int(numberN)
myList = []
for elem in range(2, numberN+1):
    if numberN % elem == 0:
        myList.append(elem)
NewList = []
for i in range(len(myList)):
    if myList[i] % 2 == 0 and myList[i]//2 > 1:
        NewList.append(myList[i]//2)
        NewList.append(2)
    elif myList[i] % 3 == 0 and myList[i]//3 > 1:
        NewList.append(myList[i]//3)
        NewList.append(3)
    else:
        NewList.append(myList[i])
myNumber = 1
myNewList = []
for elem in NewList:
    if numberN % elem == 0:
        myNewList.append(elem)
        numberN = numberN/elem
print(myNewList)
