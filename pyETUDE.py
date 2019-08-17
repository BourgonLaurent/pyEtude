intro = """
                 ███████╗████████╗██╗   ██╗██████╗ ███████╗
                 ██╔════╝╚══██╔══╝██║   ██║██╔══██╗██╔════╝
██████╗ ██╗   ██╗█████╗     ██║   ██║   ██║██║  ██║█████╗  
██╔══██╗╚██╗ ██╔╝██╔══╝     ██║   ██║   ██║██║  ██║██╔══╝  
██████╔╝ ╚████╔╝ ███████╗   ██║   ╚██████╔╝██████╔╝███████╗
██╔═══╝   ╚██╔╝  ╚══════╝   ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝
██║        ██║   MIT © Laurent Bourgon 2019
╚═╝        ╚═╝   v0.1.0~b1
"""

import os
import zipfile

class front_end():
    """## Interface qui pose des questions et qui l'envoie à la classe {Document}
    """
    def __init__(self):
        self.main()

    def main(self):
        self.intro()

    def intro(self):
        print(intro)

    def questions(self):
        pass

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

        self.base = matiere + "-" + numero
        self.folder = self.base + "_tmpyEtude"
        self.filename = self.folder + ".docx"

        self.main()

    def main(self):
        self.exportWord(self.model, self.folder)
        self.packWord(self.folder, self.filename)
        self.cleanTemp(self.folder)

    def exportWord(self, model:str, folder:str) -> str:
        """## Extract the specified `.zip` file

        ### Arguments:\n
            \tmodel {str} -- file that will be extracted (Do not forget the .docx!)\n
            \tfolder {str} -- folder that will receive the extracted file

        ### Returns:\n
            \tstr -- the name of the folder where it was extracted
        """

        with zipfile.ZipFile(model, "r") as model_file:
            model_file.extractall(folder)
            model_file.close()
        return folder

    def modifyOptions(self):
        pass

    def modifySection(self):
        pass

    def packWord(self, folder:str, final:str) -> str:
        """## Zip the folder specified
        This will only zip the contents of the folder, not the base folder

        ### Arguments:\n
            \tfolder {str} -- the folder that will be zipped\n
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
        else:
            raise NotADirectoryError
        
        return folder

if __name__ == "__main__":
    titre = ""
    sous_titre = ""
    auteur = ""
    secondaire = ""
    matiere = ""
    numero = ""
    p_section = ""

    fe = front_end()
    document = Document(fe.titre, fe.sous_titre, fe.auteur, fe.secondaire, fe.matiere, fe.numero, fe.p_section, fe.model)