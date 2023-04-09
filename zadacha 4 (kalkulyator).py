while True:
    print ("Какое действие вы хотели бы выполнить? Введите не обходимый знак:")
    operator = input()
    if operator == ("+"):
        print ("Введите первое слагаемое:")
        ch1 = float(input())
        print("Введите второе слагаемое:")
        ch2 = float(input())
        print("Результат выполнения поставленной задачи: ", ch1 + ch2)
        break
    elif operator == ("-"):
        print("Введите уменьшаемое:")
        ch1 = float(input())
        print("Введите вычитаемое:")
        ch2 = float(input())
        print("Результат выполнения поставленной задачи: ", ch1 - ch2)
        break
    elif operator == ("/"):
        print("Введите делимое:")
        ch1 = float(input())
        print("Введите делитель:")
        ch2 = float(input())
        print("Результат выполнения поставленной задачи: ", ch1 // ch2,",",ch1 % ch2)
        break
    elif operator == ("*"):
        print("Введите первый множитель:")
        ch1 = float(input())
        print("Введите второй множитель:")
        ch2 = float(input())
        print("Результат выполнения поставленной задачи: ", ch1 * ch2)
        break
    elif operator == ("^"):
        print("Введите число, возводимое в степень:")
        ch1 = float(input())
        print("Введите показатель степени:")
        ch2 = float(input())
        print("Результат выполнения поставленной задачи: ", ch1 ** ch2)
        break
    elif operator == ("abs"):
        print("Введите число, модуль которого необходимо узнать:")
        ch1 = float(input())
        print("Результат выполнения поставленной задачи: ", abs(ch1))
        break
    elif operator == ("random"):
        import random
        print("Введите левую границу диапазона:")
        ch1 = float(input())
        print("Введите правую границу диапазона:")
        ch2 = float(input())
        if input("Случайное число должно быть целым или вещественным? (ц/в) - ") == ("ц"):
            print("Результат выполнения поставленной задачи: ", random.randint(ch1, ch2))
        else:
            print ("Результат выполнения поставленной задачи: ",random.uniform(ch1, ch2))
        break
    elif operator == ("!"):
        import math
        print("Введите число:")
        ch1 = int(input())
        print("Результат выполнения поставленной задачи: ", math.factorial(ch1))
        break
    elif operator == ("arccos"):
        import math
        print("Введите число:")
        ch1 = float(input())
        if (ch1 < -1) or (ch1 > 1):
            print ("Такого арккосинуса не существует! Введите число в диапазоне от -1 до 1")
        else:
            print("Результат выполнения поставленной задачи: ", math.acos (ch1))
        break
    else:
        print ("Я пока не умею выполнять такие действия( Но меня обязательно улучшат в ближайшем будущем, честно-честно!")
    if input("Хотели бы посчитать ещё что-нибудь? Да/Нет - ") == ("Нет"):
        break
