from pyEtude.pyETUDE import frontEnd

import os

# Accède aux fichiers depuis la racine du programme, et non l'endroit du shell
os.chdir(os.path.realpath(__file__).replace(os.path.basename(__file__), ""))

if __name__ == "__main__":
    fe = frontEnd()
    fe.executeGUI()
