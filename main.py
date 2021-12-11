import os
import sys

from PyQt5.QtWidgets import QApplication
from qt_material import apply_stylesheet
from elevate import elevate

from app.error_window import ShowError
from app import main_window
from app.update_window import UpdateForm

from utils.application_update import Update
from utils.config import *


def show_main_window():
    app = QApplication(sys.argv)
    main = main_window.MainWindow()
    apply_stylesheet(app, theme=THEMES)
    main.show()
    app.exec_()


def show_update_form(update):
    app = QApplication(sys.argv)
    update_form = UpdateForm(update)
    apply_stylesheet(app, theme=THEMES)
    update_form.show()
    return app.exec_()


def show_error_form(title: str, text: str):
    app = QApplication(sys.argv)
    error_form = ShowError(title, text)
    apply_stylesheet(app, theme=THEMES)
    error_form.show()
    app.exec_()


def search_old_version_app_and_remove():
    """Находим старую версию и удаляем ее"""
    try:
        if os.path.isfile("File_search_Wizard_3.0_OLD_VERSION.exe") is True:
            os.remove('File_search_Wizard_3.0_OLD_VERSION.exe')
    except FileNotFoundError as err:
        show_error_form("Ошибка удаления старой версии файла!", str(err))


def check_new_version():
    """Проверяем дату поледнего обновления, если она больше заданного параметра проверяем обновление"""
    update = Update()
    if update.check_new_version(CONSTANT_VERSION) is True:
        if show_update_form(update) == 0:
            show_main_window()
            sys.exit(0)


def main():
    # Запросить права администратора
    try:
        elevate(show_console=False)
        search_old_version_app_and_remove()
        if check_new_version() is None:
            show_main_window()
    except OSError or KeyError or ValueError:
        show_main_window()


if __name__ == '__main__':
    main()