import importlib
from enum import Enum
from src.utils.exceptions import InvalidOperationException


class YamlContractEnum(Enum):
    SOURCE = "source"
    TARGET = "target"
    OPERATION_TYPE = "operation_type"
    OPERATION_NAME = "name"
    COPY = "copy"
    PUT = "put"
    GET = "get"
    STAGE_TYPE = "stage_type"
    QUERY = "query"
    COMPOSITE = "composite"


DICT_OPERATION_TYPE_TO_IMPORT = {
    YamlContractEnum.COPY.value: "src.operations.atomic.Copy",
    YamlContractEnum.PUT.value: "src.operations.atomic.Put",
    YamlContractEnum.GET.value: "src.operations.atomic.Get",
    YamlContractEnum.COMPOSITE.value: "src.operations.composite.Composite",
}

__LIST_ATOMIC_OPERATIONS = [
    YamlContractEnum.COPY.value,
    YamlContractEnum.PUT.value,
    YamlContractEnum.GET.value,
]


def get_operations_from_types(list_operation_types):
    try:
        sub_operations_import_attrs = [
            DICT_OPERATION_TYPE_TO_IMPORT.get(sub_op_type).rpartition(".")
            for sub_op_type in list_operation_types
        ]
    except KeyError as err:
        raise InvalidOperationException(
            f"Invalid Operation type passed : {err}. Valid base operation types -> {','.join(__LIST_ATOMIC_OPERATIONS)}"
        )
    sub_operations = [
        getattr(importlib.import_module(module_), class_)()
        for module_, delimiter, class_ in sub_operations_import_attrs
    ]
    return sub_operations
