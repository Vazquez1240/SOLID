# Ejercicio

# Problema 1: La clase UserManager es responsable de agregar, eliminar y mostrar usarios

# Codigo que no cumple con SRP
class UserManager: 
    def __init__(self):
        self.users = []
        
    def add_user(self, user):
        self.users.append(user)
        
    def remove_user(self, user):
        self.users.remove(user)
        
    def display_users(self):
        for user in self.users:
            print(user)
            
            
            
# Codigo refactorizado que cumple SRP
class UserManagerSRP: 
    def __init__(self):
        self.users = []
        
    def add_user(self, user):
        self.users.append(user)
        
    def remove_user(self, user):
        self.users.remove(user)
    

class UserDisplay:
    @staticmethod
    def display_users(users):
        for user in users:
            print(user)