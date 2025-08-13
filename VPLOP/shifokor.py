from foydalanuvchi import Foydalanuvchi

class Shifokor(Foydalanuvchi):
    def rol(self):
        print("Rol: Shifokor - bemorlarga qaraydi. ")


    def info(self):
        print(f"Shifokor Ismi: {self.ism} : Email: {self.email}")
        
        
if __name__  == "__main__":
    
    shifokor = Shifokor("Kamoliddin", "dr.kamoliddin@gmail.com")
    shifokor.info()
    shifokor.rol()