# Задача 1
# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8



def SumRecursive(x1, x2):
    if x2 > 1:
        return x1 * SumRecursive(x1, x2 - 1)
    elif x2 == 0:
        return 1
    else:
        return x1


a = int(input("A = "))
b = int(input("B = "))

print(f"sum = {pow(a, b)}")