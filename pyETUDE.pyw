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

from tkinter import *  # pylint: disable=unused-wildcard-import
from tkinter.ttk import *  # pylint: disable=unused-wildcard-import
import json, locale, os, re, sys, tkinter.filedialog, tkinter.messagebox, urllib.request, webbrowser, zipfile

TITLE = r"pyÉtude"
VERSION = r"v2.0.0"

os.chdir(os.path.realpath(__file__).replace(os.path.basename(__file__), ""))  # Accède aux fichiers depuis la racine du programme, et non l'endroit du shell

try:
    locale.setlocale(locale.LC_ALL, "")  # Met la langue en français en prenant en charge les accents (UTF-8)
except locale.Error:
    if sys.platform == "darwin":  # macOS retourne toujours une erreur
        assert EnvironmentError
    else:
        Tk().withdraw()
        tkinter.messagebox.showerror("ERREUR LOCALE", "Une langue \"UTF-8\" n'est pas trouvée\npyÉtude va se lancer en mode compatibilité\nCela pourrait entraîner une instabilité du programme")
        assert EnvironmentError
    locale.setlocale(locale.LC_ALL, (None, None))

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
        self.other_number = 1

        self.mat_dict = {
            "Anglais":"ANG",
            "Arts":"ART",
            "Chimie":"CHM",
            "Éducation Financière":"EFI",
            "Éducation Physique":"EDP",
            "Éthique et Culture Religieuse":"ECR",
            "Français":"FRA",
            "Mathématiques":"MAT",
            "Monde Contemporain":"MDC",
            "Physique":"PHY"
        }
        
        self.checkRun()
    
    def checkRun(self):
        """## Vérifie si le fichier de configuration existe
        """
        if os.path.isfile("pyEtude.json"):
            self.readJSON()
        else:
            self.createJSON_GUI()
    
    def createJSON_GUI(self):
        """## GUI tkinter qui demande les 2 informations
        """
        self.configurator = Tk()  # Initialise le configurateur
        self.configurator.title(TITLE + " - " + VERSION )
        self.configurator.resizable(False, False)

        self.style = Style()
        if os.name == "nt":
            self.style.theme_use("vista")
        else:
            self.style.theme_use("clam")
        self.style.configure("NormalEntry.TEntry", font=("Garamond", 12))
        self.style.configure("PlaceHolderEntry.TEntry", foreground="grey")

        # Ajoute un LabelFrame principal
        self.frame = LabelFrame(self.configurator, text="Configurateur",width=250)
        self.frame.grid(row=0,column=0,padx=5, pady=5)
        # Crée la question dans le LabelFrame principal
        self.frame_title = Label(self.frame, text="Veuillez répondre aux questions suivantes",justify=CENTER).grid(row=0,column=0)
        # Crée un frame à l'intérieur du princiapl pour demander l'auteur
        self.frame_auteur = LabelFrame(self.frame, text="Auteur")
        self.frame_auteur.grid(row=1,column=0,stick=W,padx=5,columnspan=2)

        self.configurator_auteur_entry = Entry(self.frame_auteur, style="NormalEntry.TEntry", font=("Garamond", 12), width=30)
        self.configurator_auteur_entry.grid(row=0,column=0,padx=2)
        Placeholder().add_placeholder_to(self.configurator_auteur_entry, self.auteur)

        # Crée un frame à l'intérieur du princiapl pour demander le secondaire
        self.frame_secondaire = LabelFrame(self.frame, text="Secondaire")
        self.frame_secondaire.grid(row=2,column=0,stick=W,padx=5,pady=5,columnspan=2)

        self.configurator_secondaire_entry = Entry(self.frame_secondaire, style="NormalEntry.TEntry", font=("Garamond", 12),width=30)
        self.configurator_secondaire_entry.grid(row=0,column=0,padx=2)
        Placeholder().add_placeholder_to(self.configurator_secondaire_entry, self.secondaire)

        # Bouton pour enregistrer
        self.configurator_generator_button = Button(self.frame, text="Appliquer et Enregistrer", command= lambda: self.getEntries()).grid(row=3,column=0,pady=5)
        # Bouton pour ouvrir le menu additionnel ("...")
        self.configurator_other_button = Button(self.frame, text="...", width=2, command= lambda: self.createOTHER_GUI()).grid(row=3, column=1)
        
        self.configurator.mainloop()  # Laisser la fenêtre ouverte jusqu'à sa fermeture

    def createOTHER_GUI(self):
        """## Ouvre une nouvelle fenêtre avec le menu additionnel "..."
        """
        def getMatieres():
            """## Enregistre les matières selon les entrées, à utiliser avec un Callback
            """
            self.mat_final_dict = dict()
            for entry in self.entries:
                if entry[0].get() == "" or entry[1].get() == "":
                    continue
                self.mat_final_dict[entry[0].get()] = [entry[1].get(), entry[2].get()]

            self.other.destroy()
        
        def reloadMatieres():
            """## Met les valeurs par défaut en quittant et ouvrant à nouveau self.createOTHER_GUI()
            """
            self.other.destroy()
            self.createOTHER_GUI()

        self.other_number = 1  # (ré)Initialise le compteur du nb. de matières

        self.other = Toplevel(self.configurator)  # Ouvre une nouvelle fenêtre
        self.other.title("Configurateur de matières")
        self.other.resizable(False, False)

        self.other_button_frame = Frame(self.other)
        self.other_button_frame.grid(row=1, pady=5)

        self.other_reset = Button(self.other_button_frame, text="Paramètres par défaut", command= lambda: reloadMatieres())
        self.other_reset.grid(row=0,column=0, padx=10)

        self.other_add = Button(self.other_button_frame, text="Ajouter une matière", command= lambda: self.createNewWindow())
        self.other_add.grid(row=0,column=1, padx=10)

        self.other_set = Button(self.other_button_frame, text="Appliquer", command= lambda: getMatieres())
        self.other_set.grid(row=1,column=0,columnspan=2, pady=5)

        self.other_frame = LabelFrame(self.other, text="Matières")
        self.other_frame.grid(row=0, padx=5,pady=5)

        self.entries = list()  # Initialise les entrées, repères qui suivent combien d'entrées il existe

        for key, value in self.mat_dict.items():  # Crée les colonnes pour toutes les valeurs par défaut (self.mat_dict)
            self.createNewWindow(key, value)
            
    def createNewWindow(self, long="", court=""):
        """## Crée une nouvelle ligne
        ### Keyword Arguments:\n
            \tlong {str} -- Nom prédéfini à mettre dans la case Long (default: {""})
            \tcourt {str} -- Nom prédéfini à mettre dans la case Court (default: {""})
        """
        if self.other_number == 1: # Si c'est la première fois, crée les en-têtes
            Label(self.other_frame, text="#").grid(row=0,column=0)
            Label(self.other_frame, text="Long").grid(row=0,column=1)
            Label(self.other_frame, text="Court").grid(row=0,column=2)
            Label(self.other_frame, text="Dossier (vide si par défaut)").grid(row=0, column=3)

        Label(self.other_frame, text=str(self.other_number)).grid(row=self.other_number,column=0) # Crée le numéro de ligne
        # NOM DE LA MATIÈRE
        nom = Entry(self.other_frame, font="Garamond", justify=CENTER)
        nom.grid(row=self.other_number, column=1)
        nom.insert(0, long)
        # NUMÉRO DE LA MATIÈRE
        num = Entry(self.other_frame, font="Garamond", justify=CENTER)
        num.grid(row=self.other_number, column=2)
        num.insert(0, court)
        # CHEMIN DE LA MATIÈRE
        path = Entry(self.other_frame, font="Garamond", justify=CENTER)
        path.grid(row=self.other_number, column=3)

        self.entries.append((nom, num, path))  # Sauvegarder les entrées dans une liste
        self.other_number += 1  # Une entrée de plus existe, il faut incrémenter le compteur

    def getEntries(self):
        """## Action qui permet de stocker les informations dans les `Entry`
        """
        # Prend les infos
        self.auteur = self.configurator_auteur_entry.get().replace("&","")
        self.secondaire = self.configurator_secondaire_entry.get().replace("&","")
        # Supprime le configurateur
        self.configurator.destroy()

        self.json_data = dict()  # Crée le dictionnaire de données
        self.json_data["auteur"] = self.auteur  # Crée une entrée pour l'auteur
        self.json_data["secondaire"] = self.secondaire  # Crée une entrée pour le secondaire
        
        try:  # Regarde si des entrèes personnalisées pour les matières existent
            self.mat_final_dict
        except AttributeError:  # Si les entrées personnalisées n'existent pas
            self.mat_final_dict = dict()
            for key, value in self.mat_dict.items():  # Ajoute une entrée vide pour signifier qu'il faut utiliser la valeur par défaut
                self.mat_final_dict[key] = [value, ""]
        
        self.json_data["matiere"] = dict()  # Crée le dictionnaire de matières
        for key, value in self.mat_final_dict.items():
            self.json_data["matiere"][key] = value

        # Crée le fichier de configuration
        with open("pyEtude.json", "w", encoding="utf-8") as json_f:
            json.dump(self.json_data, json_f, sort_keys=True, indent=4)  # Formatte le fichier JSON selon les règles PRETTY-JSON
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
        __slots__ = 'normal_style', 'placeholder_text', 'with_placeholder'  # pylint: disable=unused-variable
    def add_placeholder_to(self, entry: tkinter.ttk.Entry, placeholder: str, placeholder_style="PlaceHolderEntry.TEntry"):
        """## Classe pour faire un placeholder
        Pour utiliser cette classe, vous devrez avoir deux styles:
        1) Le style par défaut, celui qui sera affiché lorsque l'utilisateur aura réellement mis du texte
        2) Un style qui servira de "placeholder", par défaut il s'appelle "PlaceHolderEntry.TEntry", si vous utilisez un autre nom, veuillez l'indiquer avec le kargs placeholder_style=
        ### Arguments:\n
            \tentry {tkinter.ttk.Entry} -- Entrée à ajouter le placeholder
            \tplaceholder {str} -- Le texte à mettre dans le placeholder
        ### Keyword Arguments:\n
            \tplaceholder_style {str} -- Le style de placeholder à utiliser (défault: {"PlaceHolderEntry.TEntry"})
        """
        normal_style = entry.cget("style")  # Enregistre le style initial de l'entrée
        state = Placeholder()  # Enregistre Placeholder pour qu'il puisse enregistrer les états
        state.normal_style = normal_style
        state.placeholder_text = placeholder
        state.with_placeholder=True
        def on_focusin(event, entry=entry, state=state):  # Callback lorsqu'on entre l'entrée
            if state.with_placeholder:  # Regarde si le placeholder est activé
                entry.delete(0, "end")  # Enlève le placeholder
                entry.config(style=state.normal_style)  # Met le style original
                state.with_placeholder = False  # Réinitialise state
        def on_focusout(event, entry=entry, state=state):  # Callback lorsqu'on sort de l'entrée
            if entry.get() == '':  # Regarde sile placeholder est vide
                entry.insert(0, state.placeholder_text)  # Insert le placeholder
                entry.config(style="PlaceHolderEntry.TEntry")  # Ajoute le style du placeholder
                state.with_placeholder = True  # Initialise le placeholder
        entry.insert(0, placeholder)  # Insert le placeholder dans l'entrée
        entry.config(style=placeholder_style)  # Ajoute le style du placeholder pour l'initialiser
        entry.bind('<FocusIn>', on_focusin, add="+")  # Crée une connexion entre on_focusin() et l'entrée
        entry.bind('<FocusOut>', on_focusout, add="+")  # Crée une connexion entre on_focusout() et l'entrée
        entry.placeholder_state = state  # Enregistre l'état
        return state  # Retourne l'état avec ses valeurs

