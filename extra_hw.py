"""""""""
Пользователь вводит числа по одному четные вы добавляете в один список нечетные во второй.
После каждого ввода спрашиваете продолжить или нет если продолжить то предлагаете ввести следующее число, если нет
выводите два списка.
Если пользователь вводит не число выводите ошибку с текстом который говорит что можно вводить только числа.
Дальше немного усложняете задачу.
Когда пользователь говорит что дальше не продолжать спрашиваете в каком порядке сортировать списки asc по возрастанию,
desc по убыванию.
Сортировать нужно в ручную без использования встроенных функций. Методы можете поискать но большая просьба не копировать
код а продумать самостоятельно  и реализовать сортировку в виде функции.
Дальше можно еще усложнить в третий список вы добавляете все значения пользователя, но таким образом чтобы он всегда
был отсортированным по возрастанию.
Тоесть при каждом вводе вы смотрите куда нужно вставить новое значение, для поиска места вставки используйте
бинарный поиск(https://ru.wikipedia.org/wiki/Двоичный_поиск) опять же код лучше не смотреть а подумать.
"""""""""


def ask_sort_list(user_list):
    for number in range(len(user_list)):
        for second_number in range(number + 1, len(user_list)):
            if user_list[number] > user_list[second_number]:
                temp = user_list[number]
                user_list[number] = user_list[second_number]
                user_list[second_number] = temp
    return user_list


def desk_sort_list(user_list):
    for number in range(0, len(user_list)):
        for second_number in range(1, len(user_list)):
            if user_list[number] < user_list[second_number]:
                temp = user_list[number]
                user_list[number] = user_list[second_number]
                user_list[second_number] = temp
    return user_list


def return_list_of_numbers():
    list_of_evens_numbers = list()
    list_of_odds_numbers = list()
    answ_user = 1
    while answ_user == 1:
        ask_user = input("Если хотите продолжить, введите 1\n:")
        if int(ask_user) == answ_user:
            valid = False
            while not valid:
                user_input = input("Введите число:")
                if user_input.isdigit():
                    valid = True
                    if int(user_input) % 2 == 0:
                        list_of_evens_numbers.append(int(user_input))
                    else:
                        list_of_odds_numbers.append(int(user_input))
                else:
                    print("Неверный ввод, ведите пожалуйста число")
        else:
            answ_user = 0
            ask_sort = input("В каком порядке сортировать списки ?\n"
                             "- по возростанию, введите 1\n"
                             "- по убыванию, введите 2\n"
                             ":")
            if ask_sort == "1":
                print(ask_sort_list(list_of_odds_numbers), ask_sort_list(list_of_evens_numbers))
            else:
                print(desk_sort_list(list_of_odds_numbers), desk_sort_list(list_of_evens_numbers))

return_list_of_numbers()
