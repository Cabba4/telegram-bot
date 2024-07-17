import mysql.connector

from models.Model import Model
from models.Company import Company

class JobAd(Model):
    def __init__(self, attributes: dict):
        self.__id = attributes['id']
        self.__title = attributes['title']
        self.__description = attributes['description']
        self.__contract_type = attributes['contract_type']
        self.__location = attributes['location']
        self.__work_experience = attributes['work_experience']
        self.__company_id = attributes['company_id']

    def __str__(self):
        return f"*{self.getTitle()}* at {self.getCompany().getName()} - {self.getLink()}\n"

    def __setCompany(self, company: Company):
        self.__company = company
    
    def getId(self):
        return self.__id
    
    def getTitle(self):
        return self.__title
    
    def getDescription(self):
        return self.__description
    
    def getContractType(self):
        return self.__contract_type
    
    def getLocation(self):
        return self.__location
    
    def getWorkExperience(self):
        return self.__work_experience
    
    def getCompany(self):
        if (self.__company):
            return self.__company
        company = Company.getById(self.__company_id)
        self.__setCompany(company)
        return self.__company
    
    def getLink(self):
        return f'https://www.jobteaser.com/en/job-offers/{self.getId()}'
  
    @staticmethod
    def getAll() -> list:
        USER, PASS = Model.getDbCredentials()
        
        # db connection
        mydb = mysql.connector.connect(
            host='localhost',
            user=USER,
            password=PASS,
            database='user_infodb'
        )
        mycursor = mydb.cursor()

        # Fetch job data from the database
        mycursor.execute("""
            SELECT job_ads.id, job_ads.title, job_ads.description, job_ads.contract_type, job_ads.location, job_ads.work_experience, companies.id, companies.name, companies.logo_url
            FROM job_ads
            INNER JOIN companies ON job_ads.company_id = companies.id
        """)
        result = mycursor.fetchall()
        mycursor.close()
        mydb.close()

        job_list = []
        for row in result:
            job = JobAd({
                'id': row[0],
                'title': row[1],
                'description': row[2],
                'contract_type': row[3],
                'location': row[4],
                'work_experience': row[5],
                'company_id': row[6]
            })
            job.__setCompany(Company({
                'id': row[6],
                'name': row[7],
                'logo_url': row[8]
            }))
            job_list.append(job)
        
        return job_list
    
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

        # Fetch job data from the database
        mycursor.execute("""
            SELECT job_ads.id, job_ads.title, job_ads.description, job_ads.contract_type, job_ads.location, job_ads.work_experience, companies.id, companies.name, companies.logo_url
            FROM job_ads
            INNER JOIN companies ON job_ads.company_id = companies.id
            WHERE job_ads.id = %s
        """, (id,))
        result = mycursor.fetchone()
        mydb.close()

        if not result:
            return None

        job = JobAd({
            'id': result[0],
            'title': result[1],
            'description': result[2],
            'contract_type': result[3],
            'location': result[4],
            'work_experience': result[5],
            'company_id': result[6]
        })
        job.__setCompany(Company({
            'id': result[6],
            'name': result[7],
            'logo_url': result[8]
        }))
        
        return job
    