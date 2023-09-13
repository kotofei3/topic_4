num_switches: int = int(input('Введите количество\nпереключателей:'))  # 1.Исправьте текст-подсказку в input()

combinations: int = 2 ** num_switches

print("Количество возможных комбинаций:", combinations)
