from src.operations import put, get, copy
from enum import Enum


class YamlContractEnum(Enum):
    OPERATION_TYPE = "operation_type"
    COPY = "copy"
    PUT = "put"
    GET = "get"


DICT_OPERATION_TYPE_TO_CALLABLE = {
    YamlContractEnum.COPY.value: copy.CopyToSnowflake,
    YamlContractEnum.PUT.value: put.PutToSnowflake,
    YamlContractEnum.GET.value: get.GetFromSnowflake,
}
