## downloader.py - damysos.helpers
# Download manager for files on GitHub
#
# MIT (c) 2021 Laurent Bourgon
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
from urllib.error import HTTPError, URLError


class FileDownloader:
    """
    A file existing on GitHub (GITHUB_REPO)

    Parameters
    ----------
    name : str
        Name of the file

    Methods
    ----------
    saveFile : () -> ()
        Downloads a file and saves it

    returnContent: () -> str
        Returns the content of the online file
    """

    def __init__(self, name: str):
        self.name = name

    def saveFile(self):
        """Downloads a file and saves it"""
        try:
            urlretrieve(
                quote(
                    fr"https://raw.githubusercontent.com/{GITHUB_REPO}/{__version__}/src/{self.name}",
                    safe="/:?=&",
                ),
                self.name,
            )

        except (HTTPError, URLError):
            urlretrieve(
                quote(
                    fr"https://raw.githubusercontent.com/{GITHUB_REPO}/master/src/{self.name}",
                    safe="/:?=&",
                ),
                self.name,
            )

    def returnContent(self) -> str:
        """
        Returns the content of the online file

        Returns
        -------
        str
            Content of the file
        """

        try:
            with urlopen(
                quote(
                    fr"https://raw.githubusercontent.com/{GITHUB_REPO}/{__version__}/src/{self.name}",
                    safe="/:?=&",
                )
            ) as ur:
                return ur.read().decode()

        except (HTTPError, URLError):
            with urlopen(
                quote(
                    fr"https://raw.githubusercontent.com/{GITHUB_REPO}/master/src/{self.name}",
                    safe="/:?=&",
                )
            ) as ur:
                return ur.read().decode()
