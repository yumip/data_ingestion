import psycopg2
from config import config
from io import StringIO
import csv

def copy_property_list(property_list):
    # """ insert multiple vendors into the vendors table  """
    # sql = "INSERT INTO property (valuer_general_id, address, saleprice, saledate) values(%s,%s,%s,%s)"
    conn = None

    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        # cur.executemany(sql, property_list)
        with StringIO() as csv_file_like_object:
            writer = csv.writer(csv_file_like_object, delimiter=';')
            writer.writerows(property_list)
            csv_file_like_object.seek(0)
            cur.copy_from(csv_file_like_object, "property", sep=";", columns=(
                'valuer_general_id', 'address', 'suburb', 'postcode', 'saleprice', 'saledate'))
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


