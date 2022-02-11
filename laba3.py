alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
m = 4096*4
y_list = [0]*8
y_list[0] = 20475
y_list[1] = 4091
stroka = input('Введите строку').upper()
stroka_num_str =[]
stroka_num = []
shif_stroka = []
deshif_stroka = []
for i in range(1,len(stroka)):
    y_list[i] = (y_list[i-1] + y_list[i-2]) % m
print(y_list)

for i in stroka:
    stroka_num_str.append(alphabet.index(i)+1)


for i in range(len(stroka_num_str)):
    stroka_num.append((y_list[i] + stroka_num_str[i])%len(alphabet))


for i in stroka_num:
    shif_stroka.append(alphabet[i])

stroka2 = ''.join(shif_stroka)
print(stroka2)
stroka_num_str_deshif = []
stroka_num_deshif = []
for i in stroka2:
    stroka_num_str_deshif.append(alphabet.index(i))


for i in range(len(stroka_num_str_deshif)):
    stroka_num_deshif.append((stroka_num_str_deshif[i]+33 - y_list[i])%len(alphabet))

for i in stroka_num_deshif:
    deshif_stroka.append(alphabet[i-1])
print(''.join(deshif_stroka))