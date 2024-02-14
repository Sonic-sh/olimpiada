import csv

with open('vacancy.csv', encoding='utf8') as file:
    file = list(csv.DictReader(file, delimiter=';', quotechar='"'))
    #открываем файл
while True:
    in_put = input()
    #запрашиваем у пользователя название фирмы
    if in_put == "None":
        break
    for i in file:
        if i['Company'] == in_put:
            print(f'В {in_put} найдена вакансия: {i['Role']}. З/п составит:{i['\ufeffSalary']}')
    else:
        print('К сожалению, ничего не удалось найти')
    #прописываем условия если найдена фирма, не найдена и стоп-слова