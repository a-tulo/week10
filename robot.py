from inhabitant import Inhabitant
class Robot(Inhabitant):

  # A class attribute
  laws = "Protect, Obey and Survive"

  # A static method
  @staticmethod
  def the_laws():
    print(Robot.laws)

  # a class method
  @classmethod
  def assemble(cls):
    return cls("Assembled Robot")

  # An initialiser (special instance method)
  def __init__(self, name = "Robot", energy = 0):
    super().__init__(name, energy)

  def __repr__(self):
    return f'robot(name={self.name}, age={self.age})'

  def __str__(self):
    return f'Robot {self.name} is {self.age} years old.'

if __name__ == "__main__":
  robo = Robot()

  print(robo.__repr__())

  robo.grow()

  print(robo.__repr__())
