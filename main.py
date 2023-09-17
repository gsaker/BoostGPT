from chat import ChatWindow
from settings import SettingsWindow
from PyQt5 import QtWidgets
import sys 
import lib
def launchSettings():
    settingsWindow = SettingsWindow()
    settingsWindow.show()
    
if __name__ == '__main__':
    lib.initialSetup()
    app = QtWidgets.QApplication(sys.argv)
    chatWindow = ChatWindow()
    chatWindow.show()
    sys.exit(app.exec_())