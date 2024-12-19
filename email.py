from typing import List, Optional
import re


class AdresseEmail:
    def __init__(self, adresse: str):
        self.adresse = adresse
        if not self.est_valide():
            raise ValueError(f"Adresse email invalide : {adresse}")

    def est_valide(self) -> bool:
        # Validation simple du format de l'adresse email
        return re.match(r"[^@]+@[^@]+\.[^@]+", self.adresse) is not None


class TexteEmail:
    def __init__(self, titre: Optional[str] = None, corps: Optional[str] = None):
        self.titre = titre
        self.corps = corps


class FichierJoint:
    def __init__(self, nom: str, contenu: bytes):
        self.nom = nom
        self.contenu = contenu


class Email:
    def __init__(
            self,
            expediteur: AdresseEmail,
            destinataire: AdresseEmail,
            texte: TexteEmail,
            fichiers: Optional[List[FichierJoint]] = None
    ):
        self.expediteur = expediteur
        self.destinataire = destinataire
        self.texte = texte
        self.fichiers = fichiers if fichiers is not None else []

    def envoyer(self):
        print(f"Envoi de l'email de {self.expediteur.adresse} à {self.destinataire.adresse}")
        if self.texte.titre:
            print(f"Titre: {self.texte.titre}")
        if self.texte.corps:
            print(f"Corps: {self.texte.corps}")
        if self.fichiers:
            print(f"Fichiers joints: {[f.nom for f in self.fichiers]}")
