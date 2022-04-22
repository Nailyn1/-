from random import randint
lenght_str = int(input('Введите длину пароля. Пароль должен быть не меньше 6!'))
if lenght_str < 6:
    print('Длина строки меньше 6:(')
else:
    for i in range(7):
        password = ''
        arr = ['%', '*', ')','?', '@', '#', '$', '~']
        for i in range(lenght_str):
            num = 0
            b = randint(ord('a'), ord('z'))
            num = randint(1, 2)
            if num == 2:
                password = password + chr(b).upper()
            a = randint(ord('a'), ord('z'))
            password = password + chr(a) + str(randint(1,10)) + arr[randint(1,7)]
            b = randint(ord('a'), ord('z'))
            if num == 2:
                password = password + chr(b).upper()
        l = len(password)+1
        print(password[0:lenght_str])