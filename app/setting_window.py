import sys
import os
from PyQt5 import QtWidgets
from gui import setting_gui

from app.update_window import UpdateForm
from utils.config_parser import Parser
from utils.application_update import Update


class ShowSetting(QtWidgets.QWidget, setting_gui.Setting):
    def __init__(self, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.parser = Parser()
        self.add_data()
        self.pushButton.clicked.connect(self.check_update)
        self.pushButton_2.clicked.connect(self.save_setting)

    def save_setting(self):
        current_theme = self.parser.get_current_theme()
        second = self.spinBox.text()
        theme = self.comboBox.currentText()
        self.parser.save_current_theme(theme)
        self.parser.save_time_limit(second)
        if theme != current_theme:
            os.startfile("File_search_Wizard_3.0.exe")
            sys.exit(1)
        else:
            self.close()

    def check_update(self):
        update = Update()
        if update.check_new_version(self.parser.get_version()) is True:
            update_form = UpdateForm(update)
            update_form.show()
        else:
            self.parser.save_last_update_time()
            self.label_5.setText(str(self.parser.get_last_update_time()))

    def add_data(self):
        self.label_3.setText(str(self.parser.get_version()))
        self.label_5.setText(str(self.parser.get_last_update_time()))
        self.spinBox.setValue(int(self.parser.get_time_limit()))
        current_theme = str(self.parser.get_current_theme())
        all_themes = self.parser.get_all_themes()
        self.comboBox.addItems(all_themes)
        index = all_themes.index(current_theme)
        self.comboBox.setCurrentIndex(index)

