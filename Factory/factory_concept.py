from abc import ABC, abstractmethod

# Product interface
class Product(ABC):
    @abstractmethod
    def operation(self):
        pass

# ConcreteProduct implements Product
class ConcreteProduct(Product):
    def operation(self):
        print("Operation of ConcreteProduct")

# Creator abstract class with the factory method
class Creator(ABC):
    @abstractmethod
    def factory_method(self) -> Product:
        pass

    # A method that uses the product
    def do_something(self):
        product = self.factory_method()
        product.operation()

# ConcreteCreator implements the factory method to return a ConcreteProduct
class ConcreteCreator(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct()

# Client code
if __name__ == "__main__":
    creator = ConcreteCreator()
    creator.do_something()
