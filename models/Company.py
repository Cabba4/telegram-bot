import mysql.connector

from models.Model import Model

class Company(Model):
    def __init__(self, attributes: dict):
        self.__id = attributes['id']
        self.__name = attributes['name']
        self.__logo_url = attributes['logo_url']
    
    def getId(self):
        return self.__id
    
    def getName(self):
        return self.__name
    
    def getLogoUrl(self):
        return self.__logo_url
    
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
            SELECT id, name, logo_url FROM companies
        """)

        companies = mycursor.fetchall()
        mycursor.close()
        mydb.close()

        if not companies:
            return None
        
        return [Company({
            'id': company[0],
            'name': company[1],
            'logo_url': company[2]
        }) for company in companies]
    
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
            SELECT id, name, logo_url FROM companies WHERE id = %s
        """, (id))

        company = mycursor.fetchone()
        mycursor.close()
        mydb.close()

        if not company:
            return None
        
        return Company({
            'id': company[0],
            'name': company[1],
            'logo_url': company[2]
        })