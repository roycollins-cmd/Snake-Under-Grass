from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication

Form, Window = uic.loadUiType('highlight.ui')


class MyWindow(Window, Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def keyPressEvent(self, event):
        if Qt.Key.Key_A <= event.key() <= Qt.Key.Key_Z:
            letter = chr(event.key())
            widget_name = f'key{letter}'

            widget = getattr(self, widget_name, None)
            if widget:
                widget.setStyleSheet('background-color:lightgreen')

            #self.keyQ.setStyleSheet('background-color:lightgreen')
        #elif event.key() == Qt.Key.Key_W:
            #self.keyW.setStyleSheet('background-color:lightgreen')

    def keyReleaseEvent(self, event):
        if Qt.Key.Key_A <= event.key() <= Qt.Key.Key_Z:
            letter = chr(event.key())
            widget_name = f'key{letter}'

            widget = getattr(self, widget_name, None)
            if widget:
                widget.setStyleSheet('')

            #self.keyQ.setStyleSheet('')
        #elif event.key() == Qt.Key.Key_W:
            #self.keyW.setStyleSheet('')

app = QApplication([])
window = MyWindow()
window.show()
app.exec()