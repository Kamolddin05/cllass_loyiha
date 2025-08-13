from abc import ABC, abstractmethod

class Foydalanuvchi(ABC):
    def __init__(self, ism, email):
        self.ism = ism
        self.email = email
        
    def info(self):
        print(f"Ismi: {self.ism} : Email: {self.email}")
        
    @abstractmethod
    def rol(self):
        pass
    