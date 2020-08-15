## styles_ui.py - damysos.ui
# Stylesheets that are used for multiple components
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
# Default packages
from typing import Dict

STYLES: Dict[str, str] = {
    "message_box": """QWidget {
                      background-color: #262626;
                      border: 0px solid #32414B;
                      padding: 0px;
                      color: #FFFFFF;
                      selection-background-color: #1464A0;
                      selection-color: #FFFFFF;
                    }
                    QPushButton {
                      background-color: #484644;
                      border: 1px solid #605e5c;
                      color: #FFFFFF;
                      border-radius: 4px;
                      padding-left: 30px;
                      padding-right: 30px;
                      padding-top: 5px;
                      padding-bottom: 5px;
                      outline: none;
                    }
                    QPushButton:pressed, QPushButton:pressed:hover { background-color: #323130; }
                    QPushButton:hover { background-color: #605e5c; }
                    """,
    "line_edit": "QLineEdit{ border-top-right-radius: 0px; border-bottom-right-radius: 0px; }",
}
