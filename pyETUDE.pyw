# -*- coding: utf-8 -*-/
intro = """
                 ███████╗████████╗██╗   ██╗██████╗ ███████╗
                 ██╔════╝╚══██╔══╝██║   ██║██╔══██╗██╔════╝
██████╗ ██╗   ██╗█████╗     ██║   ██║   ██║██║  ██║█████╗  
██╔══██╗╚██╗ ██╔╝██╔══╝     ██║   ██║   ██║██║  ██║██╔══╝  
██████╔╝ ╚████╔╝ ███████╗   ██║   ╚██████╔╝██████╔╝███████╗
██╔═══╝   ╚██╔╝  ╚══════╝   ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝
██║        ██║   MIT © Laurent Bourgon 2019
╚═╝        ╚═╝   v2.0.0~b1
"""

import os, sys, zipfile, json, tkinter.filedialog, webbrowser
from tkinter import *


TITLE = r"pyÉtude"
VERSION = r"v2.0.0~b1"

WIDTH = 500
HEIGHT = 490

class Configurator:
    def __init__(self):
        self.checkRun()
    
    def checkRun(self):
        if os.path.isfile("pyEtude.json"):
            json_data = self.readJSON()
        else:
            self.createJSON_GUI()
    
    def createJSON_GUI(self):
        self.configurator = Tk()
        self.configurator.title(TITLE + " - " + VERSION )
        self.configurator.geometry(f"285x172")

        self.frame = LabelFrame(self.configurator, text="Configurateur",width=250)
        self.frame.grid(row=0,column=0,padx=5)

        self.frame_title = Label(self.frame, text="Veuillez répondre aux questions suivantes",justify=CENTER).grid(row=0,column=0)

        self.frame_auteur = LabelFrame(self.frame, text="Auteur")
        self.frame_auteur.grid(row=1,column=0,stick=W,padx=5)
        self.configurator_auteur_entry = Entry(self.frame_auteur,font="Garamond 12",width=30)
        self.configurator_auteur_entry.grid(row=0,column=0,padx=2)

        self.frame_secondaire = LabelFrame(self.frame, text="Secondaire")
        self.frame_secondaire.grid(row=2,column=0,stick=W,padx=5,pady=5)
        self.configurator_secondaire_entry = Entry(self.frame_secondaire,font="Garamond 12",width=30)
        self.configurator_secondaire_entry.grid(row=0,column=0,padx=2)

        self.configurator_generator_button = Button(self.frame, text="Appliquer et Enregistrer", command= lambda: self.getEntries()).grid(row=3,column=0,pady=5)
        self.configurator.mainloop()

    def getEntries(self):
        self.auteur = self.configurator_auteur_entry.get()
        self.secondaire = self.configurator_secondaire_entry.get()
        self.configurator.destroy()
        self.json_data = dict()
        self.json_data["auteur"] = self.auteur
        self.json_data["secondaire"] = self.secondaire
        with open("pyEtude.json", "w") as json_f:
            json.dump(self.json_data, json_f)

        frontEnd(self.json_data)

    def readJSON(self):
        with open("pyEtude.json") as json_f:
            self.json_data = json.load(json_f)
        frontEnd(self.json_data)

