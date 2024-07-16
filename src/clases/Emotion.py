from src.clases.Character import Character
from src.clases.Skill import Skill


class Emotion(Character, Skill):
    def __init__(self, name, age, title, level, color):
        super().__init__(name, age)
        super().__init__(title, level)
        self.__color = color

    # def introduce(self):
    #     return f'{super().introduce()} and I am an Emotion'


print(Emotion.mro())







