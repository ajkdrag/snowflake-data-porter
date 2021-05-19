from enum import Enum


class YamlContractEnum(Enum):
    OPERATION_TYPE = "operation_type"
    COPY = "copy"
    PUT = "put"
    GET = "get"
    STAGE_TYPE = "stage_type"
    QUERY = "query"


DICT_OPERATION_TYPE_TO_IMPORT = {
    YamlContractEnum.COPY.value: "src.operations.copy.CopyToSnowflake",
    YamlContractEnum.PUT.value: "src.operations.put.PutToSnowflake",
    YamlContractEnum.GET.value: "src.operations.get.GetFromSnowflake",
}
