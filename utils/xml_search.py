import xml.etree.ElementTree as ET


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

    async def start_search(self) -> None:
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