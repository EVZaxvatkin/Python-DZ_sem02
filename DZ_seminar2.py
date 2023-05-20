#import fractions


#1. Напишите программу, которая получает целое число и возвращает
#его шестнадцатеричное строковое представление.
#Функцию hex используйте для проверки своего результата.


#n = int(input("Введите целое число: "))
#h = (format(n, '#x'))

#print('Шестнадцатеричное строковое представление числа "n" = ' + h)

#if h == hex(n):
#    print("Проверка пройдена")

#else:
#    print("Проверка не пройдена")



#2. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
#Программа должна возвращать сумму и произведение* дробей.
#Для проверки своего кода используйте модуль fractions.

#a1: str = str(input("Введите числитель первой дроби "))
#b1: str = str(input("Введите знаменатель первой дроби "))
#a2: str = str(input("Введите числитель второй дроби "))
#b2: str = str(input("Введите знаменатель второй дроби "))
#number1: int = int(a1)
#number2: int = int(b1)
#number3: int = int(a2)
#number4: int = int(b2)


#result1 = (number1 / number2 ) + (number3 / number4)
#result2 = (number1 / number2 ) * (number3 / number4)
#print(result1)
#print(result2)
#firstfraction = fractions.Fraction(number1, number2)
#secondfraction = fractions.Fraction(number3, number4)
#result3 = firstfraction + secondfraction
#result4 = firstfraction * secondfraction
#print(result3)
#print(result4)

