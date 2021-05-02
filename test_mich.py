import os
import pandas as pd
from insert_property_list import insert_property_list
directory = '../20210426/'
value_lists = []
# for filename in os.listdir(directory):
#     if filename.endswith(".DAT"):


def loop_function(filename):
    f = open(filename)
    lines = f.read().split("\n")
    for line in lines[:-1]:
        if line[0] == "B":
            lineSplit = line.split(";")
            property_id = lineSplit[2]
            property_address = " ".join(lineSplit[5:11]).strip()
            sale_price = lineSplit[15]
            sale_date = lineSplit[13]
            value_list = [property_id, property_address, sale_price, sale_date]
            value_lists.append(value_list)


def loop_directory(directory: str):
    '''Loop files in the directory'''
    for filename in os.listdir(directory):
        if filename.endswith(".DAT"):
            file_directory = os.path.join(directory, filename)
            print(file_directory)
            loop_function(file_directory)


if __name__ == '__main__':
    loop_directory(directory)
    df = pd.DataFrame(value_lists)
    insert_property_list(value_lists)
    print(df)

