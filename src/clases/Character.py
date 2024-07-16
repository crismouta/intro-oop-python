class Character:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def introduce(self):
        return f'Hi, I am {self.__name}'

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

