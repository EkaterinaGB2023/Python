import os

def show_contacts(file_name):
    os.system('CLS')
    with open(file_name,'r') as file:
        data = file.readlines()

        for contact in data:
            print(contact)

    input('Нажмите Enter для продолжения: ')

def add_contact(file_name):
    os.system('CLS')
    with open(file_name,'a') as file:
        res = ''
        res += input('Введите фамилию: ') + ' '
        res += input('Введите имя: ') + ' '
        res += input('Введите номер телефона: ') 

        file.write('\n' + res)
    input('Контакт сохранен! Нажмите Enter для продолжения: ')

def find_contact(file_name):
    os.system('CLS')
    target = input('Введите информацию для поиска: ')

    with open(file_name,'r') as file:
        data = file.readlines()

        for contact in data:
            if target in contact:
                print(contact)
                break
        else:
            print('Контакт не найден')
    
    input('Нажмите Enter для продолжения: ')

def menu():
    print('1 - показать контакты')
    print('2 - добавить контакт')
    print('3 - найти контакт')
    print('4 - изменить контакт')
    print('5 - удалить контакт')
    print('6 - выход')

def change_contact(file_name):
    os.system('CLS')

    with open(file_name,'r+') as file:
        data = file.readlines()
        origin = input('Введите данные контакта, которые нужно изменить: ')
        new = input('Введите новые данные контакта: ')

        for i in range(len(data)):
            if origin in data[i]:
                data[i] = data[i].replace(origin, new)
        else:
            print('Контакт не найден')

        file.seek(0)
        file.writelines(data)
        file.truncate()

    input('Нажмите Enter для продолжения: ')

def delete_contact(file_name):
    os.system('CLS')

    with open(file_name, 'r+') as file:
        data = file.readlines()
        target = input('Введите данные контакта, который нужно удалить: ')
        for i in range(len(data)):
            if target in data[i]:
                del data[i]
                break
        else:
            print('Контакт не найден')

        file.seek(0)
        file.writelines(data)
        file.truncate()

    input('Нажмите Enter для продолжения: ')

def main(file_name):
    while True:
        os.system('CLS')
        menu()
        user_choice = int(input('Введите номер команды: '))

        if user_choice == 1:
            show_contacts(file_name)
        elif user_choice == 2:
            add_contact(file_name)
        elif user_choice == 3:
            find_contact(file_name)
        elif user_choice == 4:
            change_contact(file_name)
        elif user_choice == 5:
            delete_contact(file_name)
        elif user_choice == 6:
            print('Пока! Хорошего дня!')
            return

main('info.txt')

