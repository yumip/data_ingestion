from insert_property_list import insert_property_list
from datetime import datetime

def read_dat_current(file_path, value_list):
    # value_list = []
    with open(file_path, "r") as df:
        lines = df.read().split("\n")

        for line in lines[:-1]:
            if line.strip() != '' and line[0] == "B":
                line.replace('\\', '/')
                lineSplit = line.split(";")
                property_id = lineSplit[2]
                property_address = " ".join(lineSplit[5:9]).strip()
                suburb = lineSplit[9]
                postcode = lineSplit[10]
                sale_price = lineSplit[15]
                sale_date = lineSplit[13]
                record = [property_id, property_address,
                          suburb, postcode, sale_price, sale_date]
                value_list.append(record)
    return value_list

def read_dat_archived(file_path, value_list):
    # value_list = []
    with open(file_path, "r") as df:
        lines = df.read().split("\n")

        for line in lines[:-1]:
            if line.strip() != '' and line[0] == "B":
                line = line.replace('\\', '/')
                lineSplit = line.split(";")
                property_id = lineSplit[4]
                property_address = " ".join(lineSplit[5:8]).strip()
                suburb = lineSplit[8]
                postcode = lineSplit[9]
                sale_price = lineSplit[11]
                date_object = datetime.strptime(lineSplit[10],"%d/%m/%Y")
                sale_date = date_object.strftime("%Y%m%d")
                record = [property_id, property_address, suburb, postcode, sale_price, sale_date]
                value_list.append(record)
    return value_list 

    # insert_property_list(value_list)
