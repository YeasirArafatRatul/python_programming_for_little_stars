class Car:
  

    def __init__(self, model,year, highest_speed):
        self.model = model
        self.year = year
        self.speed = 0 #initial speed of every car
        self.higest_speed = highest_speed
  

    def lights(self):
        print("Lights On")


    def accelerate(self):
        if self.speed >= self.higest_speed:
            self.speed = self.higest_speed
        else:
            self.speed += 5
        return self.speed

    def brake(self):
        if self.speed <= 0:
            self.speed = 0
        else:
            self.speed -= 5
        return self.speed




corolla = Car("Toyota", "2020", 20)

print("Initial Speed", corolla.speed)
corolla.accelerate()
print("After accelaration", corolla.speed)

# print("After accelaration", corolla.speed)


car2 = Car("Lamborghini", "2020",100)

car2.brake()
car2.accelerate()
print(car2.speed)
