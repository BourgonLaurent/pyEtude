# -*- coding: utf-8 -*-/
"""
                 ███████╗████████╗██╗   ██╗██████╗ ███████╗
                 ██╔════╝╚══██╔══╝██║   ██║██╔══██╗██╔════╝
██████╗ ██╗   ██╗█████╗     ██║   ██║   ██║██║  ██║█████╗  
██╔══██╗╚██╗ ██╔╝██╔══╝     ██║   ██║   ██║██║  ██║██╔══╝  
██████╔╝ ╚████╔╝ ███████╗   ██║   ╚██████╔╝██████╔╝███████╗
██╔═══╝   ╚██╔╝  ╚══════╝   ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝
██║        ██║   MIT © Laurent Bourgon 2019
╚═╝        ╚═╝   v2.0.0
"""

import os, sys, zipfile, json, tkinter.filedialog, webbrowser
from tkinter import *

TITLE = r"pyÉtude"
VERSION = r"v2.0.0~b1"

class Configurator:
    """## Gestionnaire des auteurs et du Secondaire
    Si le fichier `pyEtude.json` n'existe pas, le configurateur demandera les infos

    Dans tous les cas: Lit le fichier et envoie les informations à `frontEnd()`
    """
    def __init__(self):
        """## Démarre le configurateur
        1. Met des valeurs de bases pour self.auteur et self.secondaire si jamais l'utilisateur répond en ne mettant rien
        2. Lance le configurateur
        """
        self.auteur = "Laurent Bourgon"
        self.secondaire = "Secondaire 5 - 2019-2020"
        self.checkRun()
    
    def checkRun(self):
        """## Vérifie si le fichier de configuration existe
        """
        if os.path.isfile("pyEtude.json"):
            json_data = self.readJSON()
        else:
            self.createJSON_GUI()
    
    def createJSON_GUI(self):
        """## GUI tkinter qui demande les 2 informations
        """
        self.configurator = Tk()
        self.configurator.title(TITLE + " - " + VERSION )

        self.frame = LabelFrame(self.configurator, text="Configurateur",width=250)
        self.frame.grid(row=0,column=0,padx=5, pady=5)

        self.frame_title = Label(self.frame, text="Veuillez répondre aux questions suivantes",justify=CENTER).grid(row=0,column=0)

        self.frame_auteur = LabelFrame(self.frame, text="Auteur")
        self.frame_auteur.grid(row=1,column=0,stick=W,padx=5)
        self.configurator_auteur_entry = Entry(self.frame_auteur,font="Garamond 12",width=30)
        self.configurator_auteur_entry.grid(row=0,column=0,padx=2)
        Placeholder().add_placeholder_to(self.configurator_auteur_entry, self.auteur)

        self.frame_secondaire = LabelFrame(self.frame, text="Secondaire")
        self.frame_secondaire.grid(row=2,column=0,stick=W,padx=5,pady=5)
        self.configurator_secondaire_entry = Entry(self.frame_secondaire,font="Garamond 12",width=30)
        self.configurator_secondaire_entry.grid(row=0,column=0,padx=2)
        Placeholder().add_placeholder_to(self.configurator_secondaire_entry, self.secondaire)

        self.configurator_generator_button = Button(self.frame, text="Appliquer et Enregistrer", command= lambda: self.getEntries()).grid(row=3,column=0,pady=5)
        self.configurator.mainloop()

    def getEntries(self):
        """## Action qui permet de stocker les informations dans les `Entry`
        """
        # Prend les infos
        self.auteur = self.configurator_auteur_entry.get().replace("&","")
        self.secondaire = self.configurator_secondaire_entry.get().replace("&","")
        # Supprime le configurateur
        self.configurator.destroy()

        self.json_data = dict()  # Crée le dictionnaire de données
        self.json_data["auteur"] = self.auteur
        self.json_data["secondaire"] = self.secondaire
        
        # Crée le fichier de configuration
        with open("pyEtude.json", "w") as json_f:
            json.dump(self.json_data, json_f)
        # Lance frontEnd() avec les infos indiquées
        frontEnd(self.json_data)

    def readJSON(self):
        """## Action qui lit les informations du fichier de configuration
        """
        # Ouvre le fichier de config
        with open("pyEtude.json") as json_f:
            self.json_data = json.load(json_f)  # Lit le fichier de config
        # Lance frontEnd() avec les infos indiquées
        frontEnd(self.json_data)

