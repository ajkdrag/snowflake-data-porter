from src.parsers.data_porter_config_parser import DataPorterConfigParser
from src.controller.pipeline import Pipeline


class PipelineManager:
    def __init__(self, config_path) -> None:
        self.config_path = config_path
        self.list_operations = None
        self.Pipeline = None

    def parse_config(self):
        self.list_operations = DataPorterConfigParser().parse(self.config_path)

    def buildPipeline(self):
        self.Pipeline = Pipeline()
        self.Pipeline.addAll(self.list_operations)

    def triggerPipeline(self):
        self.Pipeline.run()
