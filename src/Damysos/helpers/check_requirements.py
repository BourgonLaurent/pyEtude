import sys

try:
    import os, json, locale, typing

    from PySide2 import QtCore, QtGui
    from PySide2.QtWidgets import *

    from docxtpl import DocxTemplate
except ImportError as e:
    # Affiche le message d'erreur
    print(
        "[!] Impossible de continuer:\n\n"
        + f"\t{repr(e)}"
        + "\n\n"
        + f"[*] Avez-vous installé {e.name}?\n"
        + "C'est un module nécessaire au fonctionnement de Damysos.\n\n"
        + "Essayez la commande suivante:"
        + f"\tpip install --update {e.name}\n\n"
        + "Vous pouvez aussi vous référer au README.md de la page GitHub."
    )
    # Quitte le programme en indiquant l'erreur
    sys.exit(e)
