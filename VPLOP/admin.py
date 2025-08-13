from foydalanuvchi import Foydalanuvchi

class Admin(Foydalanuvchi):
    
    def rol(self):
        print("Rol: Admin - poliklinika kompyuter tizimlariga qaraydi. ")
        
    def info(self):
        print(f"Ism: {self.ism} : Email: {self.email}")
        
if __name__ == "__main__":
    
    admin = Admin("Sarvar", 'admin.sarvar2@gmail.com')      
    admin.info()
    admin.rol()
        
    