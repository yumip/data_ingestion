# import os
import psycopg2
from config import config

def insert_property_list(property_list):
    # """ insert multiple vendors into the vendors table  """
    sql = "INSERT INTO property (valuer_general_id, address, suburb, postcode, saleprice, saledate) values(%s,%s,%s,%s)"
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany(sql, property_list)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("the process completed")


# value_list = []
# with open('../20210426/001_SALES_DATA_NNME_26042021.DAT', "r") as df:
#     lines = df.read().split("\n")

#     for line in lines[:-1]:
#         if line[0] == "B":
#             lineSplit = line.split(";")
#             property_id = lineSplit[2]
#             property_address = " ".join(lineSplit[5:11]).strip()
#             sale_price = lineSplit[15]
#             sale_date = lineSplit[13]
#             record = [property_id, property_address, sale_price, sale_date]
#             value_list.append(record)

# insert_property_list(value_list)
# print(value_list)
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


# read_dat('../20210426/001_SALES_DATA_NNME_26042021.DAT')


# def loop_directory(directory: str):
#     for filename in os.listdir(directory):
#         if filename.endswith(".DAT"):
#             file_directory = os.path.join(directory, filename)
#             # print(filename)
#             read_dat(file_directory)


# if __name__ == '__main__':
#     loop_directory('../20210426/')
