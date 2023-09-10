a: int = int(input('Введите число a: '))
b: int = int(input('Введите число b: '))

a, b = b, a

# ----------------------

# temp = a
# a = b
# b = temp

print("Значения после перестановки:")
print('a =', a, '\nb =', b)
