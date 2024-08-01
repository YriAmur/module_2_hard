def password(a):
    password = ''

    for i in range(1, 21):
        for j in range(i + 1, 21):
            if a % (i +j) == 0:
                password += str(i) + str(j)
    return password

number = int(input('Введите чмсло от 3 до 20: '))

print(password(number))



