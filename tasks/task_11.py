number = int(input('Введите четырехзначное число:'))

thousands = number // 1000
hundreds = number % 1000 // 100
tens = number % 100 // 10
units = number % 10

print("Цифра в позиции тысяч:", thousands)
print("Цифра в позиции сотен:", hundreds)  # Ваш код
print("Цифра в позиции \nдесятков:", tens)  # Ваш код
print("Цифра в позиции единиц:\n", units)