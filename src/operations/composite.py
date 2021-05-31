from src.operations import BaseOperation
from src.utils.constants import YamlContractEnum, get_operations_from_types


class Composite(BaseOperation):
    def get_sub_operations(self, config):
        sub_operation_types = config.get(YamlContractEnum.OPERATION_TYPE.value).split(
            "_"
        )
        num_sub_operations = len(sub_operation_types)
        sub_operations = get_operations_from_types(sub_operation_types)
        list_sub_operation_configs = [
            {YamlContractEnum.OPERATION_TYPE.value: sub_operation_types[i]}
            for i in range(num_sub_operations)
        ]
        for attr, val in config.items():
            attr_tokens = attr.rsplit("_", 1)
            if attr_tokens[-1].isnumeric():
                list_sub_operation_configs[int(attr_tokens[-1]) - 1].setdefault(
                    attr_tokens[0], val
                )
            else:
                for dict_ in list_sub_operation_configs:
                    dict_.setdefault(attr, val)

        Composite._chain_source_and_target(
            num_sub_operations, list_sub_operation_configs
        )

        sub_operations = [
            sub_operation.get_sub_operations(config)[0]
            for sub_operation, config in zip(sub_operations, list_sub_operation_configs)
        ]
        return sub_operations

    @staticmethod
    def _chain_source_and_target(num_sub_operations, list_sub_operation_configs):
        for index in range(num_sub_operations):
            curr_config = list_sub_operation_configs[index]
            if index < num_sub_operations - 1:
                next_config = list_sub_operation_configs[index + 1]
                curr_config.setdefault(
                    YamlContractEnum.TARGET.value,
                    next_config.get(YamlContractEnum.SOURCE.value, None),
                )
            if index > 0:
                prev_config = list_sub_operation_configs[index - 1]
                curr_config.setdefault(
                    YamlContractEnum.SOURCE.value,
                    prev_config.get(YamlContractEnum.TARGET.value, None),
                )
