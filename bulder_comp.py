class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None

    def set_cpu(self, cpu: str):
        self.cpu = cpu

    def set_ram(self, ram: str):
        self.ram = ram

    def set_storage(self, storage: str):
        self.storage = storage

    def __str__(self):
        return f"Computer with CPU: {self.cpu}, RAM: {self.ram}, Storage: {self.storage}"

from abc import ABC, abstractmethod

class ComputerBuilder(ABC):
    @abstractmethod
    def build_cpu(self):
        pass

    @abstractmethod
    def build_ram(self):
        pass

    @abstractmethod
    def build_storage(self):
        pass

    @abstractmethod
    def get_computer(self) -> Computer:
        pass

class GamingComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer()

    def build_cpu(self):
        self.computer.set_cpu("Intel i9")

    def build_ram(self):
        self.computer.set_ram("32GB")

    def build_storage(self):
        self.computer.set_storage("1TB SSD")

    def get_computer(self) -> Computer:
        return self.computer


class Director:
    def __init__(self, builder: ComputerBuilder):
        self.builder = builder

    def build_computer(self):
        self.builder.build_cpu()
        self.builder.build_ram()
        self.builder.build_storage()

def client_code():
    # Create a builder
    builder = GamingComputerBuilder()

    # Create a director and associate it with the builder
    director = Director(builder)

    # Direct the builder to construct the product
    director.build_computer()

    # Get the constructed product
    computer = builder.get_computer()
    print(computer)

if __name__ == "__main__":
    client_code()







