from admin import Admin
from bemor import Bemor
from shifokor import Shifokor

def asosiy():
    
    a = Admin("Sarvar", "admin.sarvar2@gmail.com")
    b = Bemor("Diyorbek", "Diyorbek005@gamil.com")
    sh = Shifokor("Kamoliddin", "dr.kamoliddin@gmail.com")
    
    foydalanuvchilar = [a, b, sh]
    
    for f in foydalanuvchilar:
        f.info()
        f.rol()
        print("-" * 50)
        
if __name__ == "__main__":
    asosiy()