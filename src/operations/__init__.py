import string
from src.io.file_io import get_all_data_from_yaml
from src.utils.constants import YamlContractEnum
from src.io import snowflake_io
from src import log


class BaseOperation:
    name = None
    operation_type = None


class PortViaStage(BaseOperation):
    template_file = None
    stage_type = None
    connection_config = None
    _use_schema_query = "use schema {database}.{schema};"

    def _format_query(self, query):
        field_names = [
            name for text, name, spec, conv in string.Formatter().parse(query) if name
        ]

        return query.format(
            **{field_name: getattr(self, field_name) for field_name in field_names}
        )

    def _parse_query_from_template(self):
        list_templates = get_all_data_from_yaml(self.template_file)
        query = None
        for template in list_templates:
            stage_type = template.get(YamlContractEnum.STAGE_TYPE.value)
            if stage_type == self.stage_type:
                query = template.get(YamlContractEnum.QUERY.value)
        return query

    def run(self, context_manager):
        log.info(f"Running operation -> {self.name}")
        _connection = context_manager.get_or_create_connection(self.connection_config)
        _query = self._format_query(self._use_schema_query)
        snowflake_io.execute(_connection, _query)
        _query = self._format_query(self._parse_query_from_template())
        _cursor = snowflake_io.execute(_connection, _query)
        _output = snowflake_io.fetch_one(_cursor)
        context_manager.add_operation_output(self.operation_type, _output)
