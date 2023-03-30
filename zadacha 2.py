print ('Введите произвольную строку:')
stroka = input()
lenght = len(stroka)
stroka_bez_3 = ""
print ('Строка без 3-го символа (через срез): ', stroka [:2] + stroka [3:])
for i in range (0, lenght):
    if i != 2:
        stroka_bez_3 = stroka_bez_3 + stroka[i]
    if stroka[i] == "с":
     print('Вау! В введённой строке нашёлся заданный в условии задачи символ! P.S. через цикл')
print ('Строка без 3-го символа (через цикл): ', stroka_bez_3)
simvol = stroka.find("с")
if simvol != -1:
    print('Вау! В введённой строке нашёлся заданный в условии задачи символ! P.S. через find')
print ('Длина введённой строки: ', lenght)
print ('Введённая строка без последнего символа (через срез): ', stroka [0:lenght-1])
