from src.parsers.data_porter_config_parser import DataPorterConfigParser
from src.controller.pipeline import Pipeline
from src.controller.context_manager import ContextManager
from src.io.file_io import join, write_all_data_to_file, write_dataframe_to_file
from datetime import datetime


class PipelineManager:
    def __init__(self, config_path, wrk_dir) -> None:
        self.config_path = config_path
        self.wrk_dir = wrk_dir
        self.list_operations = None
        self.context_manager = None
        self.pipeline = None

    def setup(self):
        self.parse_config()
        self.buildContextManager()

    def buildContextManager(self):
        self.context_manager = ContextManager()
        self.context_manager.create_context()

    def parse_config(self):
        self.list_operations = DataPorterConfigParser().parse(self.config_path)

    def buildPipeline(self):
        self.pipeline = Pipeline(
            list_operations=self.list_operations, context_manager=self.context_manager
        )

    def triggerPipeline(self):
        self.pipeline.run()

    def writeResults(self):
        now = str(datetime.now().strftime("%Y%m%d_%H%M%S"))
        for (
            operation_type,
            result_df,
        ) in self.context_manager.yield_operation_outputs_as_dataframes():
            _output_file_name = f"{operation_type}_{now}.csv"
            _output_path = join(self.wrk_dir, operation_type, _output_file_name)
            write_dataframe_to_file(
                _output_path, result_df, mode="w+", create_parent_dirs=True
            )
