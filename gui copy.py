# Import PySide2 module
from PyQt6 import *
from PyQt6.QtWidgets import *
from revChatGPT.V3 import Chatbot

import threading
#from EdgeGPT import Chatbot
chatbot = Chatbot(api_key="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")
# Create an application instance
app = QApplication([])
responseMessage=""
newWord=True
# Create a main window
window = QWidget()

# Create a line edit to get user input
line_edit = QLineEdit()

#line_edit.insertPlainText("**hello**")

# Create a text edit to display output
text_edit = QTextEdit()
text_edit.setReadOnly(True)

# Create a submit button to trigger the function
button = QPushButton("Submit")
def getInfo(prompt):
    global responseMessage
    global newWord
    responseMessage = ""
    print(prompt)
    for data in chatbot.ask_stream(prompt):
        newWord = True
        print("data",data)
        responseMessage=data
def runGUI():
    while True:
        QApplication.processEvents()
# Define a function to handle submit button click
def submit():
    global newWord
    # Get the input from the line edit
    getThread = threading.Thread(target=getInfo,args=(line_edit.text(),))
    getThread.start()
    while (getThread.is_alive()):
        if (newWord==True):
            #QApplication.processEvents()
            #print("J")
            text_edit.insertPlainText(responseMessage)
            newWord = False

# Connect the button to the function
button.clicked.connect(submit)
#line_edit.returnPressed.connect(submit)
# Create a vertical layout to place widgets
layout = QVBoxLayout()
layout.addWidget(text_edit)
layout.addWidget(button)
layout.addWidget(line_edit)

# Set the layout to the window
window.setLayout(layout)

# Show the window
window.show()
# Start the main loop

app.exec()



