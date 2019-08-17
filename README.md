# pyÉtude

                     ███████╗████████╗██╗   ██╗██████╗ ███████╗
                     ██╔════╝╚══██╔══╝██║   ██║██╔══██╗██╔════╝
    ██████╗ ██╗   ██╗█████╗     ██║   ██║   ██║██║  ██║█████╗  
    ██╔══██╗╚██╗ ██╔╝██╔══╝     ██║   ██║   ██║██║  ██║██╔══╝  
    ██████╔╝ ╚████╔╝ ███████╗   ██║   ╚██████╔╝██████╔╝███████╗
    ██╔═══╝   ╚██╔╝  ╚══════╝   ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝
    ██║        ██║   MIT © Laurent Bourgon 2019
    ╚═╝        ╚═╝   v0.1.0~b1
---
<div align="center">

  [![Releases](https://img.shields.io/github/release/BourgonLaurent/pyEtude)](https://github.com/BourgonLaurent/pyEtude/releases) [![Languages](https://img.shields.io/github/languages/top/BourgonLaurent/pyEtude)](https://www.python.org/) [![License](https://img.shields.io/github/license/BourgonLaurent/pyEtude)](LICENSE)

   [![GitHub Issues](https://img.shields.io/github/issues-raw/BourgonLaurent/pyEtude)](https://img.shields.io/github/issues/BourgonLaurent/pyEtude/issues) [![GitHub Pull Requests](https://img.shields.io/github/issues-pr-raw/BourgonLaurent/pyEtude)](https://github.com/BourgonLaurent/pyEtude/pulls)

Programme `Python3` qui permet de créer un document `Microsoft Word` pré-configuré afin de réaliser un Document de Révision.
</div>

---

## 📝 Table des Matières

- [Problème encontré](#probleme)
- [Solution](#solution)
- [Ce qu'il faut et les limites du projet](#limites)
- [Avenir](#avenir)
- [Bien Démarrer](#démarrer)
  - [Configuration requise](#configuration)
  - [Installation](#installation)
- [Utilisation](#utilisation)
- [Créé avec](#créé)
- [Contributeurs](#contrib)
<!--- [Reconnaissances](#recon) -->
- [Licence](#licence)

## 🧐 Problème encontré <a name = "probleme"></a>

La création d'un document de révision est un outil majeur à l'apprentissage de nouveaux concepts, que ce soit au profil académique ou pour un loisir. Dans un monde idéal, nous n'aurions qu'à taper les informations et cela nous aiderait à les mémoriser. Cependant, les outils de traitement de texte ne permettent pas une telle facilité. Afin d'avoir un document potable pour l'étudier, il faut un modèle précis qui permet l'organisation de sujets peu importe leur champ. La création d'un tel document prend beaucoup de temps et, malheureusement, `Microsoft Word` ne permet aucun moyen efficace pour réutiliser ce modèle (les fichiers modèles `.dotx` ont beaucoup de problèmes). Ce problème réduit le temps qui peut être utilisé au remplissage du document.

Pour régler ce problème, j'ai commencé un projet qui permet de remplir un document modèle en quelques secondes et ce, sans problème de formattage.

## 💡 Solution <a name = "solution"></a>

Afin de remplir ce document facilement, le programme va faire ceci:

1. Extraire le fichier modèle dans un dossier temporaire
2. Remplacer les informations par ce qui a été demandé au niveau du GUI
    - Le programme remplacera des valeurs dans les fichiers `.xml` du document `Word`.
3. Zipper le dossier temporaire
4. Renommer l'extension du fichier créé pour qu'il soit reconnu par `Microsoft Word`

## ⛓️ Ce qu'il faut et les limites du projet <a name = "limites"></a>

- Ce problème nécessite (pour l'instant) [`Python3`](https://www.python.org/downloads/). Il devrait être installé par défaut sur les ordinateurs sous `macOS` ou `Linux`. Pour `iOS`, `Android`, `Windows`, `Nintendo Switch Horizon OS`, ou tout autre système d'exploitation, il faudra l'installer manuellement.
- Ce projet utilise un document `Word` manuellement configuré et le modifie à l'intérieur. Pour avoir un modèle différent, il faut modifier ce document avec les bonnes balises.
- Ce projet n'utilise pas le module `python-docx` puisqu'il était trop compliqué d'avoir un résultat correct et sans problème. De plus, cela enlève un élément à télécharger.

## 🚀 Avenir <a name = "avenir"></a>

- [ ] Avoir plusieurs modèles qui peuvent être choisis.
- [ ] Avoir plusieurs types de documents (page de présentation, devoirs, etc)
- [ ] Transformer ce programme en interface web pour faciliter la tâche
- [ ] Transformer ce programme en application pour faciliter l'utilisation sur tablettes

## 🏁 Bien Démarrer <a name = "démarrer"></a>


### Configuration requise <a name = "configuration"></a>

| Catégorie          | Valeur           | Notes additionnelles                                                                            | Installation                                               |
|--------------------|------------------|-------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| OS:                | N'importe lequel |                                                                                                 |                                                            |
| Python:            | `Python 3`       | Développé sous Python 3.7.4, veuillez mettre à jour votre version si vous avez des problèmes    | [Télécharger `Python3`](https://www.python.org/downloads/) |
| Extensions Python: | `os`             | Fait parti des paquets par défaut, pas besoin de l'installer ||
|                    | `zipfile`        | Fait parti des paquets par défaut, pas besoin de l'installer ||

### Installation <a name = "installation"></a>

1. Assurez-vous que vous respectez la [Configuration requise](#configuration).
2. Télécharger la version la plus récente de `pyEtude-vX.X.X.zip` dans les [releases](https://github.com/BourgonLaurent/pyEtude/releases).
3. Décompresser le fichier `pyEtude-vX.X.X.zip` dans un dossier vide.
4. Exécuter le programme avec le terminal/invite de commande ou selon votre système d'exploitation.

```bash
$ cd Users/Laurent/Documents/GitHub/pyEtude
$ python pyEtude.py
```

## 🎈 Utilisation <a name = "utilisation"></a>

Exécuter le programme avec le terminal/invite de commande ou selon votre système d'exploitation.

```bash
$ cd Users/Laurent/Documents/GitHub/pyEtude
$ python pyEtude.py
```

[À FAIRE]

## ⛏️ Créé avec <a name = "créé"></a>

- [Visual Studio Code](https://code.visualstudio.com/) pour écrire, modifier et effectuer le déboggage du programme
- [λ cmder Console Emulator](https://cmder.net/) pour le développement et pour l'invite de commande
- [Microsoft Word 365](https://products.office.com/fr-ca/word) pour créer le modèle utilisé
- [GitHub](https://github.com/) pour organiser, publier et sauvegarder ce projet

## ✍️ Contributeurs <a name = "contrib"></a>

- [@BourgonLaurent](https://github.com/BourgonLaurent) - Idée & Programme en entier

<!--- ## 🎉 Reconnaissances <a name = "recon"></a> -->

## 🔏 Licence <a name = "licence"></a>

Ce projet est sous [licence MIT](https://opensource.org/licenses/MIT).

Cet extrait provient de [LICENSE](LICENSE):
> MIT License
>
> Copyright © 2019 Laurent Bourgon
>
> Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
>
> THE SOFTWARE IS PROVIDED "AS IS", _**WITHOUT WARRANTY OF ANY KIND**_, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.