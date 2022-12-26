def read1():
    list1 = []
    search1 = input('Введите данные для поиска: ')
    with open('phone_book1.txt', 'r', encoding='utf-8') as file:
        list0 = file.read().split('***')
        for i in range(len(list0)):
            if search1 in list0[i]:
                list1.append(list0[i])
    return search1, list1


def read2():
    list2 = []
    search2 = input('Введите данные для поиска: ')
    with open('phone_book2.txt', 'r', encoding='utf-8') as file:
        list0 = file.read().split('***')
        for i in range(len(list0)):
            if search2 in list0[i]:
                list2.append(list0[i])
    return search2, list2
