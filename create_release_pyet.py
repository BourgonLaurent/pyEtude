# -*- coding: utf-8 -*-
"""
                 ███████╗████████╗██╗   ██╗██████╗ ███████╗
                 ██╔════╝╚══██╔══╝██║   ██║██╔══██╗██╔════╝
██████╗ ██╗   ██╗█████╗     ██║   ██║   ██║██║  ██║█████╗  
██╔══██╗╚██╗ ██╔╝██╔══╝     ██║   ██║   ██║██║  ██║██╔══╝  
██████╔╝ ╚████╔╝ ███████╗   ██║   ╚██████╔╝██████╔╝███████╗
██╔═══╝   ╚██╔╝  ╚══════╝   ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝
██║        ██║   MIT © Laurent Bourgon 2019
╚═╝        ╚═╝   RELEASE PREP, DEV ONLY
"""
import os, sys, shutil, webbrowser
from PyQt5 import uic

os.chdir(os.path.realpath(__file__).replace(os.path.basename(__file__), ""))  # Accède aux fichiers depuis la racine du programme, et non l'endroit du shell

# Test DEFAULT variables
import pyETUDE as pyet
if '~' in pyet.VERSION:
    sys.exit("[!] ERREUR 0-1: Êtes-vous sûr que c'est la version finale? ~ a été trouvé")
if pyet.DEBUG:
    sys.exit("[!] ERREUR 0-2: pyÉtude est encore en mode DEBUG: DEBUG=True")

# Convertit le fichier pyEtude.ui => pyet_ui.py
with open("pyet_ui.py", "w", encoding="utf-8") as ui_file:
    uic.compileUi("pyEtude.ui", ui_file)

# Met le fichier pyETUDE.pyw dans le dossier release
shutil.copy('pyETUDE.pyw', f'releases/pyEtude-v{pyet.VERSION}.pyw')

# Demande s'il faut publier la release
choice = input("[*] Souhaitez-vous publiez cette version sur GitHub? (Oui/Non, Défault: Non)")
if choice.lower() in ("oui","o","yes","y"):
    os.system("git add pyEtude.ui pyet_ui.py pyETUDE.pyw")
    os.system(f"git commit -m 'AUTOMATIC RELEASE PREP: v{pyet.VERSION}'")
    os.system("git push")
    os.system(f"git tag v{pyet.VERSION}")
    os.system(f"git push origin v{pyet.VERSION}")
    os.system("git pull")
    print("\n\n[x] Pour terminer, veuillez confirmer la release sur le site de GitHub.")
    print(f"\nN'oubliez pas de mettre le fichier releases/pyEtude-v{pyet.VERSION}.pyw dans les téléchargements!")
    webbrowser.open("https://github.com/BourgonLaurent/pyEtude/releases")
else:
    pass