from src.utils.constants import YamlContractEnum
from src.operations import BaseOperation
from src.io.file_io import get_all_data_from_yaml
from src.io import snowflake_io
from src import log


class GetFromSnowflake(BaseOperation):
    source = None
    template_file = None
    target = None
    stage_type = None
    database = None
    schema = None
    connection_config = None

    def _parse_query_from_template(self):
        list_templates = get_all_data_from_yaml(self.template_file)
        query = None
        for template in list_templates:
            stage_type = template.get(YamlContractEnum.STAGE_TYPE.value)
            if stage_type == self.stage_type:
                query = template.get(YamlContractEnum.QUERY.value)
        return query

    def _format_query(self, query):
        return query.format(self.source, self.target)

    def run(self, context_manager):
        log.info(f"Running operation -> {self.name}")
        _connection = context_manager.get_or_create_connection(self.connection_config)
        snowflake_io.execute(_connection, f"use schema {self.database}.{self.schema};")
        _query = self._format_query(self._parse_query_from_template())
        _cursor = snowflake_io.execute(_connection, _query)
        _output = snowflake_io.fetch_one(_cursor)
        context_manager.add_operation_output(self.operation_type, _output)
