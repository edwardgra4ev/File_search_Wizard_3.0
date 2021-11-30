import sys
import subprocess
import gui
import errore_form
import json
import os
import datetime
import re
import xml.etree.ElementTree as ET
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog
from qt_material import apply_stylesheet
import asyncio


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
        self.radioButton_standard_str.clicked.connect(self.radio_button_line_search_is_clicked)
        self.radioButton_standard_no_str.clicked.connect(self.radio_button_full_search_is_clicked)
        self.pushButton_directory.clicked.connect(self.director)
        self.pushButton_search.clicked.connect(self.run_search)
        self.listWidget_2.itemDoubleClicked.connect(self.open_file)

    def keyPressEvent(self, event):
        if event.key() in [QtCore.Qt.Key_Enter, QtCore.Qt.Key_Return]:
            self.run_search()
        # строка поиска
        elif event.key() in [QtCore.Qt.Key_F1]:
            self.lineEdit.setFocus()
        # выбор дерриктории
        elif event.key() in [QtCore.Qt.Key_F2]:
            self.director()
        elif event.key() in [QtCore.Qt.Key_F3]:
            self.select_file()

    def open_file(self):
        try:
            select = self.listWidget_2.selectedIndexes()[0].data()
            path = re.search(r"Файл : (.+)\n", select).group(1)
        except IndexError:
            return
        try:
            if sys.platform == 'linux':
                subprocess.check_call(["xdg-open", "--", path])
            elif sys.platform == 'win32':
                subprocess.check_call(["notepad.exe", path])
        except OSError:
            self.widget_error = ShowError(text='Неудалось открыть выбранный файл',
                                          title='Ошибка открытия файла')
            self.widget_error.show()
            return

    def select_file(self):
        try:
            select = self.listWidget_2.selectedIndexes()[0].data()
            path = re.search(r"Файл : (.+)\n", select).group(1)
        except IndexError:
            return
        try:
            if sys.platform == 'win32':
                subprocess.check_call(["explorer.exe", "/Select", f'"{path}"'])
        except OSError:
            self.widget_error = ShowError(text='Неудалось открыть выбранный файл',
                                          title='Ошибка открытия файла')
            self.widget_error.show()
            return

    def radio_button_line_search_is_clicked(self):
        """Если  установлен построчный поиск включаем доступные варианты"""
        if self.radioButton_standard_str.isChecked() is True:
            self.radioButton_standard_st.setText("Поиск в начале строки")
            self.radioButton_standard_st.setEnabled(True)

            self.radioButton_standard_en.setText("Поиск в конце строки")
            self.radioButton_standard_en.setEnabled(True)

            self.checkBox_standard_search_str.setText("Показывать строку с искомым текстом")
            self.checkBox_standard_search_str.setEnabled(True)

    def radio_button_full_search_is_clicked(self):
        """Если поиск установлен на чтение файла целиком отключаем досутпные варианты"""
        if self.radioButton_standard_no_str.isChecked() is True:
            self.radioButton_standard_st.setText('Поиск в начале строки '
                                                 '(Настройка не доступна при "Чтение файла целиком")')
            self.radioButton_standard_st.setEnabled(False)
            self.radioButton_standard_st.setChecked(False)

            self.radioButton_standard_en.setText('Поиск в конце строки '
                                                 '(Настройка не доступна при "Чтение файла целиком")')
            self.radioButton_standard_en.setEnabled(False)
            self.radioButton_standard_en.setChecked(False)

            self.checkBox_standard_search_str.setText('Показывать строку с искомым текстом '
                                                      '(Настройка не доступна при "Чтение файла целиком")')
            self.checkBox_standard_search_str.setEnabled(False)
            self.checkBox_standard_search_str.setChecked(False)

    def director(self):
        """Функция выбора директории"""
        self.path = QFileDialog.getExistingDirectory(self, 'Directory selection', str(os.getcwdb()))

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

    def collection_of_data_for_standard_search(self):
        search_text = self.lineEdit.text()
        if len(search_text) < 3:
            self.widget_error = ShowError(text='Строка поиска не должна содержать менее 3х символов!',
                                          title='Ошибка валидации')
            self.widget_error.show()
            return
        elif self.path is None:
            self.widget_error = ShowError(text='Не указано месторасположение файлов!',
                                          title='Ошибка валидации')
            self.widget_error.show()
            return
        file_search_setting = {}
        # Дата модификации файла
        if self.checkBox_standard_date_modification.isChecked() is True:
            if self.dateEdit_7.date() > self.current_date.currentDate():
                self.widget_error = ShowError(text='Дата модификации файла не может быть больше текущей!',
                                              title='Ошибка валидации')
                self.widget_error.show()
                return
            else:
                file_search_setting.update({"date": self.dateEdit_7.text()})
        else:
            file_search_setting.update({"date": False})
        # Добавляем файлы для проверки
        if self.checkBox_standard_file_name.isChecked() is True:
            in_file_name = self.lineEdit_13.text()
            if in_file_name == '':
                self.widget_error = ShowError(text='При поимке с учетом файла поле не должно быть пустым!',
                                              title='Ошибка валидации')
                self.widget_error.show()
                return
            in_file_name_list = in_file_name.split(',')
            new_in_file_name_list = []
            for file_name in in_file_name_list:
                new_in_file_name_list.append(file_name.strip())
            file_search_setting.update({"file_name": new_in_file_name_list})
        else:
            file_search_setting.update({"file_name": False})
        # Добавляем типы файлов
        file_types = []
        if self.checkBox_txt.isChecked() is True:
            file_types.append(self.checkBox_txt.text().replace('.', ''))
        if self.checkBox_log.isChecked() is True:
            file_types.append(self.checkBox_log.text().replace('.', ''))
        if self.checkBox_xml.isChecked() is True:
            file_types.append(self.checkBox_xml.text().replace('.', ''))
        if self.checkBox_json.isChecked() is True:
            file_types.append(self.checkBox_json.text().replace('.', ''))
        str_file_types = self.lineEdit_14.text()
        if str_file_types != '':
            file_types_list = str_file_types.split(',')
            for types in file_types_list:
                file_types.append(f'.{types.strip()}')
        if file_types == []:
            self.widget_error = ShowError(text='Необходимо указать хотя бы одно расшерение файла!',
                                          title='Ошибка валидации')
            self.widget_error.show()
            return
        else:
            file_search_setting.update({"file_types": file_types})
        if self.radioButton_standard_str.isChecked() is True:
            file_search_setting.update({"entirely_read": True})
        else:
            file_search_setting.update({"entirely_read": False})
        file_search_setting.update({"search_text": search_text})
        return file_search_setting

    def collection_of_data_for_xml_or_json_search(self):
        search_text = self.lineEdit.text()
        if len(search_text) < 3:
            self.widget_error = ShowError(text='Строка поиска не должна содержать менее 3х символов!',
                                          title='Ошибка валидации')
            self.widget_error.show()
            return
        elif self.path is None:
            self.widget_error = ShowError(text='Не указано месторасположение файлов!',
                                          title='Ошибка валидации')
            self.widget_error.show()
            return
        file_search_setting = {}
        # Дата модификации файла
        if self.checkBox_date_modification.isChecked() is True:
            if self.dateEdit_8.date() > self.current_date.currentDate():
                self.widget_error = ShowError(text='Дата модификации файла не может быть больше текущей!',
                                              title='Ошибка валидации')
                self.widget_error.show()
                return
            else:
                file_search_setting.update({"date": self.dateEdit_8.text()})
        else:
            file_search_setting.update({"date": False})
        # Добавляем файлы для проверки
        if self.checkBox_file_name.isChecked() is True:
            in_file_name = self.lineEdit_15.text()
            if in_file_name == '':
                self.widget_error = ShowError(text='При поимке с учетом файла поле не должно быть пустым!',
                                              title='Ошибка валидации')
                self.widget_error.show()
                return
            in_file_name_list = in_file_name.split(',')
            new_in_file_name_list = []
            for file_name in in_file_name_list:
                new_in_file_name_list.append(file_name.strip())
            file_search_setting.update({"file_name": new_in_file_name_list})
        else:
            file_search_setting.update({"file_name": False})
        # Добавляем типы файлов
        file_types = []
        if self.radioButton_xml.isChecked() is True:
            file_types.append('xml')
        elif self.radioButton_json.isChecked() is True:
            file_types.append('json')

        if file_types == []:
            self.widget_error = ShowError(text='Необходимо указать хотя бы одно расшерение файла!',
                                          title='Ошибка валидации')
            self.widget_error.show()
            return
        else:
            file_search_setting.update({"file_types": file_types})
        if self.radioButton_tag_key.isChecked() is True:
            file_search_setting.update({"entirely_read": "KEY"})
        else:
            file_search_setting.update({"entirely_read": "VALUE"})
        file_search_setting.update({"search_text": search_text})
        return file_search_setting

    def standard_run(self):
        if file_search_setting := self.collection_of_data_for_standard_search():
            files = SearchForFileInTheDirectory(path=self.path, file_search_setting=file_search_setting).files
            if files == ():
                self.widget_error = ShowError(text='Не удалось найти нужные файлы',
                                              title='Ошибка поиска файлов')
                self.widget_error.show()
                return
            else:
                if self.radioButton_standard_no_reg.isChecked() is True:
                    command = '1'
                if self.radioButton_standard_reg.isChecked() is True:
                    command = '2'
                if self.radioButton_standard_st.isChecked() is True:
                    command = '3'
                if self.radioButton_standard_en.isChecked() is True:
                    command = '4'
                if self.radioButton_standard_re.isChecked() is True:
                    command = '5'
                self.progressBar.setMaximum(len(files))
                self.progressBar.show()
                self.thread = QtCore.QThread(parent=self)
                self.thread.started.connect(SearchingTextForFile(
                    files_path=files,
                    search_text=file_search_setting.get('search_text'),
                    type_search=command,
                    gui=self,
                    line_read=file_search_setting.get('entirely_read'),
                ).start_search)
                self.thread.start()
                self.thread.quit()

    def json_run(self):
        if file_search_setting := self.collection_of_data_for_xml_or_json_search():
            files = SearchForFileInTheDirectory(path=self.path, file_search_setting=file_search_setting).files
            if files == ():
                self.widget_error = ShowError(text='Не удалось найти нужные файлы',
                                              title='Ошибка поиска файлов')
                self.widget_error.show()
                return
            else:
                self.progressBar.setMaximum(len(files))
                self.progressBar.show()
                asyncio.run(JsonSearch(files_path=files,
                           search_value=file_search_setting.get('search_text'),
                           gui=self,
                           type_search=file_search_setting.get('entirely_read')).start_search())

    def xml_run(self):
        if file_search_setting := self.collection_of_data_for_xml_or_json_search():
            files = SearchForFileInTheDirectory(path=self.path, file_search_setting=file_search_setting).files
            if files == ():
                self.widget_error = ShowError(text='Не удалось найти нужные файлы',
                                              title='Ошибка поиска файлов')
                self.widget_error.show()
                return
            else:
                self.progressBar.setMaximum(len(files))
                self.progressBar.show()
                asyncio.run(XMLSearch(files_path=files,
                                       search_value=file_search_setting.get('search_text'),
                                       gui=self,
                                       type_search=file_search_setting.get('entirely_read')).start_search())

    def run_search(self):
        self.progressBar.setValue(0)
        self.listWidget_2.clear()
        if self.radioButton_standard.isChecked() is True:
            self.standard_run()
        elif self.radioButton_xml.isChecked() is True:
            self.xml_run()
        elif self.radioButton_json.isChecked() is True:
            self.json_run()

    def add_result_to_widget_list(self, data) -> None:
        if data == {'files_error': []}:
            self.widget_error = ShowError(text='Нет результатов в соотвествии с критериями поиска!',
                                          title='Результат выполнения')
            self.widget_error.show()
            return
        if self.radioButton_standard.isChecked() is True:
            for key, value in data.items():
                if key != 'files_error':
                    lst = ["╔═══════════════════════════════════════════• ✤ •═══════════════════════════════════════════╗\n"]
                    if self.checkBox_standard_path.isChecked() is True:
                        lst.append(f" Файл : {key}\n")
                    if self.checkBox_standard_count.isChecked() is True:
                        lst.append(f" Кол-во повторений искомого текста : {value[0]}\n")
                    if self.checkBox_standard_search_str.isChecked() is True:
                        lst.append(f" Строка с искомым текстом : {value[1]}\n")
                    lst.append("╚═════════════════════════════════════════════════════════════════════════════════════════╝")
                    self.listWidget_2.addItem("".join(lst))
        if self.radioButton_xml.isChecked() is True or self.radioButton_json.isChecked() is True:
            for key, value in data.items():
                if key != 'files_error':
                    lst = [
                        "╔═══════════════════════════════════════════• ✤ •═══════════════════════════════════════════╗\n"]
                    if self.checkBox_path.isChecked() is True:
                        lst.append(f" Файл : {key}\n")
                    if self.checkBox_count.isChecked() is True:
                        lst.append(f" Кол-во повторений искомого текста : {value}\n")
                    lst.append(
                        "╚═════════════════════════════════════════════════════════════════════════════════════════╝")
                    self.listWidget_2.addItem("".join(lst))
        if len(data.get("files_error")) > 0:
            self.listWidget_2.addItem(
                f"╔═══════════════════════════════════════════• ✤ •═══════════════════════════════════════════╗\n"
                f"Неудалось прочесть следующие файлы: {data.get('files_error')}\n"
                f"╚═════════════════════════════════════════════════════════════════════════════════════════╝"
            )


