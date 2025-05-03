from binascii import Error
from turtle import pd
import mysql.connector
from mysql.connector import connect

def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            database='mysql',
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection
def create_database(connection, database_name):
    cursor = connection.cursor()

    try:
        cursor.execute(f"CREATE DATABASE {database_name}")
        print(f"Database {database_name} created successfully")
    except Error as err:
        print(f"Error: '{err}'")

    cursor.close()

def create_table(connection, database_name, table_name):
    cursor = connection.cursor()

    try:    
        cursor.execute(f"USE {database_name}")
        sql_create_table = f"""CREATE TABLE {table_name} (
                                id INT AUTO_INCREMENT PRIMARY KEY,
                                name VARCHAR(50) NOT NULL,
                                age INT NOT NULL,
                                gender VARCHAR(10) NOT NULL,
                                email VARCHAR(50) NOT NULL
                            )"""
        cursor.execute(sql_create_table)
        print(f"Table {table_name} created successfully")
    except Error as err:
        print(f"Error: '{err}'")

    cursor.close()

    def insert_data(connection, database_name, table_name, data):
        cursor = connection.cursor()

        try:
            cursor.execute(f"USE {database_name}")
            sql_insert_query = f"""INSERT INTO {table_name} (name, age, gender, email) VALUES (%s, %s, %s, %s)"""
            cursor.execute(sql_insert_query, data)
            connection.commit()
            print(f"Record inserted successfully into table {table_name}")    
        except Error as err:
            print(f"Error: '{err}'")

        cursor.close()

def fetch_all_data(connection, database_name, table_name):
    cursor = connection.cursor()

    try:
        cursor.execute(f"USE {database_name}")
        sql_fetch_query = f"SELECT * FROM {table_name}"
        cursor.execute(sql_fetch_query)
        result = cursor.fetchall()
        print("Data fetched successfully")
        return result
    except Error as err:
        print(f"Error: '{err}'")

    cursor.close()

    def delete_data(connection, database_name, table_name, id):
        cursor = connection.cursor()

        try:
            cursor.execute(f"USE {database_name}")
            sql_delete_query = f"DELETE FROM {table_name} WHERE id = {id}"
            cursor.execute(sql_delete_query)
            connection.commit()
            print(f"Record deleted successfully from table {table_name}")    
        except Error as err:
            print(f"Error: '{err}'")

        cursor.close()

        def update_data(connection, database_name, table_name, id, data):
            cursor = connection.cursor()

            try:
                cursor.execute(f"USE {database_name}")
                sql_update_query = f"""UPDATE {table_name} SET name = %s, age = %s, gender = %s, email = %s WHERE id = {id}"""
                cursor.execute(sql_update_query, data)
                connection.commit()
                print(f"Record updated successfully in table {table_name}")    
            except Error as err:
                print(f"Error: '{err}'")

            cursor.close()
            if __name__ == '__main__':
                connection = create_server_connection("localhost", "root", "root")
                create_database(connection, "mydatabase")
                create_table(connection, "mydatabase", "mytable")
                data = ("Kelly Cristina", 38, "Female", "kellycristina@gmail.com")  
                insert_data(connection, "mydatabase", "mytable", data) # type: ignore
                result = fetch_all_data(connection, "mydatabase", "mytable")
                print(result)
                delete_data(connection, "mydatabase", "mytable", 1)
                update_data(connection, "mydatabase", "mytable", 2, ("Jane Doe", 30, "Female", "janedoe@gmail.com"))
                result = fetch_all_data(connection, "mydatabase", "mytable")
                print(result)
                connection.close()

                create_database_query = "CREATE DATABASE mydatabase"
                create_table_query = "CREATE TABLE mytable (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50) NOT NULL, age INT NOT NULL, gender VARCHAR(10) NOT NULL, email VARCHAR(50) NOT NULL)"
                insert_data_query = "INSERT INTO mytable (name, age, gender, email) VALUES (%s, %s, %s, %s)"
                fetch_all_data_query = "SELECT * FROM mytable"
                delete_data_query = "DELETE FROM mytable WHERE id = %s"
                update_data_query = "UPDATE mytable SET name = %s, age = %s, gender = %s, email = %s WHERE id = %s"
                connection = create_server_connection("localhost", "root", "root")
                cursor = connection.cursor()
                cursor.execute(create_database_query)
                cursor.execute(create_table_query)
                cursor.execute(insert_data_query, data)
                cursor.execute(fetch_all_data_query)
                result = cursor.fetchall()
                print(result)
                cursor.execute(delete_data_query, (1,))
                cursor.execute(update_data_query, ("Fagner Jacob", 37, "Male", "fagnerjacob@gmail.com", 2))
                cursor.execute(fetch_all_data_query)
                result = cursor.fetchall()
                print(result)
                connection.commit()
                connection.close()

                def create_db_connection(host_name, user_name, user_password, db_name):
                    connection = None
                    try:
                        connection = mysql.connector.connect(
                            host=host_name,
                            user=user_name,
                            passwd=user_password,
                            database=db_name
                        )
                        print("MySQL Database connection successful")
                    except Error as err:
                        print(f"Error: '{err}'")

                    return connection
                
                def execute_query(connection, query):
                    cursor = connection.cursor()

                    try:    
                        cursor.execute(query)
                        connection.commit()
                        print("Query executed successfully")
                    except Error as err:
                        print(f"Error: '{err}'")

                    cursor.close()

                create_teachers_table_query = "CREATE TABLE teachers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50) NOT NULL, age INT NOT NULL, gender VARCHAR(10) NOT NULL, email VARCHAR(50) NOT NULL)"
                create_students_table_query = "CREATE TABLE students (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50) NOT NULL, age INT NOT NULL, gender VARCHAR(10) NOT NULL, email VARCHAR(50) NOT NULL)"
                create_teachers_table_query = "CREATE TABLE teachers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50) NOT NULL, age INT NOT NULL, gender VARCHAR(10) NOT NULL, email VARCHAR(50) NOT NULL)"
                create_students_table_query = "CREATE TABLE students (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50) NOT NULL, age INT NOT NULL, gender VARCHAR(10) NOT NULL, email VARCHAR(50) NOT NULL)"
                connection = create_db_connection("localhost", "root", "root", "mydatabase")
                execute_query(connection, create_teachers_table_query)
                execute_query(connection, create_students_table_query)
                connection.close()

                connection = create_db_connection("localhost", "root", "root", "mydatabase", "pw")
                execute_query(connection, "SELECT * FROM teachers")
                result = cursor.fetchall()
                print(result)
                connection.close()

                connection = create_db_connection("localhost", "root", "root", "mydatabase")
                execute_query(connection, "SELECT * FROM students")
                result = cursor.fetchall()
                print(result)
                connection.close()

                connection = create_db_connection("localhost", "root", "root", "mydatabase""pw")
                execute_query(connection, "INSERT INTO teachers (name, age, gender, email) VALUES (%s, %s, %s, %s)", ("John Doe", 35, "Male", "johndoe@gmail.com"))
                execute_query(connection, "INSERT INTO teachers (name, age, gender, email) VALUES (%s, %s, %s, %s)", ("Jane Doe", 30, "Female", "janedoe@gmail.com"))
                execute_query(connection, "INSERT INTO students (name, age, gender, email) VALUES (%s, %s, %s, %s)", ("Kelly Cristina", 38, "Female", "kellycristina@gmail.com"))
                execute_query(connection, "INSERT INTO students (name, age, gender, email) VALUES (%s, %s, %s, %s)", ("Fagner Jacob", 37, "Male", "fagnerjacob@gmail.com"))
                connection.close()





















 







    

