# Завдання 1

while True:
    a = input('Введіть ПІБ: ')
    if a.replace(' ', '').isalpha() and a.istitle():
        print(a)
        break
    else:
        print('Некоректне введення')

# Завдання 2

print('Введіть інтервал чисел!(в інтервалі мае бути не меньше 5 чисел)')
a = int(input('Від якого числа: '))
b = int(input('До якого числа: '))
rez = range(a, b + 1)
print(rez[1] + rez[-2] + sum(rez) / len(rez))

# Завдання 3

while True:
    r = input('Введіть R (цілочисельне значення від 0 до 255): ')
    g = input('Введіть G (цілочисельне значення від 0 до 255): ')
    b = input('Введіть B (цілочисельне значення від 0 до 255): ')
    if r.isdigit() and g.isdigit() and b.isdigit() and int(r) and int(g) and int(b) in range(1, 256):
        my_tuple = (int(r), int(g), int(b))
        print(my_tuple)
        break
    else:
        print('Не вірне значення спробуйте щераз')

# Завдання 4

from collections import namedtuple
from collections import deque
users = deque()
while True:
    alg = input(f"Введіть оцінку по Алгебре: ")
    geom = input(f"Введіть оцінку по Геометрії: ")
    his = input(f"Введіть оцінку по Історії: ")
    inf = input(f"Введіть оцінку по Інформатиці: ")
    geog = input(f"Введіть оцінку по Географії: ")
    Class = namedtuple('Class', 'Algebra Geometry History Information Geography')
    study1 = Class(Algebra=alg, Geometry=geom, History=his, Information=inf, Geography=geog)
    users.append(study1)

    x = input('Чи є щє учні? ')
    if x.lower() == 'ні':
        break
print(*users, sep="\n")

# Завдання 5

a = tuple(map(int, input('Введіть послидовність чисел: ').split()))
print(*sorted(a))

# Завдання 6

n = input('Залиште свій відгук: ')
counter = 0
if len(n) > 60:
    counter += 15
if 'меню' in n:
    counter += 5
if 'спортзал' in n:
    counter += 5
if 'обслуговування' in n:
    counter += 5

print(f'Дякую, на настапний рік у вас буде {counter}% знижки!!!')
