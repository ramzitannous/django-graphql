import abc


class Shape(abc.ABC):
    width: int
    height: int

    def __init__(self, width, height) -> None:
        super().__init__()
        self.width = width
        self.height = height

    @abc.abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def calculate_area(self):
        return self.width * self.height

    @staticmethod
    def say_hello():
        print("hello")

    @classmethod
    def say_bye(cls):
        print(cls.height)

