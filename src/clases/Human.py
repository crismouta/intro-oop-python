from src.clases.Character import Character


class Human(Character):
    def __init__(self, name, age, gender, rol):
        super().__init__(name, age)
        self.gender = gender
        self.rol = rol

    def introduce(self):
        return f'Hi, I am {self.name} and I am an human'
