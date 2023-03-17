from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QHBoxLayout, QVBoxLayout, QWidget, QPushButton,
    QLabel, QScrollArea, QSizePolicy, QFrame, QTextEdit, QGridLayout
)


class ChatWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set up window
        self.setWindowTitle('Chat')
        self.resize(400, 600)

        # Set up layout
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # Set up scroll area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area_content = QWidget(scroll_area)
        scroll_area_layout = QVBoxLayout(scroll_area_content)
        scroll_area_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        scroll_area.setWidget(scroll_area_content)
        main_layout.addWidget(scroll_area)

        # Add message cards to scroll area
        for i in range(10):
            message_card = MessageCard(
                sender='User {}'.format(i),
                message='Hello, world!'
            )
            scroll_area_layout.addWidget(message_card)


class MessageCard(QFrame):
    def __init__(self, sender, message):
        super().__init__()

        # Set up layout
        main_layout = QHBoxLayout()
        self.setLayout(main_layout)

        # Set up label for sender
        sender_label = QLabel(sender)
        main_layout.addWidget(sender_label)

        # Set up label for message
        message_label = QTextEdit(message)
        message_label.setReadOnly(True)
        message_label.setFrameShape(QFrame.Shape.NoFrame)
        message_label.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        main_layout.addWidget(message_label)


if __name__ == '__main__':
    app = QApplication([])
    window = ChatWindow()
    window.show()
    app.exec()
