
from os.path import exists
from CSV_Table import creating
from File_writing import writing_csv
from File_writing import writing_txt

path = 'TelephoneDirectory.csv'
valid = exists(path)
if not valid:
    creating()

writing_csv()
writing_txt()