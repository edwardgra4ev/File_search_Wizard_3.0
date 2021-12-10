from PyQt5 import QtWidgets, QtCore
from gui import errore_form


class ShowError(QtWidgets.QWidget, errore_form.Error):
    """Класс вывода сообщения об ошибке пользователю"""
    def __init__(self, title: str, text: str, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.textBrowser.setText(text)
        self.setWindowTitle(title)