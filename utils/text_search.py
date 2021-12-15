import re


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
        return text.upper().count(self.search_text.upper())

    def _case_insensitive_search(self, text: str) -> int:
        """
        Поиск с учетом регистра, так же используеться при поиске регулярным выражением
        """
        return text.count(self.search_text)

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

    def _line_search(self, file, method) -> tuple:
        count_result = 0
        lines = []
        for line in file.readlines():
            result_search = method(line)
            if result_search:
                count_result += result_search
                lines.append(line.strip())
        return count_result, lines

    def start_search(self) -> None:
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
                        count_result, lines = self._line_search(file, method)
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