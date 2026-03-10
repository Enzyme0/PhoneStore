class Dog:
    def __init__(self, name):
        self.name = name
        self.hungry = True
        
    def bark(self):
        return self.name + " says: bark"
    
    def eat(self):
        self.hungry = False
        
    def get_name(self):
        return self.name
    
    def get_hungry(self):
        return self.hungry
    
    def set_name(self, name):
        self.name = name
        
        
class Cat:
    def meow(self):
        return "meowwwwwwww"


fido = Dog("Fido")
fido.set_name("Brody")
print(fido.get_name())

print(int("45"))