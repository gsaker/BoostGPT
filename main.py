from gui import ChatWindow
from PyQt5 import QtWidgets
import sys 
import lib

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    chatWindow = ChatWindow()
    chatWindow.show()
    sys.exit(app.exec_())