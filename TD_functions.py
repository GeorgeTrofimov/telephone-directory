def new_data (id, last_name, first_name, phone_number):
    new_str = [id, last_name, first_name, phone_number]
    return "**".join(new_str)

def new_id (TemporaryDirectory):
    id_temp = [TemporaryDirectory[i][1] for i in range(len(TemporaryDirectory))]
    id_list = tuple(map(int, id_temp))
    return str(max(id_list) + 1)

def read_base(TemporaryDirectory):
    TemporaryDirectory = [TemporaryDirectory[i][:-1] for i in range(len(TemporaryDirectory))]
    TemporaryDirectory = [TemporaryDirectory[i].split('**') for i in range(len(TemporaryDirectory))]
#    TemporaryDirectory = [TemporaryDirectory[i].remove('**') for i in range(len(TemporaryDirectory))]
    return TemporaryDirectory

#def find(last_name, TemporaryDirectory):
    last_name_list = [TemporaryDirectory[i] for i in range(len(TemporaryDirectory)) if TemporaryDirectory[i][2] == last_name]
    return last_name_list