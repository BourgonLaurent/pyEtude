## downloader.py - pyEtude
# Download manager for files on GitHub
#
# MIT (c) 2020 Laurent Bourgon
#    Permission is hereby granted, free of charge, to any person obtaining a copy
#    of this software and associated documentation files (the "Software"), to deal
#    in the Software without restriction, including without limitation the rights
#    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#    copies of the Software, and to permit persons to whom the Software is
#    furnished to do so, subject to the following conditions:
#
#    The above copyright notice and this permission notice shall be included in all
#    copies or substantial portions of the Software.
#
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#    SOFTWARE.

## Imports
# Project packages
from .. import __version__, GITHUB_REPO

# Default packages
from urllib.request import urlretrieve, urlopen
from urllib.parse import quote
from urllib.error import HTTPError


class FileDownloader:
    """## Télécharge un fichier du répertoire GitHub raw
    
    ### Arguments:\n
        \tname {str} -- Nom du fichier à prendre
    
    ### Returns:\n
        \t[str] -- (si create=False): données décodées qui ont été prises
    """

    def __init__(self, name: str):
        self.name = name

    def saveFile(self):
        try:
            urlretrieve(
                quote(
                    fr"https://raw.githubusercontent.com/{GITHUB_REPO}/{__version__}/src/{self.name}",
                    safe="/:?=&",
                ),
                self.name,
            )

        except HTTPError:
            urlretrieve(
                quote(
                    fr"https://raw.githubusercontent.com/{GITHUB_REPO}/master/src/{self.name}",
                    safe="/:?=&",
                ),
                self.name,
            )

    def returnContent(self) -> str:
        try:
            with urlopen(
                quote(
                    fr"https://raw.githubusercontent.com/{GITHUB_REPO}/{__version__}/src/{self.name}",
                    safe="/:?=&",
                )
            ) as ur:
                return ur.read().decode()

        except HTTPError:
            with urlopen(
                quote(
                    fr"https://raw.githubusercontent.com/{GITHUB_REPO}/master/src/{self.name}",
                    safe="/:?=&",
                )
            ) as ur:
                return ur.read().decode()


def downloadFile(name: str):
    """## Télécharge un fichier du répertoire GitHub raw
    
    ### Arguments:\n
        \tname {str} -- Nom du fichier à prendre
    
    ### Returns:\n
        \t[str] -- (si create=False): données décodées qui ont été prises
    """
    try:
        urlretrieve(
            quote(
                fr"https://raw.githubusercontent.com/{GITHUB_REPO}/{__version__}/src/{name}",
                safe="/:?=&",
            ),
            name,
        )

    except HTTPError:
        urlretrieve(
            quote(
                fr"https://raw.githubusercontent.com/{GITHUB_REPO}/master/src/{name}",
                safe="/:?=&",
            ),
            name,
        )


def downloadFileContent(name: str) -> str:
    """## Retourne un fichier du répertoire GitHub raw
    
    ### Arguments:\n
        \tname {str} -- Nom du fichier à prendre
    
    ### Returns:\n
        \t[str] -- (si create=False): données décodées qui ont été prises
    """
    try:
        with urlopen(
            quote(
                fr"https://raw.githubusercontent.com/{GITHUB_REPO}/{__version__}/src/{name}",
                safe="/:?=&",
            )
        ) as ur:
            return ur.read().decode()

    except HTTPError:
        with urlopen(
            quote(
                fr"https://raw.githubusercontent.com/{GITHUB_REPO}/master/src/{name}",
                safe="/:?=&",
            )
        ) as ur:
            return ur.read().decode()
