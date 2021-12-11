import configparser
import datetime


class Parser:
    def __init__(self):
        self.config_file = "./config.ini"
        self.config = configparser.ConfigParser()
        self.config.read(self.config_file)

    def get_version(self) -> str:
        return self.config["Version"]["current_version"]

    def get_all_themes(self) -> list:
        lst = self.config["Themes"]["all_theme"].split(',')
        return [x.strip() for x in lst]

    def get_current_theme(self) -> str:
        return self.config["Themes"]["current_theme"]

    def get_url_update(self) -> str:
        return self.config["Update"]["url"]

    def get_last_update_time(self) -> datetime or None:
        last_update_time = self.config["Update"]["last_check_time"]
        if last_update_time != '':
            return datetime.datetime.strptime(last_update_time, '%Y-%m-%d %H:%M:%S.%f')

    def get_time_limit(self) -> int:
        return int(self.config["Update"]["time_limit_in_seconds"])

    def save_last_update_time(self) -> None:
        last_update_time = datetime.datetime.now()
        self.config.set("Update", "last_check_time", str(last_update_time))
        self.save_config()

    def save_time_limit(self, limit):
        self.config.set("Update", "time_limit_in_seconds", str(limit))
        self.save_config()

    def save_current_theme(self, theme) -> None:
        self.config.set("Themes", "current_theme", str(theme))
        self.save_config()

    def save_config(self):
        with open(self.config_file, "wb+") as config_file:
            self.config.write(config_file)

