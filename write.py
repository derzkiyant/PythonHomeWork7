def write1():
    list1 = [input('Введите фамилию: '),
             input('Введите имя: '),
             input('Введите телефон: '),
             input('Введите описание: ')]

    with open('phone_book1.txt', 'a', encoding='utf-8') as file:
        file.write(f'{"*".join(list1)}***\n')

    return list1


def write2():
    list2 = [input('Введите фамилию: '),
             input('Введите имя: '),
             input('Введите телефон: '),
             input('Введите описание: ')]

    with open('phone_book2.txt', 'a', encoding='utf-8') as file:
        for i in range(len(list2)-1):
            file.write(f'{list2[i]}*\n')
        file.write(f'{list2[len(list2)-1]}***\n')

    return list2
