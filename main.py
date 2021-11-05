import sys
from typing import Optional
import gui
import json
import os
import datetime
from PySide6 import QtWidgets
from PySide6.QtWidgets import QFileDialog

from qt_material import apply_stylesheet


class ExampleApp(QtWidgets.QMainWindow, gui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.path = None
        self.widget_error = None
        self.progressBar.hide()
        self.stackedWidget.hide()
        self.lineEdit.setFocus()
        self.groupBox_setting.clicked.connect(self.group_box_setting_is_checked)
        self.radioButton_standard.clicked.connect(self.page_switching)
        self.radioButton_xml.clicked.connect(self.page_switching)
        self.radioButton_json.clicked.connect(self.page_switching)

    def director(self):
        """Функция выбора директории"""
        self.path = QFileDialog.getExistingDirectory(options=QFileDialog.DontUseNativeDialog)

    def group_box_setting_is_checked(self):
        """Скрытие или отображение stackedWidget"""
        if self.groupBox_setting.isChecked() is False:
            self.stackedWidget.hide()
        else:
            self.stackedWidget.show()

    def page_switching(self):
        """Переключение страниц stackedWidget"""
        if self.radioButton_standard.isChecked() is True:
            self.stackedWidget.setCurrentIndex(0)
        else:
            self.stackedWidget.setCurrentIndex(1)


class SearchForFileInTheDirectory(object):
    """Класс для поиска файла в каталоге"""
    def __init__(self):
        self.path = None
        self.file_types = None
        self.date_of_modification = None

    def _getting_file_path(self) -> tuple:
        """Получаем все файлы в нужной дерриктории"""
        file_list = os.listdir(self.path)  # получение списка файлов
        file_list = [os.path.join(self.path, i) for i in file_list]
        file_list = sorted(file_list, key=os.path.getmtime)  # Сортировка списка
        file_list.reverse()  # Переворачивание списка
        return tuple(file_list)

    def _filtering_files_by_format_and_add_modification_date(self) -> dict:
        """Ищем файлы с нужным расширением и создаем словарь {файл: дата модификации}"""
        files_tuple = self._getting_file_path()
        files_and_modification_date = {}
        for file in files_tuple:
            # Получаем расширение файла
            _, file_extension = os.path.splitext(file)
            file_extension = file_extension.lower()
            if file_extension in self.file_types:
                # Получаем дату модификации файла
                file_modification_date = datetime.datetime.fromtimestamp(os.path.getmtime(file))
                files_and_modification_date.update({file: str(file_modification_date)})
        return files_and_modification_date

    def create_files_tuple(self, path: str, file_types: list, date_of_modification: Optional[str] = None) -> tuple:
        """
        Функция сравнения даты модификации файла и даты указанной пользователем.
        Если дата не передана возращает tuple всех файлов.
        Входные данные:

        path: str - путь к дериктории с файлами
        file_types: lst[str] - расширения файлов в формате .json, .txt ...
        date_of_modification: str = None - в формате YYYY-mm-dd
        """

        self.path = path
        self.file_types = file_types
        self.date_of_modification = date_of_modification

        files_and_modification_date = self._filtering_files_by_format_and_add_modification_date()
        # Если не передали дату модификации
        if self.date_of_modification is None:
            return tuple(file for file in files_and_modification_date.keys())
        # Если передали
        return tuple(file for file, file_modification_date in files_and_modification_date.items() if
                     file_modification_date[:10] == self.date_of_modification)


class JsonSearch(object):
    def __init__(self, files_path: list[str], search_value: str or int, type_search: str):
        self.files_path = files_path
        self.search_value = search_value
        self.type_search = type_search
        self._сhecking_the_input_data()

    def _сhecking_the_input_data(self):
        if isinstance(self.files_path, list) is not True:
            raise ValueError("files_path must be of type list")
        else:
            str_list = [item for item in self.files_path if isinstance(item, str)]
            if len(self.files_path) != len(str_list):
                raise ValueError("files_path: list[str] must contain only strings")
        if isinstance(self.search_value, str) is not True:
            raise ValueError("search_value must be of type str")
        self.type_search = self.type_search.upper()
        if self.type_search not in ("TAG", "KEY"):
            raise ValueError("type_search must be equal to tag or key")




def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    apply_stylesheet(app, theme='dark_teal.xml')
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()