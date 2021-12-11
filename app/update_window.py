import os
import sys

from PyQt5 import QtWidgets

from gui import update_gui
from utils.config_parser import Parser


class UpdateForm(QtWidgets.QMainWindow, update_gui.UI_Form):
    def __init__(self, update):
        super().__init__()
        self.setupUi(self)
        self.update = update
        self.progressBar.hide()
        self.textBrowser.setText(f"Доступна новая версия приложения: { self.update.new_version}\n"
                                 f"Список изменений:\n{ self.update.body}")
        self.pushButton.clicked.connect(self._exit_window)
        self.pushButton_2.clicked.connect(self._updates)

    def _exit_window(self):
        self.close()

    def _updates(self):
        self.progressBar.show()
        self.progressBar.setValue(0)
        self.update._rename_file()
        self.update._download_new_version(self.progressBar)
        Parser().save_last_update_time()
        os.startfile("File_search_Wizard_3.0.exe")
        sys.exit(1)