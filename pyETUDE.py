# -*- coding: utf-8 -*-/
intro = """
                 ███████╗████████╗██╗   ██╗██████╗ ███████╗
                 ██╔════╝╚══██╔══╝██║   ██║██╔══██╗██╔════╝
██████╗ ██╗   ██╗█████╗     ██║   ██║   ██║██║  ██║█████╗  
██╔══██╗╚██╗ ██╔╝██╔══╝     ██║   ██║   ██║██║  ██║██╔══╝  
██████╔╝ ╚████╔╝ ███████╗   ██║   ╚██████╔╝██████╔╝███████╗
██╔═══╝   ╚██╔╝  ╚══════╝   ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝
██║        ██║   MIT © Laurent Bourgon 2019
╚═╝        ╚═╝   v1.0.0
"""

import os
import zipfile
import json

class front_end():
    """## Interface qui pose des questions et qui l'envoie à la classe {Document}
    """
    def __init__(self):
        self.main()

    def main(self):
        self.intro()
        self.printConfig(self.takeJSON())
        self.questions()

    def intro(self):
        print(intro)

    def takeJSON(self) -> dict:
        """## Lance le configurateur si le fichier .json n'existe pas et enregistre le fichier dans la mémoire
        
        
        ### Returns:\n
            \tdict -- Dictionnaire contenant les valeurs
        """
        if os.path.isfile("pyEtude.json"):
            json_d = self.readJSON()
        else:
            self.createJSON()
            json_d = self.readJSON()
        return json_d

    def createJSON(self) -> None:
        """## Crée le fichier .json qui sera utilisé par la suite
        
        ### Returns:\n
            \tNone -- Ne retourne rien
        """
        print("Ceci est la première fois que vous exécutez ce programme, vous allez devoir passer par le configurateur\n")
        json_d = dict()
        json_d["auteur"] = input("Quel est votre nom? (ex. Laurent Bourgon) (Sera affiché sur la page de garde et l'en-tête): ")
        json_d["secondaire"] = input("Quel est votre année? (ex. Secondaire 5 - 2019-2020) (Sera affiché dans le pied de page): ")
        print("\n")
        json_d["model"] = "model.docx" # Ceci changera lorsque plusieurs modèles seront disponibles
        with open("pyEtude.json", "w") as json_f:
            json.dump(json_d, json_f)
        return None

    def readJSON(self) -> dict:
        """## Lit le fichier .json et le transforme en dictionnaire
        
        ### Returns:\n
            \tdict -- Dictionnaire qui contient toutes les valeurs avec les clés
        """
        with open("pyEtude.json","r") as json_f:
            json_data = json.load(json_f)
        return json_data

    def printConfig(self, dictionnary:dict):
        """## Le dictionnaire .json converti en attribut de classe
        
        ### Arguments:\n
            \tdictionnary {dict} -- Le dictionnaire .json
        """
        self.auteur = dictionnary["auteur"]
        self.secondaire = dictionnary["secondaire"]
        self.model = dictionnary["model"]

        print("Voici les informations pré-configurées:")
        print(f"\tAuteur: {self.auteur}\n\tSecondaire: {self.secondaire}\n\tModèle chargé: {self.model}")
    
    def questions(self):
        print("\nChargement des entrées personnalisées...\n")
        # .replace("&","") will remove & that causes problems with Word
        self.titre = input("Titre (ex. Chapitre 5): ").replace("&","")
        self.soustitre = input("Sous-Titre (ex. Les lois de Newton): ").replace("&","")
        self.matiere = input("Matière, courte (ex. PHY): ").replace("&","")
        self.numero = input("Numéro/Chapitre, court (ex. 1607 ou CHP5): ").replace("&","")
        self.section = input("Nom du premier titre (ex. La Première Loi): ").replace("&","")
    

