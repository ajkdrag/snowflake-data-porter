import importlib
from enum import Enum


class YamlContractEnum(Enum):
    SOURCE = "source"
    TARGET = "target"
    OPERATION_TYPE = "operation_type"
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
    YamlContractEnum.COMPOSITE.value: "src.operations.composite.LoadUnloadTable"
}


def get_operations_from_types(list_operation_types):
    sub_operations_import_attrs = [
        DICT_OPERATION_TYPE_TO_IMPORT.get(sub_op_type).rpartition(".")
        for sub_op_type in list_operation_types
    ]
    sub_operations = [
        getattr(importlib.import_module(module_), class_)()
        for module_, delimiter, class_ in sub_operations_import_attrs
    ]
    return sub_operations
