from abc import ABC, abstractmethod
import os
from typing import Final
from dotenv import load_dotenv

class Model(ABC):
    def getDbCredentials():
        load_dotenv()
        USER: Final = os.getenv('DB_USER')
        PASS: Final = os.getenv('DB_PASS')
        return USER, PASS
    
    @abstractmethod
    def getAll():
        pass

    @abstractmethod
    def getById(id: str):
        pass
