import configparser
from config.constants import config_sections


class config_operations:
    config = configparser.RawConfigParser()
    config.read(filenames="config/config.ini")

    def get_current_environment(self) -> str:
        return self.config.get(config_sections.COMMON, "environment")

    def get_project_name(self) -> str:
        return self.config.get(config_sections.COMMON, "project_name")

    def get_base_url(self) -> str:
        return self.config.get(
            config_sections.BASE_URLS, self.get_current_environment()
        )
