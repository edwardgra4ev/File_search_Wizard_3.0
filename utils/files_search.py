import os
import re
import datetime


class SearchForFileInTheDirectory(object):
    """Класс который ищетнужные файлы в указанной дирректории"""
    def __init__(self, path, file_search_setting: dict = None):
        self.path = path
        self.file_search_setting = file_search_setting
        self.files = self.create_files_tuple()

    def _getting_file_path(self) -> tuple:
        """Получаем все файлы в нужной дерриктории"""
        try:
            file_list = os.listdir(self.path)
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
                    file_modification_date = datetime.datetime.fromtimestamp(os.path.getmtime(file))
                    files_and_modification_date.update({file: str(file_modification_date)})
                else:
                    for fl in self.file_search_setting.get("file_name"):
                        if fl in file.split('\\')[-1]:
                            file_modification_date = datetime.datetime.fromtimestamp(os.path.getmtime(file))
                            files_and_modification_date.update({file: str(file_modification_date)})
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

    @staticmethod
    def get_date_modification(file_patch) -> datetime:
        """Функция получения даты модификации файла"""
        return datetime.datetime.fromtimestamp(os.path.getmtime(file_patch))