class Placeholder:
    """## Classe qui permet d'ajouter un placeholder aux `Entry`
    """
    def __init__(self):
        __slots__ = 'normal_color', 'normal_font', 'placeholder_text', 'placeholder_color', 'placeholder_font', 'with_placeholder'
    def add_placeholder_to(self, entry, placeholder, color="grey", font=None):
        normal_color = entry.cget("fg")
        normal_font = entry.cget("font")
        if font is None:
            font = normal_font
        state = Placeholder()
        state.normal_color=normal_color
        state.normal_font=normal_font
        state.placeholder_color=color
        state.placeholder_font=font
        state.placeholder_text = placeholder
        state.with_placeholder=True
        def on_focusin(event, entry=entry, state=state):
            if state.with_placeholder:
                entry.delete(0, "end")
                entry.config(fg = state.normal_color, font=state.normal_font)
                state.with_placeholder = False
        def on_focusout(event, entry=entry, state=state):
            if entry.get() == '':
                entry.insert(0, state.placeholder_text)
                entry.config(fg = state.placeholder_color, font=state.placeholder_font)
                state.with_placeholder = True
        entry.insert(0, placeholder)
        entry.config(fg = color, font=font)
        entry.bind('<FocusIn>', on_focusin, add="+")
        entry.bind('<FocusOut>', on_focusout, add="+")
        entry.placeholder_state = state
        return state

