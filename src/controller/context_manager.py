from collections import defaultdict
from src.io.snowflake_io import create_new_connection
from src.io.file_io import get_all_data_from_yaml, get_dataframe_from_list
from src import log


class Context:
    dict_connections = {}
    dict_operation_outputs = defaultdict(list)


class ContextManager:
    def __init__(self) -> None:
        self.context = None

    def create_context(self):
        if self.context is None:
            self.context = Context()

    def get_or_create_connection(self, connection_path):
        if connection_path not in self.context.dict_connections:
            log.debug("Connection not cached. Creating a new connection")
            _connection_params = get_all_data_from_yaml(connection_path)
            _connection = create_new_connection(_connection_params)
            self.context.dict_connections[connection_path] = _connection
            log.debug("Successfully connected to snowflake")
        return self.context.dict_connections.get(connection_path)

    def add_operation_output(self, operation_type, operation_output):
        self.context.dict_operation_outputs[operation_type].append(operation_output)

    def yield_operation_outputs_as_dataframes(self):
        for operation_type, results in self.context.dict_operation_outputs.items():
            yield operation_type, get_dataframe_from_list(results)
