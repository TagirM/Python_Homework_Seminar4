# Задача 5.
# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

data1 = open('poly_1.txt', 'r')
data2 = open('poly_2.txt', 'r')
multiX1 = []
for line in data1:
    multiX1 = line
data1.close()
multiX2 = []
for line in data2:
    multiX2 = line
data2.close()
multiX3 = multiX1 + ' + ' + multiX2
data3=open('poly_3.txt','w')
data3.writelines(multiX3)
data3.close()
