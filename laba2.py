dictionary = {"А":"11", "Б":"12", "В":"13",
    "Г":"14", "Д":"15", "Е":"16", "Ё":"21",
    "Ж":"22", "З":"23", "И":"24","Й":"25",
    "К":"26", "Л":"31", "М":"32", "Н":"33",
    "О":"34", "П":"35", "Р":"36", "С":"41",
    "Т":"42", "У":"43", "Ф":"44", "Х":"45",
    "Ц":"46", "Ч":"51", "Ш":"52", "Щ":"53",
    "Ъ":"54", "Ы":"55", "Ь":"56", "Э":"61",
    "Ю":"62", "Я":"63"}
choice = int(input('1 - Шифровать, 2 - Дешифровать'))
if choice == 1:
    word = input('Введите слово, которое хотите зашифровать').upper()
    new_numbers = ''
    for i in word:
        if i in dictionary:
            new_numbers += dictionary.get(i)
    print('Зашифрованный текст:', new_numbers)

elif choice == 2:
    list_numbers = []
    new_txt = ''
    numbers = input('Введите зашифрованный текст')
    step = 2
    for i in range(0, len(numbers), 2):
        list_numbers.append(numbers[i:step])
        step += 2


    list_keys = list(dictionary.keys())
    list_values = list(dictionary.values())

    for i in list_numbers:
        if i in list_values:
            g = list_values.index(i)
            new_txt += list_keys[g]
        else:
            new_txt += i[0:1]
    print(new_txt)