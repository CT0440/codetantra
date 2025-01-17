class Car:
    def apply_brake(self):
        pass
    def start_gear(self):
        pass
    def checkfuel(self):
        return "Fuel suffiecient to drive"
    def start_engine(self):
        pass

class Seden(Car):
    def start_engine(self):
        return "seden engine started with key ignition"
    
    def start_gear(self, gear):
        self.gear = gear
        return f"seden gear shifted to {self.gear}"
    def apply_brake(self):
        return "Sudden brake applied smoothely"

class Sportscar(Car):
    def start_engine(self):
        return "seden engine started with keypush- button start"
    
    def start_gear(self, gear):
        self.gear = gear
        return f"seden gear shifted to {self.gear} for high speed performace"
    def apply_brake(self):
        return "Sudden brake applied with advanced ABS for instance responce"  

seden = Seden()
sports = Sportscar()

print(seden.start_engine())
print(seden.start_gear(3))
print(seden.apply_brake())
print(seden.checkfuel())

print()

print(sports.start_engine())
print(sports.start_gear(5))
print(sports.apply_brake())
print(seden.checkfuel())
