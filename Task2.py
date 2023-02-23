# Задача 2
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# 2 2
# 4


def SumRecursive(x1, x2):
    if x1 != 0:
        return SumRecursive(x1 - 1, x2 + 1)
    return b


a = int(input("A = "))
b = int(input("B = "))

print(f"max = {SumRecursive(a, b)}")