from abc import ABC, abstractmethod
class BasePizza(ABC):
    @abstractmethod
    def cost(self):
        pass

class ChessPizza(BasePizza):
    def cost(self):
       return 100

class VegPizza(BasePizza):
    def cost(self):
       return 150

class NonVegPizza(BasePizza):
    def cost(self):
       return 200


class ToppingInterface(BasePizza):
    @abstractmethod
    def cost(self):
      pass

class CheeseTopping(BasePizza):
    def __init__(self, basePizza: BasePizza):
        self.basePizza = basePizza
    def cost(self):
       return self.basePizza.cost() + 20


class OnionTopping(BasePizza):
    def __init__(self, basePizza: BasePizza):
        self.basePizza = basePizza
    def cost(self):
       return self.basePizza.cost() + 10

class SpicesTopping(BasePizza):
    def __init__(self, basePizza: BasePizza):
        self.basePizza = basePizza
    def cost(self):
       return self.basePizza.cost() + 5

pizza = ChessPizza()
pizza.cost()
pizza = OnionTopping(pizza)
pizza = CheeseTopping(pizza)
print(pizza.cost())
