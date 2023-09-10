num_chicken = int(input('Введите количество курочек:'))
num_cows = int(input('Введите количество коровок:'))
num_pigs = int(input('Введите количество свинок:'))

total_legs = num_chicken * 2 + num_cows * 4 + num_pigs * 4

print("Общее количество ног на ферме:\n", total_legs)
