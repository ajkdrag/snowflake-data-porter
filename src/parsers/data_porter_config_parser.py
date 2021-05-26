import importlib
from src import log
from src.parsers import BaseConfigParser
from src.utils.constants import YamlContractEnum, DICT_OPERATION_TYPE_TO_IMPORT


class DataPorterConfigParser(BaseConfigParser):
    def parse(self, path_to_data_porter_config):
        _data_porter_config = self.get_all_data_from_yaml(path_to_data_porter_config)
        list_operations = []
        for operation_config in _data_porter_config:
            _operation_type = operation_config.get(
                YamlContractEnum.OPERATION_TYPE.value
            )
            operation_to_import = DICT_OPERATION_TYPE_TO_IMPORT.get(_operation_type)
            module_, delimiter, class_ = operation_to_import.rpartition(".")
            operation = getattr(importlib.import_module(module_), class_)()
            list_sub_operations = operation.get_sub_operations(operation_config)
            list_operations.extend(list_sub_operations)
        return list_operations
