class Bird:
    def fly(self):
        print("Most birds can fly")

class Crow(Bird):
    pass


class Penguin(Bird):
    def fly(self):
        print("Penguins cannot fly")

# Creating objects
bird = Bird()
penguin = Penguin()

bird.fly()  # Output: Most birds can fly
penguin.fly()  # Output: Penguins cannot fly

Crow().fly()  # Output: Penguins cannot fly
