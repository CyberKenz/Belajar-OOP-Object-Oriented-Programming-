#Object Class
class user(object):
    
    #Encapsulation Protected
    _password = None
    
    def __init__(self, username, password):
        self.username = username
        self._password = password
        
    def _samarkanPass(self):
        return '*' * len(self._password)
       
    def registerInfo(self):
        print(f"Username : {self.username}\nPassword : {self._samarkanPass()}")
        
    def notification(self):
        print("User Created by Self\n")
        
#Inheritance
class admin(user):
    
    #Polymorphism
    def notification(self):
        print("User Created by Admin\n")

                              
def register():
        print("REGISTER\n")
        username = input("Masukkan username anda : ")
        password = input("Masukkan password anda : ")
        role = input("Ingin daftar sebagai (user/admin)? : ").strip().lower()
        
        if role not in ("user", "admin"):
            print("Inputan role tidak valid")
            return
        
        if role == "user":
            account = user(username, password)
        else:
            account = admin(username, password)

        account.registerInfo()
        account.notification()
        
if __name__ == "__main__" :
        register()
        
        
        
       
