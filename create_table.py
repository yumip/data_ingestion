import psycopg2
from config import config

def create_table():
    # """ create tables in the PostgreSQL database"""
    command = """
        CREATE TABLE property (
            property_id SERIAL PRIMARY KEY,
            valuer_general_id INTEGER,
            address VARCHAR(255),
            suburb VARCHAR(255),
            postcode INTEGER,
            saleprice BIGINT,
            saledate DATE
        )
        """

    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(command)
        # create table one by one
        # for command in commands:
        #     cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_table()
