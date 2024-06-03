#Component Interface
class SimpleCoffee(Coffee):
    def cost(self):
        return 5

    def description(self):
        return "Simple coffee"

#Concrete Component
class SimpleCoffee(Coffee):
    def cost(self):
        return 5

    def description(self):
        return "Simple coffee"

#Decorator
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._decorated_coffee = coffee

    def cost(self):
        return self._decorated_coffee.cost()

    def description(self):
        return self._decorated_coffee.description()

#Concrete Decorators
class MilkDecorator(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)

    def cost(self):
        return self._decorated_coffee.cost() + 1

    def description(self):
        return f"{self._decorated_coffee.description()}, milk"

class SugarDecorator(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)

    def cost(self):
        return self._decorated_coffee.cost() + 0.5

    def description(self):
        return f"{self._decorated_coffee.description()}, sugar"

#Client Code

if __name__ == "__main__":
    coffee = SimpleCoffee()
    print(f"Cost: ${coffee.cost()}, Description: {coffee.description()}")

    coffee_with_milk = MilkDecorator(coffee)
    print(f"Cost: ${coffee_with_milk.cost()}, Description: {coffee_with_milk.description()}")

    coffee_with_milk_and_sugar = SugarDecorator(coffee_with_milk)
    print(f"Cost: ${coffee_with_milk_and_sugar.cost()}, Description: {coffee_with_milk_and_sugar.description()}")
