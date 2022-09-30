from ast import Try
from distutils.log import info


def information ():
    info = []
    Last_name=input( 'Введите вашу фамилию:')
    info.appened(Last_name)
    first_name=input('Введите ваше имя')

    phone_number = ''

    valid = False

    while not valid:
        try:
            phone_number=input('Введите номер телефона: ')
            if len(phone_number) != 11:
                print('Проверьте номер (в номере должно быть 11 символов)')
            else:
                phone_number=int(phone_number)
                valid = True
        except:
            print('Номер должен содержать только цифры! ')

    info.append(phone_number)
    description=input('Введите описание: ')
    info.append(description)
    return

