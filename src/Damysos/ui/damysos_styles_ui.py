## damysos_styles_ui.py - Damysos.ui
# Stylesheets that are used for multiple components

# Imports
## Default packages
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
