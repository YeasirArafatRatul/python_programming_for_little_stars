class Car:
  

    def __init__(self, owner_name):
        self.owner = owner_name
        print(f"Engine Start {self.owner} Sir!")
        print(self)
        

    def lights(self):
        print(self)
        #print("Lights Start")



car1 = Car("Ratul")
car1.lights()

car2 = Car("Rabib")
car2.lights()