class ShowError(QtWidgets.QWidget, errore_form.Error):
    def __init__(self, title: str, text: str, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.textBrowser.setText(text)
        self.setWindowTitle(title)


class SearchForFileInTheDirectory(object):
    """Класс который ищетнужные файлы в указанной дирректории"""
    def __init__(self, path, file_search_setting: dict = None):
        self.path = path
        self.file_search_setting = file_search_setting
        self.files = self.create_files_tuple()

    def _getting_file_path(self) -> tuple:
        """Получаем все файлы в нужной дерриктории"""
        try:
            file_list = os.listdir(self.path)  # получение списка файлов
        except FileNotFoundError:
            return ()
        file_list = [os.path.join(self.path, i) for i in file_list]
        file_list = sorted(file_list, key=os.path.getmtime)  # Сортировка списка
        file_list.reverse()  # Переворачивание списка
        return tuple(file_list)

    def _filtering_files_by_format(self) -> dict:
        """Ищем файлы с нужным расширением и создаем словарь {файл: дата модификации}"""
        files_tuple = self._getting_file_path()
        files_and_modification_date = {}
        for file in files_tuple:
            format = self.file_search_setting.get('file_types')
            format = '|'.join(format)
            if re.search(r"\.({})".format(format), file):
                if self.file_search_setting.get("file_name") is False:
                    file_create_date = datetime.datetime.fromtimestamp(os.path.getmtime(file))
                    files_and_modification_date.update({file: str(file_create_date)})
                else:
                    for fl in self.file_search_setting.get("file_name"):
                        if fl in file.split('\\')[-1]:
                            file_create_date = datetime.datetime.fromtimestamp(os.path.getmtime(file))
                            files_and_modification_date.update({file: str(file_create_date)})
                            break
        return files_and_modification_date

    def create_files_tuple(self) -> tuple:
        """
        Функция сравнения даты модификации файла и даты указанной пользователем.
        Если дата не передана возращает tuple всех файлов
        """
        files_and_modification_date = self._filtering_files_by_format()
        date = self.file_search_setting.get('date')
        if date is False:
            files = []
            for file in files_and_modification_date.keys():
                files.append(file)
            return tuple(files)

        date = date.replace('.', '-')
        date = date.split('-')
        new_date = f'{date[2]}-{date[1]}-{date[0]}'
        # Сравниваем даты
        files = []
        for file, file_date in files_and_modification_date.items():
            if file_date[:10] == new_date:
                files.append(file)
        return tuple(files)


class JsonSearch(object):
    """
    Класс реализующий поиск в Json по ключу или значению.
    Поиск проходит путем поиска подстроки в строке без учета регистра.
    "fan" in "Fantasy" будет успешный результат
    """
    def __init__(self, files_path: list[str], search_value: str or int, type_search: str, gui):
        self.files_path = files_path
        self.search_value = search_value
        self.type_search = type_search
        self.gui = gui

    def _key_search(self, *, json_obj: json, result_lst: list = None, key: str) -> list:
        """Поиск в json по ключу"""
        if result_lst is None:
            result_lst = []
        if isinstance(json_obj, list):
            for item in json_obj:
                self._key_search(json_obj=item, result_lst=result_lst, key=key)
        if isinstance(json_obj, dict):
            for item_key in json_obj.keys():
                value = json_obj[item_key]
                if key.lower() in str(item_key).lower():
                    result_lst.append(value)
                else:
                    self._key_search(json_obj=value, result_lst=result_lst, key=key)
        return result_lst

    def _value_search(self, *, json_obj: json, result_lst: list = None, value: str) -> list:
        """Поиск в json по значению"""
        if result_lst is None:
            result_lst = []
        if isinstance(json_obj, list):
            for item in json_obj:
                self._value_search(json_obj=item, result_lst=result_lst, value=value)
        if isinstance(json_obj, dict):
            for item_value in json_obj.values():
                if value.lower() in str(item_value).lower():
                    result_lst.append(value)
                else:
                    self._value_search(json_obj=item_value, result_lst=result_lst, value=value)
        return result_lst

    async def start_search(self) -> dict:
        """Функция читает файлы и запускает функцию парсинга"""
        result = {}
        files_error = []
        for file_path in self.files_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as json_file:
                    # Заполняем прогресс бар при чтении нового файла
                    self.gui.progressBar.setValue(self.gui.progressBar.value() + 1)
                    json_obj = json.load(json_file)
                    if self.type_search == 'KEY':
                        result_search = self._key_search(json_obj=json_obj, key=self.search_value)
                    elif self.type_search == 'VALUE':
                        result_search = self._value_search(json_obj=json_obj, value=self.search_value)
                    if result_search:
                        result.update({file_path: len(result_search)})
            except json.JSONDecodeError or TypeError:
                files_error.append(file_path)
        result.update({"files_error": files_error})
        self.gui.add_result_to_widget_list(result)


class SearchingTextForFile(object):
    """
    Класс реализует поиск в файле построчно и нет.
    1: поиск без учета регистра
    2: поиск с учетом регистра
    3: поиск в начале строки
    4: поиск в конце строки
    5: поиск регулярным выражением
    """
    def __init__(self, files_path: list[str], search_text: str, type_search: str,
                 gui, line_read: bool):
        self.method_search = {
            "1": self._no_case_insensitive_search,
            "2": self._case_insensitive_search,
            "3": self._search_at_the_beginning_of_line,
            "4": self._search_at_the_end_of_line,
            "5": self._case_insensitive_search,
        }
        self.files_path = files_path
        self.search_text = search_text
        self.type_search = type_search
        self.gui = gui
        self.line_read = line_read

    def _no_case_insensitive_search(self, text: str) -> int:
        """
        Поиск без учета регистра
        """
        return len(re.findall(self.search_text.upper(), text.upper()))

    def _case_insensitive_search(self, text: str) -> int:
        """
        Поиск с учетом регистра, так же используеться при поиске регулярным выражением
        """
        return len(re.findall(self.search_text, text))

    def _search_at_the_beginning_of_line(self, text: str) -> int:
        """
        Поиск в начале строки
        """
        if text.upper().startswith(self.search_text.upper().strip()):
            return 1
        return 0

    def _search_at_the_end_of_line(self, text: str) -> int:
        """
        Поиск в конце строки
        """
        if text.upper().endswith(self.search_text.upper().strip()):
            return 1
        return 0

    def start_search(self) -> dict:
        """Функция читает файлы и запускает функцию парсинга"""
        result = {}
        files_error = []
        method = self.method_search.get(self.type_search)
        for file_path in self.files_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    # Заполняем прогресс бар при чтении нового файла
                    self.gui.progressBar.setValue(self.gui.progressBar.value() + 1)
                    # Построчный поиск в файле
                    if self.line_read:
                        count_result = 0
                        lines = []
                        for line in file.readlines():
                            result_search = method(line)
                            if result_search:
                                count_result += result_search
                                lines.append(line.strip())
                        if count_result:
                            result.update({file_path: (count_result, lines)})
                    # Чтение файла целиком
                    else:
                        file_text = file.read()
                        result_search = method(file_text)
                        if result_search:
                            result.update({file_path: (result_search, file_text)})
            except UnicodeDecodeError or TypeError:
                files_error.append(file_path)
        result.update({"files_error": files_error})
        self.gui.add_result_to_widget_list(result)


class XMLSearch(object):
    """
    Класс реализующий поиск в XML по ключу или значению.
    Поиск проходит путем поиска подстроки в строке без учета регистра.
    "fan" in "Fantasy" будет успешный результат
    """
    def __init__(self, files_path: list[str], search_value: str or int, type_search: str, gui):
        self.files_path = files_path
        self.search_value = search_value
        self.types_search = type_search
        self.gui = gui

    def _key_search(self, *, root: ET, result_lst: list = None, key: str) -> list:
        """Поиск в xml по ключу"""
        if result_lst is None:
            result_lst = []
        for children in root:
            if key.upper() in children.tag.upper():
                result_lst.append(children.tag)
            else:
                self._key_search(root=children, result_lst=result_lst, key=key)
        return result_lst

    def _value_search(self, *, root: ET, result_lst: list = None, value: str) -> list:
        """Поиск в xml по значению"""
        if result_lst is None:
            result_lst = []
        for children in root:
            if value.upper() in children.text.upper():
                result_lst.append(children.text)
            else:
                self._value_search(root=children, result_lst=result_lst, value=value)
        return result_lst

    async def start_search(self) -> dict:
        """Функция читает файлы и запускает функцию парсинга"""
        result = {}
        files_error = []
        for file_path in self.files_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as xml_file:
                    # Заполняем прогресс бар при чтении нового файла
                    self.gui.progressBar.setValue(self.gui.progressBar.value() + 1)
                    root = ET.parse(xml_file).getroot()
                    if self.types_search == 'KEY':
                        result_search = self._key_search(root=root, key=self.search_value)
                    elif self.types_search == 'VALUE':
                        result_search = self._value_search(root=root, value=self.search_value)
                    if result_search:
                        result.update({file_path: len(result_search)})
            except ET.ParseError or TypeError:
                files_error.append(file_path)
        result.update({"files_error": files_error})
        self.gui.add_result_to_widget_list(result)


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    apply_stylesheet(app, theme='dark_teal.xml')
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()