class frontEnd:
    def __init__(self, json_data):
        self.auteur = json_data["auteur"]
        self.secondaire = json_data["secondaire"]
        
        self.custom_directory = False
        self.custom_name = False
        
        self.titre = "Ceci est un example"
        self.soustitre = "Newton, un homme incroyable"
        self.matiere = "PHY"
        self.numero = "0716"
        self.section = "La Loi de l'Inertie"

        self.main()
        self.root.mainloop()

    def main(self):
        self.root = Tk()
        self.root.title(TITLE + " - " + VERSION)
        self.root.geometry(f"{WIDTH}x{HEIGHT}")

        # self.top_frame = Frame(self.root)
        # self.top_frame.grid(row=0, column=0)

        self.frame = Frame(self.root)
        self.frame.grid(row=1, column=0)

        self.input = LabelFrame(self.frame, text="Information")
        self.input.grid(row=0, column=0, sticky=NW, padx=10)

        self.options = Frame(self.frame)
        self.options.grid(row=1, column=0, sticky=SW, padx=10)

        self.generate = Frame(self.frame)
        self.generate.grid(row=0, column=1, sticky=N)

        self.settings = Frame(self.frame)
        self.settings.grid(row=1, column=1, sticky=SE)

        self.showInput()
        self.showOptions()
        self.showGenerate()
        self.showSettings()

    def showInput(self):
        self.frame_title = LabelFrame(self.input, text="")
        self.frame_title.grid(row=0, column=0, padx=5, pady=5)

        self.frame_titre = LabelFrame(self.frame_title, text="Titre")
        self.frame_titre.grid(row=0, column=0, padx=5, pady=3)
        self.frame_titre_entry = Entry(self.frame_titre, font="Garamond 12", justify=CENTER)
        self.frame_titre_entry.grid(row=0,column=0,padx=5,pady=5)

        self.frame_soustitre = LabelFrame(self.frame_title, text="Sous-Titre")
        self.frame_soustitre.grid(row=1, column=0, padx=5, pady=1.5)
        self.frame_soustitre_entry = Entry(self.frame_soustitre, font="Garamond 12", justify=CENTER)
        self.frame_soustitre_entry.grid(row=0,column=0,padx=5,pady=5)

        self.frame_cours = LabelFrame(self.input, text="")
        self.frame_cours.grid(row=1,column=0, padx=5,pady=5)

        self.frame_matiere = LabelFrame(self.frame_cours, text="Matière")
        self.frame_matiere.grid(row=1, column=0, padx=5, pady=3)
        self.frame_matiere_entry = Entry(self.frame_matiere, font="Garamond 12", justify=CENTER)
        self.frame_matiere_entry.grid(row=0,column=0,padx=5,pady=5)

        self.frame_numero = LabelFrame(self.frame_cours, text="Numéro")
        self.frame_numero.grid(row=2, column=0, padx=5, pady=1.5)
        self.frame_numero_entry = Entry(self.frame_numero, font="Garamond 12", justify=CENTER)
        self.frame_numero_entry.grid(row=0,column=0,padx=5,pady=5)

        self.frame_section = LabelFrame(self.input, text="Première Section")
        self.frame_section.grid(row=3, column=0, padx=5, pady=3)
        self.frame_section_entry = Entry(self.frame_section, font="Garamond 12", justify=CENTER)
        self.frame_section_entry.grid(row=0,column=0,padx=5,pady=5)

        def validateButton():
            self.titre = self.frame_titre_entry.get()
            self.soustitre = self.frame_soustitre_entry.get()
            self.matiere = self.frame_matiere_entry.get()
            self.numero = self.frame_numero_entry.get()
            self.section = self.frame_section_entry.get()
            self.refreshValues()
        self.input_button = Button(self.input, text="Valider", font=("", 10, "bold"), command=lambda:validateButton()).grid(row=4, column=0,padx=5,pady=8)

    def showOptions(self):
        self.frame_options = LabelFrame(self.options, text="Options")
        self.frame_options.grid(row=0,column=0)

        self.frame_options_auteur = LabelFrame(self.frame_options, text="Auteur")
        self.frame_options_auteur.grid(row=0,column=0,padx=5)
        self.options_auteur_label = Label(self.frame_options_auteur, text=self.auteur, font="Garamond 13 italic").grid(row=0,column=0)

        self.frame_options_secondaire = LabelFrame(self.frame_options, text="Secondaire")
        self.frame_options_secondaire.grid(row=1,column=0,padx=5, pady=2)
        self.options_secondaire_label = Label(self.frame_options_secondaire, text=self.secondaire, font="Garamond 13 italic").grid(row=0,column=0)

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
        self.values_text = Message(self.frame_values, width=250, text=f"Titre: {self.titre}\nSous-Titre: {self.soustitre}\nMatière: {self.matiere}\nNuméro: {self.numero}\nSection: {self.section}\n\nAuteur: {self.auteur}\nSecondaire: {self.secondaire}\n\n{self.filepath}")
        self.values_text.grid(row=0,column=0)
    def showGenerate(self):
        def browserButton():
            self.directory_name = tkinter.filedialog.askdirectory()
            self.custom_directory = True
            self.refreshValues()
        def fileButton():
            self.file_directory_name = tkinter.filedialog.asksaveasfilename(filetypes = (("Document Word","*.docx"),))
            self.custom_name = True
            self.refreshValues()
        def generateButton():
            pass
        
        self.frame_values = LabelFrame(self.generate, text="Valeurs")
        self.frame_values.grid(row=0,column=0,padx=5,sticky=NW)

        self.refreshValues()

        self.frame_generate = LabelFrame(self.generate, text="Générer")
        self.frame_generate.grid(row=1,column=0,padx=5)
        self.generate_button = Button(self.frame_generate, text="Générer", font=("", 15, "bold"), command=lambda: generateButton()).grid(row=0,column=0,padx=10,pady=10)
        self.file_button = Button(self.frame_generate, text="Enregistrer sous...", font=("",8,"italic"), command= lambda: fileButton()).grid(row=1,column=0,padx=10,pady=2)
        self.browser_button = Button(self.frame_generate, text="Choisir le dossier de sortie", font=("",8,"italic"), command=lambda: browserButton()).grid(row=2,column=0,padx=10,pady=3)

    def showSettings(self):
        def modifyOptions(self):
            os.remove("pyEtude.json")
            os.execl(sys.executable, 'python', __file__, *sys.argv[1:])
        
        self.frame_settings = LabelFrame(self.settings, text="Réglages")
        self.frame_settings.grid(row=0,column=0,padx=5)

        self.settings_options_button = Button(self.frame_settings, width=19, text="Modifier les Options", command=lambda: modifyOptions(self)).grid(row=0,column=0,padx=5,pady=3)

        self.settings_model_button = Button(self.frame_settings, width=19, text="Modifier le Modèle Word").grid(row=1,column=0,padx=5,pady=3)

        self.settings_a_propos = Button(self.frame_settings, width=19, text="À Propos", command=lambda: self.aboutProgram()).grid(row=2,column=0,padx=5,pady=3)
    
    def aboutProgram(self):
        self.about = Toplevel()
        self.about.title = f"pyÉtude - À propos"

        self.about_frame = Frame(self.about)
        self.about_frame.grid()

        self.about_github = Label(self.about_frame, text="Github here", fg="blue", cursor="hand")
        self.about_github.grid()
        self.about_github.bind("<Button-1>", lambda e: webbrowser.open_new(r"https://github.com/BourgonLaurent/pyEtude"))

        self.about.mainloop()

class Document:
    def __init__(self):
        pass

if __name__ == "__main__":
    Configurator()