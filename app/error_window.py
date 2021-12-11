from PyQt5 import QtWidgets, QtCore
from gui import error_gui


class ShowError(QtWidgets.QWidget, error_gui.Error):
    """Класс вывода сообщения об ошибке пользователю"""
    def __init__(self, title: str, text: str, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.textBrowser.setText(text)
        self.setWindowTitle(title)