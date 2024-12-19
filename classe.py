class Dossier:
    def __init__(self, nom, prenom, date_naissance, adresse, telephone, email):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.adresse = adresse
        self.telephone = telephone
        self.email = email

    def __str__(self):
        return (f"{self.prenom} {self.nom}, Né(e) le {self.date_naissance}\n"
                f"Adresse: {self.adresse}, Téléphone: {self.telephone}, Email: {self.email}")

class Personne:
    def __init__(self, dossier):
        self.dossier = dossier

    def __str__(self):
        return str(self.dossier)

class Professeur(Personne):
    def __init__(self, dossier, matiere):
        super().__init__(dossier)
        self.matiere = matiere

    def __str__(self):
        return f"Professeur de {self.matiere} : {super().__str__()}"

class Eleve(Personne):
    def __init__(self, dossier, niveau):
        super().__init__(dossier)
        self.niveau = niveau

    def __str__(self):
        return f"Élève (Niveau: {self.niveau}) : {super().__str__()}"

class Classe:
    def __init__(self, professeur, nom_classe):
        self.professeur = professeur
        self.nom_classe = nom_classe
        self.eleves = []

    def ajouter_eleve(self, eleve):
        if len(self.eleves) < 30:
            self.eleves.append(eleve)
        else:
            print("La classe est déjà pleine, impossible d'ajouter cet élève.")

    def afficher_classe(self):
        print(f"Classe : {self.nom_classe}")
        print(f"Professeur : {self.professeur}")
        print("Élèves :")
        for eleve in self.eleves:
            print(eleve)
