from collections import deque

hex_1 = deque(input('Введите первое шестнадцатиричное число: ').upper())
hex_2 = deque(input('Введите второе шестнадцатиричное число: ').upper())
hex_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
if len(hex_1) > len(hex_2):
    hex_1, hex_2 = hex_2, hex_1
hex_1.reverse()
hex_2.reverse()
hex_result = deque()
j, k = 0, 0
for i in hex_2:
    dex_1 = hex_list.index(i)
    dex_2 = hex_list.index(hex_1[j])
    hex_result.append(hex_list[(dex_1 + dex_2 + k) % 16])
    if (dex_1 + dex_2) >= 15:
        k = 1
    else:
        k = 0
    j += 1
    if j == len(hex_1):
        break
remainder = len(hex_2) - len(hex_1)
if remainder:
    for _ in range(remainder):
        hex_result.append(hex_list[(hex_list.index(hex_2[-remainder]) + k) % 16])
        if hex_list.index(hex_2[-remainder]) + 1 >= 15:
            k = 1
        else:
            k = 0
if k == 1:
    hex_result.append('1')
hex_result.reverse()
print(hex_result)
