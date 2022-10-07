def get_storage(data):
    with open ('TelephoneDirectory.txt', 'a', encoding="utf-8") as file:
        file.write(f'**{data}**\n')

def get_base():
    with open ('TelephoneDirectory.txt', 'r', encoding="utf-8") as file:
        return file.readlines()

def del_data (id, TelephoneDirectory):
    TelephoneDirectory = [TelephoneDirectory[i] for i in range(len(TelephoneDirectory)) if TelephoneDirectory[i][1] != id]
    '**'.join(TelephoneDirectory)
    with open('TelephoneDirectory.txt', 'w', encoding="utf-8") as file:
        file.write(f'**{TelephoneDirectory}**\n') 