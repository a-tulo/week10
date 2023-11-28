from inhabitant import Inhabitant

class Human(Inhabitant):

    def __init__(self, name="Human", age=0):
        super().__init__(name, age)

    # method _init__, __repr__, __str__and display.
    def display(self):
        print(f"I am {self.name}")

    def __repr__(self):
        return f'human(name={self.name}, age ={self.age}, energy ={self.energy})'

    def __str__(self):
        return f'Human {self.name} is {self.age} years old and my energy is {self.energy}'


if __name__ == "__main__":
  # create an object of type Human
  human = Human()

  # display the current state of the object
  print(repr(human))

  # invoke the method move on the object
  human.move(10)

  print(repr(human))

