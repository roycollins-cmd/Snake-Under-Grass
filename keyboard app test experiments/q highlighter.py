from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication

Form, Window = uic.loadUiType('highlight.ui')


class MyWindow(Window, Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Q:
            self.keyQ.setStyleSheet('background-color:lightgreen')

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key.Key_Q:
            self.keyQ.setStyleSheet('')

app = QApplication([])
window = MyWindow()
window.show()
app.exec()