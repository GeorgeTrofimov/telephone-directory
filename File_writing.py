from distutils.log import info
import Information as gi
info = gi()
def writing_scv ():
    file = 'TelephoneDirectory.csv'
    with open (file, 'a', encoding='utf-8') as data:
        data.write(f'{info[0]}; {info[1]}; {info[2]}; {info[3]}\n')

def writing_txt ():
      file = 'TelephoneDirectory.txt'
      with open (file, 'a', encoding='utf-8') as data:
        data.write(f'Фамилия: {info[0]}\n\n Имя:  {info[1]}\n\n Телефон: {info[2]}\n\n Описание:{info[3]}\n\n\n')

def creating ():
      file='TelephoneDirectory.csv'
      with open (file, 'w', encoding= 'utf-8') as data:
        data.write(f'Фамилия, Имя, Телефон, Описание\n')