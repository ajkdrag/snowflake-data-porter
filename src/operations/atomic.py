import string

from src.utils.exceptions import LoadUnloadStageException
from src.operations import BaseOperation
from src.io.file_io import get_all_data_from_yaml, yield_all_files
from src.io import snowflake_io
from src.utils.constants import YamlContractEnum
from src import log


class LoadUnloadStage(BaseOperation):
    template_file = None
    source = None
    stage_type = None
    connection_config = None
    _use_schema_query = "use schema {database}.{schema};"

    def get_sub_operations(self, config):
        for attr, val in config.items():
            setattr(self, attr, val)
        return [self]

    def _format_query(self, query):
        field_names = [
            name for text, name, spec, conv in string.Formatter().parse(query) if name
        ]

        return query.format(
            **{field_name: getattr(self, field_name) for field_name in field_names}
        )

    def _parse_query_from_template(self, list_templates):
        query = None
        for template in list_templates:
            stage_type = template.get(YamlContractEnum.STAGE_TYPE.value)
            if stage_type == self.stage_type:
                query = template.get(YamlContractEnum.QUERY.value)
        if query is None:
            raise LoadUnloadStageException(
                f"No matching stage type for stage -> {stage_type}, found in template file -> {self.template_file}"
            )
        return query

    def run(self, context_manager):
        log.info(f"Running operation -> {self.name}")
        _connection = context_manager.get_or_create_connection(self.connection_config)
        _query = self._format_query(self._use_schema_query)
        snowflake_io.execute(_connection, _query)

        _list_templates = get_all_data_from_yaml(self.template_file)
        log.debug("Successfully read template file")

        _query = self._format_query(self._parse_query_from_template(_list_templates))
        _cursor = snowflake_io.execute(_connection, _query)
        _output = snowflake_io.fetch_one(_cursor)
        _output[YamlContractEnum.OPERATION_TYPE.value] = self.operation_type

        context_manager.add_operation_output(self.operation_type, _output)


class Copy(LoadUnloadStage):
    pass


class Get(LoadUnloadStage):
    pass


class Put(LoadUnloadStage):
    def run(self, context_manager):
        log.info(f"Running operation -> {self.name}")
        _connection = context_manager.get_or_create_connection(self.connection_config)
        _query = self._format_query(self._use_schema_query)
        snowflake_io.execute(_connection, _query)

        _list_templates = get_all_data_from_yaml(self.template_file)
        log.debug("Successfully read template file")

        file_or_directory_to_load_from = self.source
        for file_to_load in yield_all_files(file_or_directory_to_load_from):
            self.source = file_to_load
            _query = self._format_query(
                self._parse_query_from_template(_list_templates)
            )
            _cursor = snowflake_io.execute(_connection, _query)
            _output = snowflake_io.fetch_one(_cursor)
            _output[YamlContractEnum.OPERATION_NAME.value] = self.name

            context_manager.add_operation_output(self.operation_type, _output)
