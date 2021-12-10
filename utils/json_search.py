import json


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

    async def start_search(self) -> None:
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