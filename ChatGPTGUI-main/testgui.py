import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QScrollArea
from PyQt5.QtGui import QFont, QPainter, QColor, QBrush, QPen
from PyQt5.QtCore import Qt

class ChatBubble(QWidget):
    def __init__(self, message, is_sent_by_me):
        super().__init__()
        self.message = message
        self.is_sent_by_me = is_sent_by_me
        self.initUI()

    def initUI(self):
        self.message_label = QLabel(self.message)
        self.message_label.setWordWrap(True)
        self.message_label.setFont(QFont('Arial', 10))
        self.message_label.setStyleSheet('background-color: #f0f0f0; padding: 8px; border-radius: 10px;')
        self.message_label.setMaximumWidth(300)

        self.message_layout = QHBoxLayout()
        self.message_layout.addWidget(self.message_label)
        self.message_layout.setAlignment(Qt.AlignRight if self.is_sent_by_me else Qt.AlignLeft)

        self.setLayout(self.message_layout)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        pen = QPen(QColor('#cccccc'), 2, Qt.SolidLine)
        painter.setPen(pen)

        brush = QBrush(Qt.white, Qt.SolidPattern)
        painter.setBrush(brush)

        rect = self.rect()
        rect.adjust(1, 1, -1, -1)
        painter.drawRoundedRect(rect, 10, 10)

class ChatWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Chat Window')
        self.setGeometry(100, 100, 400, 600)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.scroll_area_widget = QWidget()
        self.scroll_area_layout = QVBoxLayout()
        self.scroll_area_layout.setAlignment(Qt.AlignTop)
        self.scroll_area_widget.setLayout(self.scroll_area_layout)

        self.scroll_area.setWidget(self.scroll_area_widget)

        self.message_input = QLineEdit()
        self.send_button = QPushButton('Send')
        self.send_button.clicked.connect(self.send_message)

        self.input_layout = QHBoxLayout()
        self.input_layout.addWidget(self.message_input)
        self.input_layout.addWidget(self.send_button)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.scroll_area)
        self.main_layout.addLayout(self.input_layout)

        self.setLayout(self.main_layout)

    def send_message(self):
        message = self.message_input.text()
        if message:
            chat_bubble = ChatBubble(message, True)
            self.scroll_area_layout.addWidget(chat_bubble)
            self.message_input.setText('')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    chat_window = ChatWindow()
    chat_window.show()
    sys.exit(app.exec_())