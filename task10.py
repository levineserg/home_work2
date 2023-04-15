# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
#
# Пример
# 5 -> 1 0 1 1 0
# 2

n = int(input("Ведите количество монет: "))
cur_obverse = 0
cur_reverse = 0
for i in range(n):
    coin_temp = int(input())
    if coin_temp > 0:
        cur_obverse += 1
    else:
        cur_reverse += 1
if cur_obverse > cur_reverse:
    print(cur_reverse)
else:
    print(cur_obverse)
