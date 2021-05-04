from insert_property_list import insert_property_list

# def read_dat(file_path):
#     value_list = []
#     with open(file_path, "r") as df:
#         lines = df.read().split("\n")

#         for line in lines[:-1]:
#             if line[0] == "B":
#                 lineSplit = line.split(";")
#                 property_id = lineSplit[2]
#                 property_address = " ".join(lineSplit[5:11]).strip()
#                 sale_price = lineSplit[15]
#                 sale_date = lineSplit[13]
#                 record = [property_id, property_address, sale_price, sale_date]
#                 value_list.append(record)

#     insert_property_list(value_list)


def read_dat(file_path, value_list):
    # value_list = []
    with open(file_path, "r") as df:
        lines = df.read().split("\n")

        for line in lines[:-1]:
            if line[0] == "B":
                lineSplit = line.split(";")
                property_id = lineSplit[2]
                property_address = " ".join(lineSplit[5:9]).strip()
                suburb = lineSplit[9]
                postcode = lineSplit[10]
                sale_price = lineSplit[15]
                sale_date = lineSplit[13]
                record = [property_id, property_address, suburb, postcode, sale_price, sale_date]
                value_list.append(record)
    return value_list 
    # insert_property_list(value_list)
