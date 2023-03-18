# Import PySide2 module
from PySide2 import *
from PySide2.QtWidgets import *
from revChatGPT.V3 import Chatbot

import threading
#from EdgeGPT import Chatbot
chatbot = Chatbot(api_key="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")
# Create an application instance
app = QApplication([])

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
    print(prompt)
    for data in chatbot.ask_stream(prompt):
        text_edit.insertPlainText(data)

# Define a function to handle submit button click
def submit():
    # Get the input from the line edit
    getThread = threading.Thread(target=getInfo,args=(line_edit.text(),))
    getThread.start()

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

app.exec_()