class Document():
    """## Modifie le modèle selon les arguments fournis

    ### Arguments:\n
        \ttitre {str} -- Titre de la page de garde
        \tsoustitre {str} -- Sous-titre de la page de garde
        \tauteur {str} -- Nom de l'auteur
        \tsecondaire {str} -- Pied de page, coin gauche
        \tmatiere {str} -- Pied de page, centre
        \tnumero {str} -- Pied de page, centre
        \tsection {str} -- Premier titre
        \tmodel {str} -- Nom du fichier modèle (Il faut que ce soit un .docx!)
    
    ### Returns:\n
        \t[type] -- [description]
    """

    def __init__(self, titre, soustitre, auteur, secondaire, matiere, numero, section, model):
        self.titre = titre
        self.soustitre = soustitre
        self.auteur = auteur
        self.secondaire = secondaire
        self.matiere = matiere
        self.numero = numero
        self.section = section
        self.model = model

        self.options = {"pyETUDE_Titre": titre,
                    "pyETUDE_SousTitre": soustitre,
                    "pyETUDE_Matiere": matiere,
                    "pyETUDE_Auteur": auteur,
                    "pyETUDE_Sec": secondaire,
                    "pyETUDE_Num": numero}
        self.sections = {"sectionpy": section}

        self.base = matiere + "-" + numero
        self.folder = self.base + "_tmpyEtude"
        self.filename = self.base + ".docx"

        self.main()

    def main(self):
        self.exportWord(self.model, self.folder)

        self.modifyOptions(self.folder + "\\docProps\\core.xml", self.options)
        self.modifyOptions(self.folder + "\\word\\document.xml", self.sections)

        self.packWord(self.folder, self.filename)
        self.cleanTemp(self.folder)

    def exportWord(self, model:str, folder:str) -> str:
        """## Extract the specified `.zip` file

        ### Arguments:\n
            \tmodel {str} -- file that will be extracted (Do not forget the .docx!)
            \tfolder {str} -- folder that will receive the extracted file

        ### Returns:\n
            \tstr -- the name of the folder where it was extracted
        """

        with zipfile.ZipFile(model, "r") as model_file:
            model_file.extractall(folder)
            model_file.close()
        return folder

    def modifyOptions(self, path:str, info:dict) -> str:
        """## Send command to {self.searchAndReplace} for all values in a dictionnary
        
        ### Arguments:\n
            \tpath {str} -- The path of the file to be modified
            \tinfo {dict} -- A dictionnary in this format {"to search":"to replace"}
        
        ### Returns:\n
            \tstr -- Returns the name of the file modified
        """
        for search, replace in info.items():
            self.searchAndReplace(path, search, replace)
        return path

    def searchAndReplace(self, infile:str, search:str, replace:str) -> str:
        """## Search the specified file with the keyword given and replaces it with the third argument
        
        ### Arguments:\n
            \tinfile {str} -- The file to change
            \tsearch {str} -- The word to replace
            \treplace {str} -- The word that will be replaced by {search}

        ### Returns:\n
            \tstr -- Returns the name of the file modified
        """
        if os.path.isfile(infile):
            with open(infile, "r", encoding="utf8") as in_f:
                data_f = in_f.read()
                with open(infile, "w", encoding='utf8') as out_f:
                    out_f.write(data_f.replace(search, replace))
        else:
            raise FileNotFoundError
        return infile


    def packWord(self, folder:str, final:str) -> str:
        """## Zip the folder specified
        This will only zip the contents of the folder, not the base folder

        ### Arguments:\n
            \tfolder {str} -- the folder that will be zipped
            \tfinal {str} -- the name of the archive (Do not forget the .docx!)

        ### Returns:\n
            \tstr -- the name of the zip file that was created
        """

        with zipfile.ZipFile(final, "w") as zip_file:
            for root, dirs, files in os.walk(folder):
                zip_file.write(os.path.join(root, "."))

                for File in files:
                    filePath = os.path.join(root, File)
                    inZipPath = filePath.replace(folder, "", 1).lstrip("\\/")
                    zip_file.write(filePath, inZipPath)
        print(f"\nLe document {final} a été créé dans {os.getcwd()}")
        return final

    def cleanTemp(self, folder:str) -> str:
        """## Clean the temporary folder
        DANGEROUS: THIS WILL DELETE ALL THE FILES IN THE SPECIFIED FOLDER!!
        
        ### Arguments:\n
            \tfolder {str} -- The folder that will be deleted
        
        ### Raises:\n
            \tNotADirectoryError: The specified folder is not a folder
        
        ### Returns:\n
            \tstr -- Returns the name of the folder deleted
        """
        if os.path.isdir(folder):
            for root, dirs, files in os.walk(folder, topdown=False):
                for File in files:
                    os.remove(os.path.join(root, File))
                for Dir in dirs:
                    os.rmdir(os.path.join(root, Dir))
            os.rmdir(folder)
        else:
            raise NotADirectoryError
        
        return folder

if __name__ == "__main__":
    fe = front_end()
    doc = Document(fe.titre, fe.soustitre, fe.auteur, fe.secondaire, fe.matiere, fe.numero, fe.section, fe.model)