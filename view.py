def view_input1():
    text = input(
        '\nВведите "0" - сделать запись, или "1" - получить запись: ')
    return text


def view_input2():
    text = input(
        'Введите "0" - выбрать "phone_book1.txt", или "1" - выбрать "phone_book2.txt": ')
    return text


def view_write(data):
    print(f'\nСделана запись: "{", ".join(data)}"')


def view_read(search, data):
    if len(data) == 1:
        print(f'\nЗапись по запросу "{search}":')
        if '\n' in data[0]:
            data[0] = data[0].replace('\n', '')
        data = data[0].split('*')
        print(f'{", ".join(data)}')
    elif len(data) > 1:
        print(f'\nЗаписи по запросу "{search}":')
        for i in range(len(data)):
            if '\n' in data[i]:
                data[i] = data[i].replace('\n', '')
            data[i] = data[i].split('*')
            print(f'{", ".join(data[i])}')
    else:
        print(f'\nЗаписи не найдены по запросу "{search}"')
