from lib import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import qdarkstyle
import threading


class ChatBubble(QWidget):
    def __init__(self, message, isSentByMe):
        super().__init__()
        
        self.message = message
        self.isSentByMe = isSentByMe
        self.initUI()

    def initUI(self):
        self.textEdit = GrowingTextEdit(isSentByMe=self.isSentByMe,heightMin=15,heightMax=65000)
        self.textEdit.setReadOnly(True)
        self.textEdit.setFrameStyle(QTextEdit.NoFrame)
        self.textEdit.document().setDocumentMargin(10)
        self.setMaximumWidth(700)
        self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit.viewport().setAutoFillBackground(False)
        if (self.isSentByMe):
            self.textEdit.setStyleSheet("""
            QTextEdit {
                background-color: #19232D;
                color: #ffffff;
                border-radius: 10px;
                padding: 8px;
                font-size: 14px;
            }
            """)
        else:
            self.textEdit.setStyleSheet("""
            QTextEdit {
                background-color: #455364;
                color: #ffffff;
                border-radius: 10px;
                padding: 8px;
                font-size: 14px;
            }
            """)
        self.layout = QHBoxLayout(self)
        self.layout.addWidget(self.textEdit)
        self.layout.setContentsMargins(0, 0, 0, 0)
        
    def appendMessage(self, message):
        #workaround api oddities where there is no space after punctuation
        self.textEdit.moveCursor(QTextCursor.End)
        if (message == "," or message == "." or message == "!" or message == "?"):
            self.textEdit.insertPlainText(message+" ")
        else:
            self.textEdit.insertPlainText(message)

class GrowingTextEdit(QTextEdit):
    def __init__(self, isSentByMe,heightMin,heightMax,*args, **kwargs):
        super(GrowingTextEdit, self).__init__(*args, **kwargs)  
        self.document().contentsChanged.connect(self.sizeChange)
        #use isSentByMe to check if this is human entered or GPT test
        self.isSentByMe = isSentByMe
        self.heightMin = heightMin
        self.heightMax = heightMax

    def sizeChange(self):
        #workaround api oddities where AI generated messages have a larger height than non gpt messages
        if (self.isSentByMe):
            docHeight = self.document().size().height()+10
        else:
            docHeight = self.document().size().height()-2
        if self.heightMin <= docHeight <= self.heightMax:
            self.setMinimumHeight(int(docHeight)+20)
class ChatWindow(QWidget):
    messageReceived = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        #load theme
        darkStylesheet = qdarkstyle.load_stylesheet_pyqt5()
        self.setStyleSheet(darkStylesheet)
        #connect socket for sending messages to GUI
        self.messageReceived.connect(self.addToResponse)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Chat Window')
        #Set minimum width of window to make sure chat experience is consistent
        self.setGeometry(100, 100, 770, 1000) 
        self.setMinimumWidth(770)
        
        self.scrollArea = QScrollArea()
        self.scrollArea.setWidgetResizable(True)

        self.scrollAreaLayout = QVBoxLayout()
        self.scrollAreaLayout.setAlignment(Qt.AlignCenter)

        self.scrollAreaWidget = QWidget()
        self.scrollAreaWidget.setLayout(self.scrollAreaLayout)

        self.scrollArea.setWidget(self.scrollAreaWidget)
        #add spacer, this is to ensure chat bubbles don't fill the screen when they are created
        self.spacerItem = QSpacerItem(20, 10000, QSizePolicy.Minimum, QSizePolicy.Expanding)
        
        self.messageInput = QTextEdit()
        self.messageInput.setPlaceholderText("Chat Message Here...")
        self.messageInput.setMaximumHeight(100)

        self.sendButton = QPushButton('Send')
        self.sendButton.clicked.connect(self.sendMessage)

        self.inputLayout = QVBoxLayout()
        self.inputLayout.addWidget(self.messageInput)
        self.inputLayout.addWidget(self.sendButton)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.scrollArea)
        self.mainLayout.addLayout(self.inputLayout)

        self.setLayout(self.mainLayout)
    def getResponse(self,prompt):
        for data in chatbot.ask_stream(prompt):
            #emit signal to GUI thread to update responseBubble
            self.messageReceived.emit(data)
        return
    def sendMessage(self):
        message = self.messageInput.toPlainText()
        print(message)
        if message:
            self.chatBubble = ChatBubble("", True)
            self.scrollAreaLayout.removeItem(self.spacerItem)
            self.scrollAreaLayout.addWidget(self.chatBubble)
            self.scrollAreaLayout.addItem(self.spacerItem)
            self.chatBubble.appendMessage(message)
            
            self.messageInput.setText('') 
            
            self.responseBubble = ChatBubble("", False)
            self.scrollAreaLayout.removeItem(self.spacerItem)
            self.scrollAreaLayout.addWidget(self.responseBubble)
            self.scrollAreaLayout.addItem(self.spacerItem)
            t = threading.Thread(target=self.getResponse, args=(message,))
            t.start()
    def addToResponse(self,data):
        self.responseBubble.appendMessage(data)
            
