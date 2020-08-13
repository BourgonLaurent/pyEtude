import sys

try:
    import os, json, locale, typing

    from PySide2 import QtCore, QtGui
    from PySide2.QtWidgets import *

    from docxtpl import DocxTemplate
except ImportError as e:
    # Crée le message d'erreur
    error_message = (
        "[!] Impossible de continuer:\n\n"
        + f"\t{repr(e)}"
        + "\n\n"
        + f"[*] Avez-vous installé {e.name}?\n"
        + "C'est un module nécessaire au fonctionnement de pyÉtude.\n\n"
        + "Essayez la commande suivante:"
        + f"\tpip install --update {e.name}\n\n"
        + "Vous pouvez aussi vous référer au README.md de la page GitHub."
    )
    # Essaie de montrer un message d'erreur à l'aide d'un GUI par défaut
    try:
        from tkinter import Tk
        from tkinter.messagebox import showerror

        Tk().withdraw()
        showerror("pyÉtude - Configuration requise non respectée", error_message)
    except ImportError:  # Le module de GUI n'existe pas
        print(error_message)
    # Quitte le programme en indiquant l'erreur
    sys.exit(e)
