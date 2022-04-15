from collections import defaultdict

count_firms = int(input('Введите количество компаний: '))
QUARTER = 4
all_profit = 0
avg_profit = 0
rating = [[], []]
firm = defaultdict(int)
for i in range(count_firms):
    name = input('Введите имя компании: ')
    for j in range(1, QUARTER + 1):
        firm[name] = firm.get(name, 0) + int(input(f'Введите доход компании {name} за {j} квартал: '))
for i in firm.values():
    all_profit += i
avg_profit = all_profit / count_firms
print(f'Средний доход всех предприятий: {avg_profit}')
for company, income in firm.items():
    if income > avg_profit:
        rating[0].append(company)
    if income < avg_profit:
        rating[1].append(company)
print('Прибыль выше среднего у следующих предприятий:')
print(*rating[0])
print('-' * 46)
print('Прибыль ниже среднего у следующих предприятий:')
print(*rating[1])
