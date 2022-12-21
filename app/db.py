import pymysql
from decouple import config

class DAO():
    def __init__(self, parameters: tuple = None):
        self._parameters = parameters
        try:
            print("Iniciando conexion ...")
            self.conexion = pymysql.connect(
            host=config("DB_HOST"),
            user=config("DB_USER"),
            password=config("DB_PASSWORD"),
            db=config("DB_NAME"),
            cursorclass=pymysql.cursors.DictCursor
            )
        except Exception as ex:
            print("Error durante la conexion: {}".format(ex))

    def get_users(self):
        try:
            cursor = self.conexion.cursor()
            cursor.execute("call sp_get_user(null)")
            table = cursor.fetchall()
            return table
        except Exception as ex:
            print("Error durante la conexion: {}".format(ex))
            return None
        finally:
            print("La conexion ha sido finalizada ....")
            self.conexion.close()

    def get_user(self):
        try:
            cursor = self.conexion.cursor()
            cursor.execute("call sp_get_user(%s)", self._parameters)
            table = cursor.fetchone()
            return table
        except Exception as ex:
            print("Error durante la conexion: {}".format(ex))
            return None
        finally:
            print("La conexion ha sido finalizada ....")
            self.conexion.close()

    def insert_user(self):
        try:
            cursor = self.conexion.cursor()
            cursor.execute("call sp_insert_user(%s, %s)", self._parameters)
            self.conexion.commit()
            table = cursor.fetchone()
            return table
        except Exception as ex:
            print("Error durante la conexion: {}".format(ex))
            return None
        finally:
            print("La conexion ha sido finalizada ....")
            self.conexion.close()

    def delete_user(self):
        try:
            cursor = self.conexion.cursor()
            cursor.execute("call sp_delete_user(%s)", self._parameters)
            self.conexion.commit()
            table = cursor.fetchone()
            return table
        except Exception as ex:
            print("Error durante la conexion: {}".format(ex))
            return None
        finally:
            print("La conexion ha sido finalizada ....")
            self.conexion.close()
