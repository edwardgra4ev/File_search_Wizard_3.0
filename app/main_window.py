import re
import sys
import os
import subprocess
import asyncio

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog
from gui import main_gui

from app.error_window import ShowError

from utils.files_search import SearchForFileInTheDirectory
from utils.json_search import JsonSearch
from utils.text_search import SearchingTextForFile
from utils.xml_search import XMLSearch
from utils.config import *
import icon


class MainWindow(QtWidgets.QMainWindow, main_gui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pre_launch_setup()
        self.path = None
        self.widget_error = None
        self.widget_setting = None
        self.result_search = None
        self.show_or_hide_setting()
        self.groupBox_3.clicked.connect(self.show_or_hide_setting)
        self.radio_button_list.clicked.connect(self.show_list_or_tree)
        self.radio_button_tree.clicked.connect(self.show_list_or_tree)
        self.radio_button_standard_search.clicked.connect(self.page_switching)
        self.radio_button_xml_search.clicked.connect(self.page_switching)
        self.radio_button_json_search.clicked.connect(self.page_switching)
        self.push_button_dir.clicked.connect(self.directory_selection)
        self.radio_button_str_read.clicked.connect(self.radio_button_line_search_is_clicked)
        self.radio_button_full_read.clicked.connect(self.radio_button_full_search_is_clicked)
        self.push_button_serach.clicked.connect(self.run_search)
        self.listWidget.viewport().installEventFilter(self)
        self.treeWidget.viewport().installEventFilter(self)
        self.treeWidget.itemDoubleClicked.connect(self.itemDoubleClicked_none)
        #self.groupBox_setting.clicked.connect(self.group_box_setting_is_checked)
        # self.radioButton_standard.clicked.connect(self.page_switching)
        # self.radioButton_xml.clicked.connect(self.page_switching)
        # self.radioButton_json.clicked.connect(self.page_switching)
        # self.radioButton_standard_str.clicked.connect(self.radio_button_line_search_is_clicked)
        # self.radioButton_standard_no_str.clicked.connect(self.radio_button_full_search_is_clicked)
        # self.pushButton_directory.clicked.connect(self.director)
        # self.pushButton_search.clicked.connect(self.run_search)
        # self.listWidget_2.viewport().installEventFilter(self)

    def itemDoubleClicked_none(self):
        return

    def pre_launch_setup(self) -> None:
        self.setWindowIcon(QtGui.QIcon(':/icon/icon.ico'))
        self.version.setText("Версия: %s" % CONSTANT_VERSION)
        current_date = QtCore.QDate()
        font = self.line_edit_search.font()
        font.setPointSize(15)
        self.line_edit_search.setFont(font)
        self.line_edit_search.setFocus()
        self.line_edit_search.setAlignment(QtCore.Qt.AlignCenter)
        self.date_edit.setDate(current_date.currentDate())
        self.line_edit_file_name.setPlaceholderText(
            'Пример: "test, file". Результат: ["test.txt", "my_test.json", "file1.xml"]')
        self.line_edit_files_format.setPlaceholderText('Пример: doc, docx, md')
        self.progressBar.hide()
        self.progressBar.setValue(0)

    def show_or_hide_setting(self):
        """Скрывает или показывает блок настроек"""
        if self.groupBox_3.isChecked() is True:
            for widget in self.groupBox_3.findChildren(QtWidgets.QFrame):
                widget.show()
        elif self.groupBox_3.isChecked() is False:
            for widget in self.groupBox_3.findChildren(QtWidgets.QFrame):
                widget.hide()

    def show_list_or_tree(self):
        """Переключает результат отображения на древо или лист"""
        if self.radio_button_list.isChecked() is True:
            self.stackedWidget_2.setCurrentIndex(0)
            self.listWidget.clear()
            self.groupBox_33.show()
            self.groupBox_27.show()
        elif self.radio_button_tree.isChecked() is True:
            self.stackedWidget_2.setCurrentIndex(1)
            self.treeWidget.clear()
            self.groupBox_33.hide()
            self.groupBox_27.hide()

    def radio_button_line_search_is_clicked(self):
        """Если  установлен построчный поиск включаем доступные варианты"""
        if self.radio_button_str_read.isChecked() is True:
            self.radio_button_st.setText("Поиск в начале строки")
            self.radio_button_st.setEnabled(True)
            self.radio_button_en.setText("Поиск в конце строки")
            self.radio_button_en.setEnabled(True)
            self.check_box_standard_search_str.setText("Показывать строку с искомым текстом")
            self.check_box_standard_search_str.setEnabled(True)

    def radio_button_full_search_is_clicked(self):
        """Если поиск установлен на чтение файла целиком отключаем досутпные варианты"""
        if self.radio_button_full_read.isChecked() is True:
            self.radio_button_st.setText('Поиск в начале строки '
                                         '(Настройка не доступна при "Чтение файла целиком")')
            self.radio_button_st.setEnabled(False)
            self.radio_button_st.setChecked(False)

            self.radio_button_en.setText('Поиск в конце строки '
                                         '(Настройка не доступна при "Чтение файла целиком")')
            self.radio_button_en.setEnabled(False)
            self.radio_button_en.setChecked(False)

            self.check_box_standard_search_str.setText('Показывать строку с искомым текстом '
                                                       '(Настройка не доступна при "Чтение файла целиком")')
            self.check_box_standard_search_str.setEnabled(False)
            self.check_box_standard_search_str.setChecked(False)

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.MouseButtonDblClick:
            if event.button() == QtCore.Qt.LeftButton:
                self.open_file()
                return True
            elif event.button() == QtCore.Qt.RightButton:
                self.select_file()
                return True
            elif event.button() == QtCore.Qt.MidButton:
                self.show_text()
                return True
        return super().eventFilter(source, event)

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
            self.open_file()
        elif event.key() in [QtCore.Qt.Key_F4]:
            self.show_text()
        elif event.key() in [QtCore.Qt.Key_F5]:
            self.select_file()

    def show_text(self):
        if self.radio_button_list.isChecked() is True:
            try:
                select = self.listWidget.selectedIndexes()[0].data()
                path = re.search(r"Файл : (.+)\n", select).group(1).strip()
                text = self.result_search.get(path)
                if text is None:
                    return
                text = '\n'.join(text)
            except IndexError or AttributeError:
                return
            self.widget_error = ShowError(text=text,
                                          title='Вывод результата')
            self.widget_error.show()
            return

    def open_file(self):
        """
        Открывает выбраный файл в notepad.exe для Windows
        Или через xdg-open для Linux
        """
        if self.radio_button_list.isChecked() is True:
            try:
                select = self.listWidget.selectedIndexes()[0].data()
                path = re.search(r"Файл : (.+)\n", select).group(1).strip()
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
        elif self.radio_button_tree.isChecked() is True:
            try:
                select = self.treeWidget.selectedIndexes()[0].data()
                if os.path.isfile(select):
                    if sys.platform == 'linux':
                        subprocess.check_call(["xdg-open", "--", select])
                    elif sys.platform == 'win32':
                        subprocess.check_call(["notepad.exe", select])
            except OSError:
                self.widget_error = ShowError(text='Неудалось открыть выбранный файл',
                                              title='Ошибка открытия файла')
                self.widget_error.show()
                return

    def select_file(self):
        """
        Открыввает проводник и выделяет выбранный файл.
        Работает только на Windows
        """
        if self.radio_button_list.isChecked() is True:
            try:
                select = self.listWidget.selectedIndexes()[0].data()
                path = re.search(r"Файл : (.+)\n", select).group(1).strip()
                path = path.replace('/', '\\')
            except IndexError:
                return
            try:
                if sys.platform == 'win32':
                    os.system(f'explorer /select, "{path}"')
            except OSError:
                self.widget_error = ShowError(text='Неудалось открыть выбранный файл',
                                              title='Ошибка открытия файла')
                self.widget_error.show()
                return
        elif self.radio_button_tree.isChecked() is True:
            try:
                select = self.treeWidget.selectedIndexes()[0].data()
                if os.path.isfile(select):
                    path = select.replace('/', '\\')
                    if sys.platform == 'win32':
                        os.system(f'explorer /select, "{path}"')
            except OSError:
                self.widget_error = ShowError(text='Неудалось открыть выбранный файл',
                                              title='Ошибка открытия файла')
                self.widget_error.show()
                return

    def radio_button_line_search_is_clicked(self):
        """Если  установлен построчный поиск включаем доступные варианты"""
        if self.radio_button_str_read.isChecked() is True:
            self.radio_button_st.setText("Поиск в начале строки")
            self.radio_button_st.setEnabled(True)
            self.radio_button_st.setChecked(False)

            self.radio_button_en.setText("Поиск в конце строки")
            self.radio_button_en.setEnabled(True)
            self.radio_button_en.setChecked(False)

            self.check_box_standard_search_str.setText("Показывать строку с искомым текстом")
            self.check_box_standard_search_str.setEnabled(True)
            if self.groupBox_27.isChecked() is False:
                self.groupBox_27.setChecked(True)
                self.groupBox_27.setChecked(False)

    def radio_button_full_search_is_clicked(self):
        """Если поиск установлен на чтение файла целиком отключаем досутпные варианты"""
        if self.radio_button_full_read.isChecked() is True:
            self.radio_button_st.setText('Поиск в начале строки '
                                                 '(Настройка не доступна при "Чтение файла целиком")')
            self.radio_button_st.setEnabled(False)
            self.radio_button_st.setChecked(False)

            self.radio_button_en.setText('Поиск в конце строки '
                                                 '(Настройка не доступна при "Чтение файла целиком")')
            self.radio_button_en.setEnabled(False)
            self.radio_button_en.setChecked(False)

            self.check_box_standard_search_str.setText('Показывать строку с искомым текстом '
                                                      '(Настройка не доступна при "Чтение файла целиком")')
            self.check_box_standard_search_str.setEnabled(False)
            self.check_box_standard_search_str.setChecked(False)

    def directory_selection(self):
        """Функция выбора директории"""
        self.path = QFileDialog.getExistingDirectory(self, 'Directory selection')

    def group_box_setting_is_checked(self):
        """Скрытие или отображение stackedWidget"""
        if self.groupBox_setting.isChecked() is False:
            self.stackedWidget.hide()
        else:
            self.stackedWidget.show()

    def page_switching(self):
        """Переключение страниц stackedWidget"""
        if self.radio_button_standard_search.isChecked() is True:
            self.stackedWidget.setCurrentIndex(0)
        else:
            self.stackedWidget.setCurrentIndex(1)

    def collection_of_data_for_standard_search(self):
        """
        Функция валидации при старте стандартного поиска.
        Проверяет что строка поиска болье 3.
        Выбрана директория поиска.
        Поиск по дате модификации файла.
        Поиск с учетом имени файла.
        Типы файлов которые ищем.
        Тип чтения файла.
        """
        search_text = self.line_edit_search.text()
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
        if self.check_box_date_modification.isChecked() is True:
            if self.dateEdit_7.date() > self.current_date.currentDate():
                self.widget_error = ShowError(text='Дата модификации файла не может быть больше текущей!',
                                              title='Ошибка валидации')
                self.widget_error.show()
                return
            else:
                file_search_setting.update({"date": self.dateEdit_7.text()})
        else:
            file_search_setting.update({"date": False})
        if self.check_box_recursion.isChecked() is True:
            file_search_setting.update({"recursion": True})
        else:
            file_search_setting.update({"recursion": False})
        # Добавляем файлы для проверки
        if self.check_box_file_name.isChecked() is True:
            in_file_name = self.line_edit_file_name.text()
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
        if self.check_box_txt.isChecked() is True:
            file_types.append(self.check_box_txt.text().replace('.', ''))
        if self.check_box_log.isChecked() is True:
            file_types.append(self.check_box_log.text().replace('.', ''))
        if self.check_box_xml.isChecked() is True:
            file_types.append(self.check_box_xml.text().replace('.', ''))
        if self.check_box_json.isChecked() is True:
            file_types.append(self.check_box_json.text().replace('.', ''))
        str_file_types = self.line_edit_files_format.text()
        if str_file_types != '':
            file_types_list = str_file_types.split(',')
            for types in file_types_list:
                file_types.append(types.strip())
        if file_types == []:
            self.widget_error = ShowError(text='Необходимо указать хотя бы одно расшерение файла!',
                                          title='Ошибка валидации')
            self.widget_error.show()
            return
        else:
            file_search_setting.update({"file_types": file_types})
        if self.radio_button_str_read.isChecked() is True:
            file_search_setting.update({"entirely_read": True})
        else:
            file_search_setting.update({"entirely_read": False})
        file_search_setting.update({"search_text": search_text})
        return file_search_setting

    def collection_of_data_for_xml_or_json_search(self):
        """
        Функция валидации при старте поиска XML или JSON.
        Проверяет что строка поиска болье 3.
        Выбрана директория поиска.
        Поиск по дате модификации файла.
        Поиск с учетом имени файла.
        Типы файлов которые ищем.
        Тип чтения файла.
        """
        search_text = self.line_edit_search.text()
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
        if self.check_box_date_modification.isChecked() is True:
            if self.dateEdit_8.date() > self.current_date.currentDate():
                self.widget_error = ShowError(text='Дата модификации файла не может быть больше текущей!',
                                              title='Ошибка валидации')
                self.widget_error.show()
                return
            else:
                file_search_setting.update({"date": self.dateEdit_8.text()})
        else:
            file_search_setting.update({"date": False})
        if self.check_box_recursion.isChecked() is True:
            file_search_setting.update({"recursion": True})
        else:
            file_search_setting.update({"recursion": False})
        # Добавляем файлы для проверки
        if self.check_box_file_name.isChecked() is True:
            in_file_name = self.line_edit_file_name.text()
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
        if self.radio_button_xml_search.isChecked() is True:
            file_types.append('xml')
        elif self.radio_button_json_search.isChecked() is True:
            file_types.append('json')

        if file_types == []:
            self.widget_error = ShowError(text='Необходимо указать хотя бы одно расшерение файла!',
                                          title='Ошибка валидации')
            self.widget_error.show()
            return
        else:
            file_search_setting.update({"file_types": file_types})
        if self.radio_button_tag_key.isChecked() is True:
            file_search_setting.update({"entirely_read": "KEY"})
        else:
            file_search_setting.update({"entirely_read": "VALUE"})
        file_search_setting.update({"search_text": search_text})
        return file_search_setting

    def standard_run(self):
        """Функция запуска стандартного поиска."""
        if file_search_setting := self.collection_of_data_for_standard_search():
            files = SearchForFileInTheDirectory(path=self.path, file_search_setting=file_search_setting).files
            if files == ():
                self.widget_error = ShowError(text='Не удалось найти нужные файлы',
                                              title='Ошибка поиска файлов')
                self.widget_error.show()
                return
            else:
                if self.radio_button_no_reg.isChecked() is True:
                    command = '1'
                if self.radio_button_reg.isChecked() is True:
                    command = '2'
                if self.radio_button_st.isChecked() is True:
                    command = '3'
                if self.radio_button_en.isChecked() is True:
                    command = '4'
                if self.radio_button_re.isChecked() is True:
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
        """Функция запуска поиска по JSON"""
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
        """Функция запуска поиска по XML"""
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
        """Функция запуска поиска которая запускает функцию поиска по типу"""
        self.progressBar.setValue(0)
        self.listWidget.clear()
        self.treeWidget.clear()
        self.push_button_serach.setEnabled(False)
        if self.radio_button_standard_search.isChecked() is True:
            self.standard_run()
        elif self.radio_button_xml_search.isChecked() is True:
            self.xml_run()
        elif self.radio_button_json_search.isChecked() is True:
            self.json_run()
        self.push_button_serach.setEnabled(True)

    def add_tree(self, data) -> None:
        if data == {'files_error': []}:
            self.widget_error = ShowError(text='Нет результатов в соотвествии с критериями поиска!',
                                          title='Результат выполнения')
            self.widget_error.show()
            return
        if self.radio_button_standard_search.isChecked() is True:
            self.result_search = {}
            for key, value in data.items():
                if key != 'files_error':
                    i = QtWidgets.QTreeWidgetItem(self.treeWidget, [key])
                    j = QtWidgets.QTreeWidgetItem(i, ['Кол-во повторений: {}'.format(value[0])])
                    if self.radio_button_str_read.isChecked() is True:
                        for x in range(len(value[1])):
                            QtWidgets.QTreeWidgetItem(j, [str(value[1][x])])
                    QtWidgets.QTreeWidgetItem(i, ['Дата модификации файла: {}'.format(
                        SearchForFileInTheDirectory.get_date_modification(key))])
        if self.radio_button_xml_search.isChecked() is True or self.radio_button_json_search.isChecked() is True:
            for key, value in data.items():
                if key != 'files_error':
                    i = QtWidgets.QTreeWidgetItem(self.treeWidget, [key])
                    QtWidgets.QTreeWidgetItem(i, ['Кол-во повторений: {}'.format(value)])
                    QtWidgets.QTreeWidgetItem(i, ['Дата модификации файла: {}'.format(
                        SearchForFileInTheDirectory.get_date_modification(key))])

        if len(data.get("files_error")) > 0:
            i = QtWidgets.QTreeWidgetItem(self.treeWidget, ['Файлы которые неудалось прочитать:'])
            for j in data.get('files_error'):
                QtWidgets.QTreeWidgetItem(i, [j])

    def add_result_to_widget_list(self, data) -> None:
        if self.radio_button_tree.isChecked() is True:
            self.add_tree(data)
            return
        """Добавление полученного результата в ListWidget"""
        if data == {'files_error': []}:
            self.widget_error = ShowError(text='Нет результатов в соотвествии с критериями поиска!',
                                          title='Результат выполнения')
            self.widget_error.show()
            return
        if self.radio_button_standard_search.isChecked() is True:
            self.result_search = {}
            for key, value in data.items():
                if key != 'files_error':
                    lst = ["╔═══════════════════════════════════════════• ✤ •═══════════════════════════════════════════╗\n"]
                    if self.check_box_standard_path.isChecked() is True:
                        lst.append(" Файл : %s \n" % key)
                    if self.check_box_standard_count.isChecked() is True:
                        lst.append(" Кол-во повторений искомого текста : %s \n" % value[0])
                    if self.check_box_standard_search_str.isChecked() is True:
                        if value[0] > 1:
                            lst.append(f" Строка с искомым текстом : {value[1][0]} и еще "
                                       f"{len(value[1][1:-1])} вариантов.\n")
                        else:
                            lst.append(f" Строка с искомым текстом : {value[1][0]} \n")
                        self.result_search.update({key: value[1]})
                    if self.check_box_standard_display_modification_date.isChecked() is True:
                        lst.append(f" Дата модификаии файла : {SearchForFileInTheDirectory.get_date_modification(key)} \n")
                    lst.append("╚═════════════════════════════════════════════════════════════════════════════════════════╝")
                    item = QtWidgets.QListWidgetItem()
                    item.setText("".join(lst))
                    self.listWidget.addItem(item)
        if self.radio_button_xml_search.isChecked() is True or self.radio_button_json_search.isChecked() is True:
            for key, value in data.items():
                if key != 'files_error':
                    lst = [
                        "╔═══════════════════════════════════════════• ✤ •═══════════════════════════════════════════╗\n"]
                    if self.chec_box_path.isChecked() is True:
                        lst.append(f" Файл : {key}\n")
                    if self.check_box_count.isChecked() is True:
                        lst.append(f" Кол-во повторений искомого текста : {value}\n")
                    if self.check_box_display_modification_date.isChecked() is True:
                        lst.append(
                            f" Дата модификаии файла : {SearchForFileInTheDirectory.get_date_modification(key)} \n")
                    lst.append(
                        "╚═════════════════════════════════════════════════════════════════════════════════════════╝")
                    self.listWidget.addItem("".join(lst))
        if len(data.get("files_error")) > 0:
            self.listWidget.addItem(
                f"╔═══════════════════════════════════════════• ✤ •═══════════════════════════════════════════╗\n"
                f" Неудалось прочесть следующие файлы: {data.get('files_error')}\n"
                f"╚═════════════════════════════════════════════════════════════════════════════════════════╝"
            )