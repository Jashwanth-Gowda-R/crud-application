from db import connect


class User:
    def __init__(self, email, first_name, last_name, id):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    # INSERT data into database Table
    def insert_to_db(self):
        # with psycopg2.connect(user="postgres",password="99866",database="crud", host="localhost")as connection:
        with connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute('INSERT INTO users (email,first_name,last_name) VALUES (%s,%s,%s)',
                              (self.email, self.first_name, self.last_name))

    # update or replace row or column data in table
    @staticmethod
    def update_table(email,first_name):
        # with psycopg2.connect(user="postgres",password="99866",database="crud", host="localhost")as connection:
        with connect() as connection:
            with connection.cursor() as cursor:
                print("Table Before updating record ")
                sql_select_query = ('select * from users')
                cursor.execute(sql_select_query)
                record = cursor.fetchone()
                print(record)

                #update single record row
                sql_update_query = ('Update users set email = %s where first_name = %s')
                cursor.execute(sql_update_query, (email, first_name))
                connection.commit()
                count = cursor.rowcount
                print(count, "Record Updated successfully ")

                print("Table After updating record ")
                sql_select_query = ('select * from users where email = %s')
                cursor.execute(sql_select_query, (email,))
                record = cursor.fetchone()
                print(record)

    # delete row or column in table
    @staticmethod
    def delete_data(email):
        # with psycopg2.connect(user="postgres",password="99866",database="crud", host="localhost")as connection:
        with connect() as connection:
            with connection.cursor() as cursor:
                sql_delete_query = ('Delete from users where email = %s')
                cursor.execute(sql_delete_query, (email,))
                print("Record deleted successfully ")








# my_user=User("jashwanth.go@gmail.com","jashwanth","gowda",None)
# my_user.insert_to_db()

# email ="jashwanth.go@gmail.com"
# first_name="jashwanth"
# User.update_table(email,first_name)


#
# email="jashwanth.go@gmail.com"
# User.delete_data(email)







