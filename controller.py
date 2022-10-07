import TD_functions as f
import TD_base as td
import gui as g  

def start_button():
    TemporaryDirectory_temp = td.get_base()
    td.get_storage(f.new_data(f.new_id(f.read_base(TemporaryDirectory_temp)), g.last_name(), g.first_name(), g.phone_number()))
    #fy.find(g.get_surname(), fy.read_base(TemporaryDirectory_temp))
    #print(fy.find(g.get_surname(), fy.read_base(TemporaryDirectory_temp)))