class frontEnd:
    """## Main GUI du programme
    """
    def __init__(self, jsonData):
        """## Lance le programme principal
        
        ### Arguments:\n
            \tjsonData {dict} -- Un dictionnaire ayant les auteurs et le secondaire
        """
        # Extrait les infos dans jsonData
        self.auteur = jsonData["auteur"]  # Auteur
        self.secondaire = jsonData["secondaire"]  # Secondaire
        self.mat_dict = jsonData["matiere"]  # Matières + Clés + Chemins

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

        self.checkModels("model.docx")
        self.main()  # Lance le programme principal
        self.root.mainloop()  # Permet au programme de rester ouvert
    def checkModels(self, model_name:str):
        if os.path.isfile(model_name):
            return False
        else:
            urllib.request.urlretrieve(fr"https://raw.githubusercontent.com/BourgonLaurent/pyEtude/master/{model_name}", model_name)
            return True
        
    def main(self):
        """## Fonction "maison" qui regroupe les éléments de bases et renvoies aux autres composants du GUI
        """
        self.root = Tk()  # Crée une fenêtre
        self.root.title(TITLE + " - " + VERSION)  # Met un titre à cette fenêtre
        self.root.resizable(False, False)

        self.style = Style()
        if os.name == "nt":
            self.style.theme_use("vista")
        else:
            self.style.theme_use("clam")

        self.style.configure("BlueLink.TLabel", foreground="blue")
        self.style.configure("RaisedButton.TButton", relief="raised")
        self.style.configure("Generate.TButton", font=("", 15, "bold"))
        self.style.configure("OtherGen.TButton", font=("", 8, "italic"))
        self.style.configure("NormalEntry.TEntry", font=("Garamond", 12))
        self.style.configure("PlaceHolderEntry.TEntry", foreground="grey")
        
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
            self.refreshValues()  # Met à jour les valeurs sur le panneau
        
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


        # Met un Frame à la section Titre-SousTitre
        # self.frame_title = LabelFrame(self.input, text="")
        self.frame_title = Frame(self.input, borderwidth=2)
        self.frame_title.grid(row=0, column=0, padx=5)

        self.frame_titre = LabelFrame(self.frame_title, text="Titre")  # Crée un Frame avec un Label comme titre
        self.frame_titre.grid(row=0, column=0, padx=5, pady=3)  # Le place

        self.frame_titre_entry = Entry(self.frame_titre, style="NormalEntry.TEntry", font=("Garamond", 12), justify=CENTER, textvariable=self.frame_titre_entry_sv)  # Crée une entrée pour la section
        self.frame_titre_entry.grid(row=0,column=0,padx=5,pady=5)  # La place
        Placeholder().add_placeholder_to(self.frame_titre_entry, self.titre)  # Crée le callback avec le StringVar créer plus tôt

        self.frame_soustitre = LabelFrame(self.frame_title, text="Sous-Titre")
        self.frame_soustitre.grid(row=1, column=0, padx=5, pady=1)
        self.frame_soustitre_entry = Entry(self.frame_soustitre, style="NormalEntry.TEntry", font=("Garamond", 12), justify=CENTER, textvariable=self.frame_soustitre_entry_sv)
        self.frame_soustitre_entry.grid(row=0,column=0,padx=5,pady=5)
        Placeholder().add_placeholder_to(self.frame_soustitre_entry, self.soustitre)

        # Met un Frame à la section Matiere-Numero
        # self.frame_cours = LabelFrame(self.input, text="")
        self.frame_cours = Frame(self.input, borderwidth=2)
        self.frame_cours.grid(row=1,column=0, padx=5,pady=5)

        self.frame_matiere = LabelFrame(self.frame_cours, text="Matière")
        self.frame_matiere.grid(row=1, column=0, padx=5)
        self.frame_matiere_entry = Entry(self.frame_matiere, style="NormalEntry.TEntry", font=("Garamond", 12), justify=CENTER, textvariable=self.frame_matiere_entry_sv, width=10)
        self.frame_matiere_entry.grid(row=0,column=0,padx=5,pady=5)

        self.frame_matiere_entry.config(state='disabled')

        def setMatiereEntry():
            if cours.get() == "Personnaliser...":
                self.frame_matiere_entry.config(state='normal')
                return None
            self.frame_matiere_entry.config(state='normal')
            choice = re.sub(r"(?:.* - )", "", cours.get())
            self.frame_matiere_entry.delete(0, END)
            self.frame_matiere_entry.insert(0, choice)
            self.frame_matiere_entry.config(state='disabled')

            for values in self.mat_dict.values():
                if values[0] == choice:
                    if values[1] == "":
                        self.custom_directory = False
                        self.refreshValues()
                    else:
                        self.directory_name = values[1]
                        self.custom_directory = True
                        self.refreshValues()

            
        menu_matiere = Menubutton(self.frame_matiere, text="↩", style="RaisedButton.TButton", width=5)
        menu_matiere.grid(row=0,column=1, padx=5)

        menu_matiere.menu = Menu(menu_matiere, tearoff=0)
        menu_matiere["menu"] = menu_matiere.menu

        cours = StringVar()
        
        for key in sorted(self.mat_dict, key=locale.strxfrm):  # Crée les chemins selon les noms de matières triés selon le locale (avec accents)
            menu_matiere.menu.add_radiobutton(label=f"{key} - {self.mat_dict[key][0]}", variable=cours, command=setMatiereEntry)

        menu_matiere.menu.add_separator()
        menu_matiere.menu.add_radiobutton(label="Personnaliser...", variable=cours, command=setMatiereEntry)

        self.frame_numero = LabelFrame(self.frame_cours, text="Numéro")
        self.frame_numero.grid(row=2, column=0, padx=5, pady=1)
        self.frame_numero_entry = Entry(self.frame_numero, font="Garamond", justify=CENTER, textvariable=self.frame_numero_entry_sv, width=10)
        self.frame_numero_entry.grid(row=0,column=0,padx=5,pady=5)
        self.frame_numero_entry.config(state='disabled')

        menu_numero = Menubutton(self.frame_numero, text="↩", style="RaisedButton.TButton", width=5)
        menu_numero.grid(row=0,column=1, padx=5)

        menu_numero.menu = Menu(menu_numero, tearoff=0)
        menu_numero["menu"] = menu_numero.menu


        chapitreMenu = Menu(menu_numero.menu, tearoff=0)
        menu_numero.menu.add_cascade(label="Chapitre", menu=chapitreMenu)
        numero = StringVar()
        def setNumeroEntry():
            if numero.get() == "Personnaliser...":
                self.frame_numero_entry.config(state='normal')
                return None
            self.frame_numero_entry.config(state='normal')
            self.frame_numero_entry.delete(0, END)
            self.frame_numero_entry.insert(0, numero.get().replace(" - ", ""))
            self.frame_numero_entry.config(state='disabled')
        for index in range(0,20):
            chapitreMenu.add_radiobutton(label=f"CHP{index}", variable=numero, command=setNumeroEntry)

        dateMenu = Menu(menu_numero.menu, tearoff=0)
        menu_numero.menu.add_cascade(label="Date", menu=dateMenu)
        for pos, mois in enumerate(("Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"), start=1):
            if mois == "Février":
                number = 29+1
            elif mois in ("Avril", "Juin", "Septembre", "Novembre"):
                number = 30+1
            else:
                number = 31+1
            temp_menu = Menu(dateMenu, tearoff=0)
            dateMenu.add_cascade(label=mois, menu=temp_menu)

            for d in range(1,number):
                temp_menu.add_radiobutton(label= f"{str(pos).zfill(2)} - {str(d).zfill(2)}", variable=numero, command=setNumeroEntry)

            del temp_menu
        menu_numero.menu.add_separator()
        menu_numero.menu.add_radiobutton(label="Personnaliser...", variable=numero, command=setNumeroEntry)
        
        # Met un Frame à la section Première Section
        self.frame_section = LabelFrame(self.input, text="Première Section")
        self.frame_section.grid(row=3, column=0, padx=5, pady=3, ipadx=2)
        self.frame_section_label = Label(self.frame_section, text="1.", font=("Garamond", 12), justify=RIGHT).grid(row=0,column=0)
        self.frame_section_entry = Entry(self.frame_section, style="NormalEntry.TEntry", font=("Garamond", 12), justify=CENTER, textvariable=self.frame_section_entry_sv)
        self.frame_section_entry.grid(row=0,column=1,pady=5)
        Placeholder().add_placeholder_to(self.frame_section_entry, self.section)

    def showOptions(self):
        # Crée le label frame principal
        self.frame_options = LabelFrame(self.options, text="Options")
        self.frame_options.grid(row=0,column=0)
        # Crée le label frame pour l'option auteur
        self.frame_options_auteur = LabelFrame(self.frame_options, text="Auteur")
        self.frame_options_auteur.grid(row=0,column=0,padx=5)

        self.options_auteur_label = Label(self.frame_options_auteur, text=self.auteur, font=("Garamond", 13, "italic")).grid(row=0,column=0)
        # Crée le label frame pour l'option secondaire
        self.frame_options_secondaire = LabelFrame(self.frame_options, text="Secondaire")
        self.frame_options_secondaire.grid(row=1,column=0,padx=5, pady=2)
        self.options_secondaire_label = Label(self.frame_options_secondaire, text=self.secondaire, font=("Garamond", 13, "italic")).grid(row=0,column=0)

        # Crée le label frame qui contiendra toutes les valeurs créées par self.refreshValues()
        self.frame_values = LabelFrame(self.options, text="Valeurs")
        self.frame_values.grid(row=1,column=0,sticky=NW)

    def refreshValues(self):
        try:  # test s'il faut enlever les anciennes valeurs
            self.values_text.destroy()  # pylint: disable=access-member-before-definition
        except:  # ne fait rien
            pass
        # Regarde si l'utilisateur a spécifé un dossier
        if self.custom_directory == True:
            self.filepath = os.path.join(self.directory_name, f"{self.matiere}-{self.numero}.docx")
        elif self.custom_name == True: # Regarde si l'utilisateur a spécifé un dossier + fichier
            self.filepath = self.file_directory_name
        else:  # utilise les paramètres par défaut
            self.filepath = os.path.join(os.getcwd(), f"{self.matiere}-{self.numero}.docx")
        
        try:  # crée le message de valeurs
            self.values_text = Label(self.frame_values, wraplength=350, justify=LEFT, text=f"Titre: {self.titre}\nSous-Titre: {self.soustitre}\nMatière: {self.matiere}\nNuméro: {self.numero}\nSection: 1. {self.section}\n\nAuteur: {self.auteur}\nSecondaire: {self.secondaire}\n\n{self.filepath}")
            self.values_text.grid(row=0,column=0)
        except AttributeError:  # ne met pas l'alerte dans la console, mais le dit dans le debugger
            assert AttributeError
    
    def showGenerate(self):
        def browserButton():
            self.directory_name = tkinter.filedialog.askdirectory()
            if not self.directory_name:
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
        self.generate_button = Button(self.frame_generate, text="Générer",style="Generate.TButton", command=lambda: generateButton())
        self.generate_button.grid(row=0,column=0,padx=10,pady=9)
        self.file_button = Button(self.frame_generate, text="Enregistrer sous...", style="OtherGen.TButton", command= lambda: fileButton())
        self.file_button.grid(row=1,column=0,padx=10,pady=2)
        self.browser_button = Button(self.frame_generate, text="Choisir le dossier de sortie", style="OtherGen.TButton", command=lambda: browserButton()).grid(row=2,column=0,padx=10,pady=3)

    def showSettings(self):
        def modifyOptions(self):
            os.remove("pyEtude.json")
            os.execl(sys.executable, 'python', __file__, *sys.argv[1:])
        
        self.frame_settings = LabelFrame(self.settings, text="Réglages")
        self.frame_settings.grid(row=0,column=0)

        self.settings_options_button = Button(self.frame_settings, width=19, text="Modifier les Options", command=lambda: modifyOptions(self)).grid(row=0,column=0,padx=5,pady=3)

        self.settings_model_button = Button(self.frame_settings, width=19, text="Modifier le Modèle", command=lambda: self.showModelWindow()).grid(row=1,column=0,padx=5,pady=3)
        
        self.about_github = Label(self.frame_settings, text="Projet GitHub", style="BlueLink.TLabel", cursor="hand2",justify=CENTER)
        self.about_github.grid(row=2,column=0)
        self.about_github.bind("<Button-1>", lambda e: webbrowser.open_new(r"https://github.com/BourgonLaurent/pyEtude"))
        
        self.about_license = Label(self.frame_settings, text="Sous la license MIT\n© Laurent Bourgon 2019", style="BlueLink.TLabel", cursor="hand2", font=("",8,"italic"))
        self.about_license.grid(row=3,column=0,sticky=S)
        self.about_license.bind("<Button-1>", lambda e: webbrowser.open_new(r"https://github.com/BourgonLaurent/pyEtude/blob/master/LICENSE"))
    
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

        # self.modifyOptions(os.path.join(self.folder, "docProps", "core.xml"), self.options)
        self.modifyOptions(os.path.join(self.folder, "word", "document.xml"), self.options)
        self.modifyOptions(os.path.join(self.folder, "word", "header1.xml"), self.options)
        self.modifyOptions(os.path.join(self.folder, "word", "footer1.xml"), self.options)

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
        locale.setlocale(locale.LC_ALL, (None, None))  # Fix compatibility with locale
        with zipfile.ZipFile(final, "w") as zip_file:
            for root, dirs, files in os.walk(folder):  # pylint: disable=unused-variable
                # zip_file.write(os.path.join(root, "."))

                for File in files:
                    filePath = os.path.join(root, File)
                    inZipPath = filePath.replace(folder, "", 1).lstrip("\\/")
                    zip_file.write(filePath, inZipPath)
        print(f"\nLe document a été créé: {self.filepath}")  # Si démarré à partir de l'invite de commande

        Tk().withdraw()  # Si démarré sous .pyw
        tkinter.messagebox.showinfo(TITLE+VERSION, f"Le document a été créé: {self.filepath}")
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