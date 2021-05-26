from src import log
from src.parsers import BaseConfigParser
from src.utils.constants import YamlContractEnum, get_operations_from_types


class DataPorterConfigParser(BaseConfigParser):
    def parse(self, path_to_data_porter_config):
        _data_porter_config = self.get_all_data_from_yaml(path_to_data_porter_config)
        list_operations = []
        for operation_config in _data_porter_config:
            _operation_type = operation_config.get(
                YamlContractEnum.OPERATION_TYPE.value
            )
            operation = get_operations_from_types([_operation_type])[0]
            list_sub_operations = operation.get_sub_operations(operation_config)
            list_operations.extend(list_sub_operations)
        return list_operations
