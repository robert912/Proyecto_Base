"""import pymysql

class Database:
    def __init__(self):
        self.connection = pymysql.connect(
            host = 'localhost',
            user='root',
            password='toor',
            db='gestion_recursos'
        )

        self.cursor = self.connection.cursor()
        print("conexion Stableshied")
    
    def select_pers(self, id):
        sql = 'select * from persona where id = '+str(id)
        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()

            print("id:",user[0])
            print("identificacion:",user[1])
            print("nombre2:",user[2])

        except Exception as e:
            raise

database = Database()
database.select_pers(1)"""