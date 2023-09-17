import lib
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import qdarkstyle
import threading

class SettingsWindow(QDialog):
    def __init__(self):
        super().__init__()
        darkStylesheet = qdarkstyle.load_stylesheet_pyqt5()
        self.setStyleSheet(darkStylesheet)
        self.setWindowTitle("Settings")
        self.setGeometry(100,  100,  400,  100)

        # Create a tabbed view
        self.tabWidget = QTabWidget()
        self.tabWidget.addTab(APITab(), "API")
        #self.tabWidget.addTab(ThemeTab(), "Theme")

        # Add the tabbed view to the window
        layout = QVBoxLayout()
        layout.addWidget(self.tabWidget)
        self.setLayout(layout)

class APITab(QWidget):
    def __init__(self):
        super().__init__()
        # Create a QLineEdit for the API key
        self.apiKeyLabel = QLabel("API Key:")
        self.apiKeyEdit = QLineEdit(lib.readConfigFile("apiKey"))
        self.apiKeyMessage = QLabel("Restart app after changing!")
        print(self.apiKeyEdit.text())
        self.apiKeyEdit.textChanged.connect(lambda:lib.writeConfigFile("apiKey",self.apiKeyEdit.text()))

        # Add the QLineEdit to the layout
        layout = QVBoxLayout()
        layout.addWidget(self.apiKeyLabel)
        layout.addWidget(self.apiKeyEdit)
        layout.addWidget(self.apiKeyMessage)
        self.setLayout(layout)

class ThemeTab(QWidget):
    def __init__(self):
        super().__init__()