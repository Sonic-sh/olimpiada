import csv
with open('vacancy.csv', encoding='utf8') as file:
    file = list(csv.DictReader(file, delimiter=';', quotechar='"'))
    file = sorted(file, key=lambda x: x['\ufeffSalary'])
for i in range(196, 199):
    print(f'{file[i]['Company']} - {file[i]['Role']} - {file[i]['\ufeffSalary']}')
# 2 и 3 строчки - открытие и считывание файла
# 4 строка - сортировка по возрастанию зарплаты в компаниях