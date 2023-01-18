from model.movies import MoviesScores, database
from decouple import config
import pymysql
import json
import peewee

HOST_MYSQL = config('HOST_MYSQL')
PORT_MYSQL = int(config('PORT_MYSQL'))
USER_MYSQL = config('USER_MYSQL')
PASSWORD_MYSQL = config('PASSWORD_MYSQL')
DB_MYSQL = config('DB_MYSQL')

database = peewee.MySQLDatabase(
    DB_MYSQL,
    host=HOST_MYSQL,
    port=PORT_MYSQL,
    user=USER_MYSQL,
    passwd= PASSWORD_MYSQL
)

def create_database_if_not_exists(host,user,password, db_name):
    try:
        connection = pymysql.connect(
            host=host,
            user=user,
            password=password
        )
        cursor = connection.cursor()
        cursor.execute(f'SHOW DATABASES LIKE "{db_name}"')
        result = cursor.fetchone()
        if result:
            print(f'La base de datos "{db_name}" ya existe.')
        else:
            cursor.execute(f'CREATE DATABASE {db_name}')
            print(f'La base de datos "{db_name}" se ha creado exitosamente.')
    except pymysql.Error as e:
        print(f'Ocurrió un error durante la creación de la base de datos "{db_name}":\n{e}')
    finally:
        connection.close()
        
def upload_data_to_mysql(table_model, file_name):
    try:
        # Verificar si la tabla existe
        if table_model.table_exists():
            table_model.drop_table()
        # Crear tabla en MySQL
        table_model.create_table()
        # Abrir el archivo json y cargar en una variable
        with open(f'app/db/{file_name}.json', 'r') as file:
            data = json.load(file)
        # Insertar los datos en la tabla creada
        query = table_model.insert_many(data)
        query.execute()
        print(f'La carga del archivo "{file_name}.json" se ha completado exitosamente!')
    except Exception as e:
        print(f'Ocurrió un error al cargar los datos {e}')

if __name__ == '__main__':
    create_database_if_not_exists(HOST_MYSQL, USER_MYSQL, PASSWORD_MYSQL, DB_MYSQL)
    upload_data_to_mysql(MoviesScores, DB_MYSQL)