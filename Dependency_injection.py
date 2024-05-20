class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self, engine: Engine):
        self.engine = engine

    def start(self):
        return self.engine.start()

class ElectricEngine(Engine):
    def start(self):
        return "Electric engine started"

class FuelEngine(Engine):
    def start(self):
        return "Fuel engine started"

class Driver:
    def __init__(self, car: Car):
        self.car = car

    def drive(self):
        return self.car.start()

def main():
    electric_engine = ElectricEngine()
    fuel_engine = FuelEngine()

    electric_car = Car(electric_engine)
    fuel_car = Car(fuel_engine)

    driver1 = Driver(electric_car)
    driver2 = Driver(fuel_car)

    print(driver1.drive())  # Output: Electric engine started
    print(driver2.drive())  # Output: Fuel engine started

if __name__ == "__main__":
    main()
