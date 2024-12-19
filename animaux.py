class Animal:
    def __init__(self, tete, corps, membres, habitat):
        self.tete = tete
        self.corps = corps
        self.membres = membres
        self.habitat = habitat

    def __str__(self):
        return f"{self.__class__.__name__} (Habitat: {self.habitat}, Tête: {self.tete}, Corps: {self.corps}, Membres: {self.membres})"

class Herbivore(Animal):
    def __init__(self, tete, corps, membres, habitat, alimentation="herbivore"):
        super().__init__(tete, corps, membres, habitat)
        self.alimentation = alimentation

    def __str__(self):
        return f"{super().__str__()} - Alimentation: {self.alimentation}"

class Carnivore(Animal):
    def __init__(self, tete, corps, membres, habitat, alimentation="carnivore"):
        super().__init__(tete, corps, membres, habitat)
        self.alimentation = alimentation

    def __str__(self):
        return f"{super().__str__()} - Alimentation: {self.alimentation}"
