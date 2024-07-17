import mysql.connector

from models.Model import Model

class User(Model):
    def __init__(self, attributes: dict):
        self.__id = attributes['id']
        self.__first_name = attributes['first_name']
        self.__last_name = attributes['last_name']
        self.__username = attributes['username']
        self.__language_code = attributes['language_code']
    
    def getId(self):
        return self.__id
    
    def getFirstName(self):
        return self.__first_name
    
    def getLastName(self):
        return self.__last_name
    
    def getUsername(self):  
        return self.__username
    
    def getLanguageCode(self):
        return self.__language_code
    
    @staticmethod
    def getAll():
        USER, PASS = Model.getDbCredentials()
        
        # db connection
        mydb = mysql.connector.connect(
            host='localhost',
            user=USER,
            password=PASS,
            database='user_infodb'
        )
        mycursor = mydb.cursor()

        # Fetch company data from the database
        mycursor.execute("""
            SELECT id, first_name, last_name, username, language_code FROM users
        """)

        users = mycursor.fetchall()
        mycursor.close()
        mydb.close()

        if not users:
            return None
        
        return [User({
            'id': user[0],
            'first_name': user[1],
            'last_name': user[2],
            'username': user[3],
            'language_code': user[4]
        }) for user in users]
    
    @staticmethod
    def getById(id: str):
        USER, PASS = Model.getDbCredentials()
        
        # db connection
        mydb = mysql.connector.connect(
            host='localhost',
            user=USER,
            password=PASS,
            database='user_infodb'
        )
        mycursor = mydb.cursor()

        # Fetch company data from the database
        mycursor.execute("""
            SELECT id, first_name, last_name, username, language_code FROM users WHERE id = %s
        """, (id))

        user = mycursor.fetchone()
        mycursor.close()
        mydb.close()

        if not user:
            return None
        
        return User({
            'id': user[0],
            'first_name': user[1],
            'last_name': user[2],
            'username': user[3],
            'language_code': user[4]
        })
    
    @staticmethod
    def create(attributes: dict):
        USER, PASS = Model.getDbCredentials()
        
        # db connection
        mydb = mysql.connector.connect(
            host='localhost',
            user=USER,
            password=PASS,
            database='user_infodb'
        )
        mycursor = mydb.cursor()

        # Fetch company data from the database
        mycursor.execute("""
            INSERT INTO users (id, first_name, last_name, username, language_code) VALUES (%s, %s, %s, %s, %s)
        """, (attributes['id'], attributes['first_name'], attributes['last_name'], attributes['username'], attributes['language_code']))

        mydb.commit()
        mycursor.close()
        mydb.close()

        return User(attributes)