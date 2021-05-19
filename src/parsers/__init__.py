from src.io.file_io import get_all_data_from_yaml


class BaseConfigParser:
    def get_all_data_from_yaml(self, path):
        return get_all_data_from_yaml(path)