class frontEnd:
    """## Main GUI du programme
    """
    def __init__(self, jsonData):
        """## Lance le programme principal
        
        ### Arguments:\n
            \tjsonData {dict} -- Un dictionnaire ayant les auteurs et le secondaire
        """
        # Extrait les infos dans jsonData
        self.auteur = jsonData["auteur"]
        self.secondaire = jsonData["secondaire"]
        # Par défaut, il n'y a pas de chemins customs
        self.custom_directory = False
        self.custom_name = False
        # Information par défaut, afin de montrer un exemple à l'utilisateur
        self.titre = "Ceci est un exemple"
        self.soustitre = "Newton, grand physicien"
        self.matiere = "PHY"
        self.numero = "0716"
        self.section = "La Loi de l'Inertie"
        self.model = "model.docx"

        self.main()  # Lance le programme principal
        self.root.mainloop()  # Permet au programme de rester ouvert

    def main(self):
        """## Fonction "maison" qui regroupe les éléments de bases et renvoies aux autres composants du GUI
        """
        self.root = Tk()  # Crée une fenêtre
        self.root.title(TITLE + " - " + VERSION)  # Met un titre à cette fenêtre

        self.frame = Frame(self.root)  # Crée un frame principal
        self.frame.grid(row=0, column=0, pady=3)  # Place le frame principal

        self.input = LabelFrame(self.frame, text="Information")  # Crée un frame pour la section input
        self.input.grid(row=0, column=0, sticky=NW, padx=5)

        self.generate = Frame(self.frame)  # Crée un frame pour la section generate
        self.generate.grid(row=1, column=0, sticky=NW, padx=5)

        self.options = Frame(self.frame)  # Crée un frame pour la section options
        self.options.grid(row=0, column=1, sticky=SE, padx=5)

        self.settings = Frame(self.frame)  # Crée un frame pour la section settings
        self.settings.grid(row=1, column=1, sticky=SE, padx=5)
        # Renvoie aux autres composantes du GUI
        self.showInput()
        self.showOptions()
        self.showGenerate()
        self.showSettings()

    def showInput(self):
        
        def callbackEntry(name="", index="", mode=""):
            """## Stocke les informations dans les `Entry`
            
            ### Keyword Arguments:\n
                \tname {str} -- Nom du StringVar UTILE (default: {""})
                \tindex {str} -- Index INUTILE (default: {""})
                \tmode {str} -- Model INUTILE (default: {""})
                * Les arguments inutiles sont là puisque tkinter envoie toujours 3 arguments
            """
            # Regarde quelle variable changer
            if name == "titre":
                self.titre = self.frame_titre_entry.get().replace("&","")
            elif name == "soustitre":
                self.soustitre = self.frame_soustitre_entry.get().replace("&","")
            elif name == "matiere":
                self.matiere = self.frame_matiere_entry.get().replace("&","")
            elif name == "numero":
                self.numero = self.frame_numero_entry.get().replace("&","")
            elif name == "section":
                self.section = self.frame_section_entry.get().replace("&","")
            else:  # Si le nom n'est pas identifier, tout sera mis à jour
                self.titre = self.frame_titre_entry.get().replace("&","")
                self.soustitre = self.frame_soustitre_entry.get().replace("&","")
                self.matiere = self.frame_matiere_entry.get().replace("&","")
                self.numero = self.frame_numero_entry.get().replace("&","")
                self.section = self.frame_section_entry.get().replace("&","")
            self.refreshValues()  # Met à jour les valeurs sur le paneau
        
        # Crée les StringVar qui feront le callback
        self.frame_titre_entry_sv = StringVar(name="titre")
        self.frame_titre_entry_sv.trace_add("write", callbackEntry)

        self.frame_soustitre_entry_sv = StringVar(name="soustitre")
        self.frame_soustitre_entry_sv.trace_add("write", callbackEntry)

        self.frame_matiere_entry_sv = StringVar(name="matiere")
        self.frame_matiere_entry_sv.trace_add("write", callbackEntry)

        self.frame_numero_entry_sv = StringVar(name="numero")
        self.frame_numero_entry_sv.trace_add("write", callbackEntry)
        
        self.frame_section_entry_sv = StringVar(name="section")
        self.frame_section_entry_sv.trace_add("write", callbackEntry)


        # Met un Frame à lasection Titre-SousTitre
        self.frame_title = LabelFrame(self.input, text="")
        self.frame_title.grid(row=0, column=0, padx=5, pady=5)

        self.frame_titre = LabelFrame(self.frame_title, text="Titre")  # Crée un Frame avec un Label comme titre
        self.frame_titre.grid(row=0, column=0, padx=5, pady=3)  # Le place
        self.frame_titre_entry = Entry(self.frame_titre, font="Garamond 12", justify=CENTER, textvariable=self.frame_titre_entry_sv)  # Crée une entrée pour la section
        self.frame_titre_entry.grid(row=0,column=0,padx=5,pady=5)  # La place
        Placeholder().add_placeholder_to(self.frame_titre_entry, self.titre)  # Crée le callback avec le StringVar créer plus tôt

        self.frame_soustitre = LabelFrame(self.frame_title, text="Sous-Titre")
        self.frame_soustitre.grid(row=1, column=0, padx=5, pady=1.5)
        self.frame_soustitre_entry = Entry(self.frame_soustitre, font="Garamond 12", justify=CENTER, textvariable=self.frame_soustitre_entry_sv)
        self.frame_soustitre_entry.grid(row=0,column=0,padx=5,pady=5)
        Placeholder().add_placeholder_to(self.frame_soustitre_entry, self.soustitre)

        # Met un Frame à la section Matiere-Numero
        self.frame_cours = LabelFrame(self.input, text="")
        self.frame_cours.grid(row=1,column=0, padx=5,pady=5)

        self.frame_matiere = LabelFrame(self.frame_cours, text="Matière")
        self.frame_matiere.grid(row=1, column=0, padx=5, pady=3)
        self.frame_matiere_entry = Entry(self.frame_matiere, font="Garamond 12", justify=CENTER, textvariable=self.frame_matiere_entry_sv)
        self.frame_matiere_entry.grid(row=0,column=0,padx=5,pady=5)
        Placeholder().add_placeholder_to(self.frame_matiere_entry, self.matiere)

        self.frame_numero = LabelFrame(self.frame_cours, text="Numéro")
        self.frame_numero.grid(row=2, column=0, padx=5, pady=1.5)
        self.frame_numero_entry = Entry(self.frame_numero, font="Garamond 12", justify=CENTER, textvariable=self.frame_numero_entry_sv)
        self.frame_numero_entry.grid(row=0,column=0,padx=5,pady=5)
        Placeholder().add_placeholder_to(self.frame_numero_entry, self.numero)

        # Met un Frame à la section Première Section
        self.frame_section = LabelFrame(self.input, text="Première Section")
        self.frame_section.grid(row=3, column=0, padx=5, pady=3, ipadx=2)
        self.frame_section_label = Label(self.frame_section, text="1.", font="Garamond 12", justify=RIGHT).grid(row=0,column=0)
        self.frame_section_entry = Entry(self.frame_section, font="Garamond 12", justify=CENTER, textvariable=self.frame_section_entry_sv)
        self.frame_section_entry.grid(row=0,column=1,pady=5)
        Placeholder().add_placeholder_to(self.frame_section_entry, self.section)

    def showOptions(self):
        self.frame_options = LabelFrame(self.options, text="Options")
        self.frame_options.grid(row=0,column=0)

        self.frame_options_auteur = LabelFrame(self.frame_options, text="Auteur")
        self.frame_options_auteur.grid(row=0,column=0,padx=5)
        self.options_auteur_label = Label(self.frame_options_auteur, text=self.auteur, font="Garamond 13 italic").grid(row=0,column=0)

        self.frame_options_secondaire = LabelFrame(self.frame_options, text="Secondaire")
        self.frame_options_secondaire.grid(row=1,column=0,padx=5, pady=2)
        self.options_secondaire_label = Label(self.frame_options_secondaire, text=self.secondaire, font="Garamond 13 italic").grid(row=0,column=0)

        self.frame_values = LabelFrame(self.options, text="Valeurs")
        self.frame_values.grid(row=1,column=0,sticky=NW)

    def refreshValues(self):
        try:
            self.values_text.destroy()
        except:
            pass
        if self.custom_directory == True:
            self.filepath = os.path.join(self.directory_name, f"{self.matiere}-{self.numero}.docx")
        elif self.custom_name == True:
            self.filepath = self.file_directory_name
        else:
            self.filepath = os.path.join(os.getcwd(), f"{self.matiere}-{self.numero}.docx")
        try:
            self.values_text = Message(self.frame_values, width=250, text=f"Titre: {self.titre}\nSous-Titre: {self.soustitre}\nMatière: {self.matiere}\nNuméro: {self.numero}\nSection: 1. {self.section}\n\nAuteur: {self.auteur}\nSecondaire: {self.secondaire}\n\n{self.filepath}")
            self.values_text.grid(row=0,column=0)
        except AttributeError:
            pass
    
    def showGenerate(self):
        def browserButton():
            self.directory_name = tkinter.filedialog.askdirectory()
            if not self.directory_name:
                print("hello")
                return None
            self.custom_directory = True
            self.refreshValues()
        def fileButton():
            self.file_directory_name = tkinter.filedialog.asksaveasfilename(filetypes = (("Document Word","*.docx"),))
            if not self.file_directory_name:
                return None
            if not self.file_directory_name.endswith(".docx"):
                self.file_directory_name = self.file_directory_name + ".docx"
            self.custom_name = True
            self.refreshValues()
        def generateButton():
            Document(self.titre, self.soustitre, self.auteur, self.secondaire, self.matiere, self.numero, self.section, self.model, self.filepath)
        
        

        self.refreshValues()

        self.frame_generate = LabelFrame(self.generate, text="Générer")
        self.frame_generate.grid(row=0,column=0,sticky=NW)
        self.generate_button = Button(self.frame_generate, text="Générer", font=("", 15, "bold"), command=lambda: generateButton())
        self.generate_button.grid(row=0,column=0,padx=10,pady=9)
        self.file_button = Button(self.frame_generate, text="Enregistrer sous...", font=("",8,"italic"), command= lambda: fileButton())
        self.file_button.grid(row=1,column=0,padx=10,pady=2)
        self.browser_button = Button(self.frame_generate, text="Choisir le dossier de sortie", font=("",8,"italic"), command=lambda: browserButton()).grid(row=2,column=0,padx=10,pady=3)

    def showSettings(self):
        def modifyOptions(self):
            os.remove("pyEtude.json")
            os.execl(sys.executable, 'python', __file__, *sys.argv[1:])
        
        self.frame_settings = LabelFrame(self.settings, text="Réglages")
        self.frame_settings.grid(row=0,column=0)

        self.settings_options_button = Button(self.frame_settings, width=19, text="Modifier les Options", command=lambda: modifyOptions(self)).grid(row=0,column=0,padx=5,pady=3)

        self.settings_model_button = Button(self.frame_settings, width=19, text="Modifier le Modèle Word", command=lambda: self.showModelWindow()).grid(row=1,column=0,padx=5,pady=3)
        
        self.about_github = Label(self.frame_settings, text="Projet GitHub", fg="blue", cursor="hand2",justify=CENTER)
        self.about_github.grid(row=2,column=0)
        self.about_github.bind("<Button-1>", lambda e: webbrowser.open_new(r"https://github.com/BourgonLaurent/pyEtude"))
        
        self.about_license = Label(self.frame_settings, text="Sous la license MIT\n© Laurent Bourgon 2019", fg="blue", cursor="hand2", font=("",8,"italic"))
        self.about_license.grid(row=3,column=0,sticky=S)
        self.about_license.bind("<Button-1>", lambda e: webbrowser.open_new(r"https://github.com/BourgonLaurent/pyEtude/blob/master/LICENSE"))
        # self.settings_a_propos = Button(self.frame_settings, width=19, text="À Propos", command=lambda: self.aboutProgram()).grid(row=2,column=0,padx=5,pady=3)
    
    def showAbout(self):
        self.frame_about = LabelFrame(self.about, text="À Propos")
        self.frame_about.grid()
        
        self.about_github = Label(self.frame_about, text="Github here", fg="blue", cursor="hand2")
        self.about_github.grid(row=1,column=0,sticky=N)
        self.about_github.bind("<Button-1>", lambda e: webbrowser.open_new(r"https://github.com/BourgonLaurent/pyEtude"))
    
    def showModelWindow(self):
        self.model_window = Toplevel()
        self.model_window.title(f"{TITLE} - Modifier le Modèle Word")
        self.model_window.geometry("362x54")

        self.model_frame = Frame(self.model_window)
        self.model_frame.grid(padx=125, pady=5, sticky=N)

        self.model_frame_default = LabelFrame(self.model_frame, text="Modèle 1: Défaut")
        self.model_frame_default.grid(sticky=N)

        self.default_label = Label(self.model_frame_default, text="Défaut").grid(row=0,column=1)
        self.default_radio = Radiobutton(self.model_frame_default, text="").grid(row=0,column=0)

        self.model_window.mainloop()

class Document:
    def __init__(self, titre, soustitre, auteur, secondaire, matiere, numero, section, model, filepath):
        self.titre = titre
        self.soustitre = soustitre
        self.auteur = auteur
        self.secondaire = secondaire
        self.matiere = matiere
        self.numero = numero
        self.section = section
        self.model = model
        self.filepath = filepath

        self.options = {"pyETUDE_Titre": titre,
                    "pyETUDE_SousTitre": soustitre,
                    "pyETUDE_Matiere": matiere,
                    "pyETUDE_Auteur": auteur,
                    "pyETUDE_Sec": secondaire,
                    "pyETUDE_Num": numero}
        self.sections = {"sectionpy": section}

        self.folder = f"{matiere}-{numero}_tmpyETUDE"

        self.main()

    def main(self):
        self.exportWord(self.model, self.folder)

        self.modifyOptions(os.path.join(self.folder, "docProps", "core.xml"), self.options)
        self.modifyOptions(os.path.join(self.folder, "word", "document.xml"), self.sections)

        self.packWord(self.folder, self.filepath)
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
        print(f"\nLe document a été créé: {self.filepath}")
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
    Configurator()