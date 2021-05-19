from src import log


class Pipeline:
    def __init__(self, list_operations=None, context_manager=None) -> None:
        self.list_operations = list_operations
        if self.list_operations is None:
            self.list_operations = []
        self.context_manager = context_manager

    def addAll(self, list_operations):
        self.list_operations = list_operations

    def run(self):
        for operation in self.list_operations:
            operation.run(context_manager=self.context_manager)
