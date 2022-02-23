dictionary = {"А":"11", "Б":"12", "В":"13",
    "Г":"14", "Д":"15", "Е":"16", "Ё":"21",
    "Ж":"22", "З":"23", "И":"24","Й":"25",
    "К":"26", "Л":"31", "М":"32", "Н":"33",
    "О":"34", "П":"35", "Р":"36", "С":"41",
    "Т":"42", "У":"43", "Ф":"44", "Х":"45",
    "Ц":"46", "Ч":"51", "Ш":"52", "Щ":"53",
    "Ъ":"54", "Ы":"55", "Ь":"56", "Э":"61",
    "Ю":"62", "Я":"63"}

key = '3143143143143143143'

text = "Привет всем"
l = len(text) + 1
part_1 = text[0:l//2].upper()
part_2 = text[l//2:].upper()
print(part_1, part_2)
new_numbers = ''
for i in part_1:
    if i in dictionary:
        new_numbers += dictionary.get(i)


indexenc = []
finallyenc = []
for i in range(len(part_2)):
    enc = ord(part_2[i]) + int(key[i])
    indexenc.append(enc)
for i in range(len(part_2)):
    encfin = chr(indexenc[i])
    finallyenc.append(encfin)
print(new_numbers + ''.join(finallyenc))

list_numbers = []
new_txt = ''
step = 2
for i in range(0, len(new_numbers), 2):
    list_numbers.append(new_numbers[i:step])
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

indexenc2 = []
finallyenc2 = []
strfinallyenc = ''.join(finallyenc)
print(strfinallyenc)
for i in range(len(strfinallyenc)):
    enc = ord(strfinallyenc[i]) - int(key[i])
    indexenc2.append(enc)
for i in range(len(strfinallyenc)):
    encfin = chr(indexenc2[i])
    finallyenc2.append(encfin)
print(new_txt+''.join(finallyenc2))