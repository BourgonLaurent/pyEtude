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
import os, sys, shutil
from PyQt5 import uic

os.chdir(os.path.realpath(__file__).replace(os.path.basename(__file__), ""))  # Accède aux fichiers depuis la racine du programme, et non l'endroit du shell

# Test DEFAULT variables
import pyETUDE as pyet
if '~' in pyet.VERSION:
    sys.exit("[x] ERREUR 0-1: Êtes-vous sûr que c'est la version finale? ~ a été trouvé")
if pyet.DEBUG:
    sys.exit("[x] ERREUR 0-2: pyÉtude est encore en mode DEBUG: DEBUG=True")

# Convertit le fichier pyEtude.ui => pyet_ui.py
with open("pyet_ui.py", "w", encoding="utf-8") as ui_file:
    uic.compileUi("pyEtude.ui", ui_file)

# Met le fichier pyETUDE.pyw dans le dossier release

shutil.copy('pyETUDE.pyw', f'releases/pyEtude-v{pyet.VERSION}.pyw')