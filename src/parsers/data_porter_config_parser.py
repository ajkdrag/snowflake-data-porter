from src import log
from src.parsers import BaseConfigParser
from src.utils.constants import YamlContractEnum, DICT_OPERATION_TYPE_TO_CALLABLE


class DataPorterConfigParser(BaseConfigParser):
    def parse(self, path_to_data_porter_config):
        _data_porter_config = self.get_all_data_from_yaml(path_to_data_porter_config)
        list_operations = []
        for operation_config in _data_porter_config:
            _operation_type = operation_config.get(YamlContractEnum.OPERATION_TYPE.value)
            operation = DICT_OPERATION_TYPE_TO_CALLABLE.get(_operation_type)()
            list_operations.append(operation)
        return list_operations
