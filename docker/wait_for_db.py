import psycopg2
import os


def main():

    db_host = os.environ['POSTGRES_HOST']
    db_name = os.environ['POSTGRES_DB']
    db_user = os.environ['POSTGRES_USER']
    db_pass = os.environ['POSTGRES_PASSWORD']
    db_port = os.environ['POSTGRES_PORT']

    # Define our connection string
    conn_string = "host='{}' dbname='{}' user='{}' password='{}' port={}".format(db_host, db_name, db_user, db_pass, db_port)

    while True:
        try:
            # get a connection, if a connect cannot be made an exception will be raised here
            psycopg2.connect(conn_string)
            print("DB Connected!")
            break
        except Exception as e:
            if 'Connection refused' in str(e):
                print("waiting ...")
            else:
                print("DB Connected!")
                break


if __name__ == "__main__":
    main()
