#pip install mysql-connector-python
import mysql.connector

class CConexion:
    def conexionBaseDeDatos():
        try:
            #Poner los datos de ty Mysql y el nombre de tu base datos
            Conexion=mysql.connector.connect(user='root',password='root',
                                            host='127.0.0.1',
                                            database='clientesbd',
                                            port='2206')
            print("Conexion Correcta")
            return Conexion
        except mysql.connector.Error as error:
            print("Error al conectarse a la base de datos {}".format(error))
            return Conexion
    conexionBaseDeDatos()