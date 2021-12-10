import os
import sys
import json
import requests


class Update:
    def __init__(self):
        self.URL_RELEASES_LATEST = "https://api.github.com/repos/edwardgra4ev/File_search_Wizard_3.0/releases/latest"
        self.current_version = None
        self.new_version = None
        self.name = None
        self.url = None
        self.body = None

    def _get_releases_latest_on_github(self) -> json or None:
        """Првоеряем последний релиз на GitHub"""
        r = requests.get(url=self.URL_RELEASES_LATEST)
        if r.status_code == 200:
            return r.json()

    def _version_comparison(self) -> bool:
        """Сравниваем текущую версию и новую"""
        current_version_lst = self.current_version.split('.')
        new_version_lst = self.new_version.split('.')
        if current_version_lst == new_version_lst:
            return False
        if int(current_version_lst[0]) > int(new_version_lst[0]):
            return False
        elif int(current_version_lst[1]) > int(new_version_lst[1]):
            return False
        elif int(current_version_lst[2]) > int(new_version_lst[2]):
            return False
        else:
            return True

    def _rename_file(self):
        os.rename(self.name, "File_search_Wizard_3.0_OLD_VERSION.exe")

    def _download_new_version(self, progress) -> bool or None:
        """Скачиваем новую версию"""
        with requests.get(self.url, stream=True) as r:
            r.raise_for_status()
            size_file = int(r.headers['Content-length'])
            progress.setMaximum(size_file)
            with open(self.name, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1048576):
                    f.write(chunk)
                    progress.setValue(progress.value() + sys.getsizeof(chunk))
                progress.setValue(size_file)
                return True

    def dell_file(self):
        os.remove('File_search_Wizard_3.0_OLD_VERSION.exe')

    def check_new_version(self, current_version: str):
        self.current_version = current_version
        json_obj = self._get_releases_latest_on_github()
        self.new_version = json_obj["tag_name"]
        self.name = json_obj["assets"][0]["name"]
        self.url = json_obj["assets"][0]["browser_download_url"]
        self.body = json_obj["body"]
        return self._version_comparison()