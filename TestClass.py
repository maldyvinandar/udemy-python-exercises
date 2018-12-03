class Dog():
    """ It is a sample class dog"""


species = 'mammal'


def __init__(self, breed, name, spots):
    """Init the class"""
    # Attributes

    self.breed = breed
    self.name = name
    self.spots = spots


def bark(self):
    """Bark method"""
    print("WOOF! My name is {}".format(self.name)")


my_dog = Dog('Lab', 'Frankie')

my_dog.bark()
