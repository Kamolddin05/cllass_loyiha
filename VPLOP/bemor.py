from foydalanuvchi import Foydalanuvchi

class Bemor(Foydalanuvchi):
    
    def holati(slef):
        print("Holat: Bemor - sariq kasal bolgan. ")
        
    def info(self):
        print(f"Ismi: {self.ism} : Email: {self.email}")
        
if __name__ == "__main__":
    
    bemor = Bemor("Diyorbek", "Diyorbek005@gamil.com")
    bemor.info()
    bemor.holati()
    

        