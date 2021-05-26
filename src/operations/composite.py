from src.operations import BaseOperation
from src.utils.constants import YamlContractEnum, get_operations_from_types


class LoadUnloadTable(BaseOperation):
    def get_sub_operations(self, config):
        sub_operation_types = config.get(YamlContractEnum.OPERATION_TYPE.value).split(
            "_"
        )
        sub_operations = get_operations_from_types(sub_operation_types)
        list_operation_configs = [
            {YamlContractEnum.OPERATION_TYPE.value: sub_operation_types[i]}
            for i in range(len(sub_operation_types))
        ]
        for attr, val in config.items():
            attr_tokens = attr.rsplit("_", 1)
            if attr_tokens[-1].isnumeric():
                list_operation_configs[int(attr_tokens[-1]) - 1].setdefault(
                    attr_tokens[0], val
                )
            else:
                for dict_ in list_operation_configs:
                    dict_.setdefault(attr, val)

        for index in range(len(sub_operation_types)):
            curr_config = list_operation_configs[index]
            if index < len(sub_operation_types) - 1:
                next_config = list_operation_configs[index + 1]
                curr_config.setdefault(
                    YamlContractEnum.TARGET.value,
                    next_config.get(YamlContractEnum.SOURCE.value, None),
                )
            if index > 0:
                prev_config = list_operation_configs[index - 1]
                curr_config.setdefault(
                    YamlContractEnum.SOURCE.value,
                    prev_config.get(YamlContractEnum.TARGET.value, None),
                )
            sub_operations[index] = sub_operations[index].get_sub_operations(
                curr_config
            )[0]
        return sub_operations


class PutCopy(LoadUnloadTable):
    pass
