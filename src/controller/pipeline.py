from src import log


class Pipeline:
    def __init__(self) -> None:
        self.list_operations = []

    def addAll(self, list_operations):
        self.list_operations = list_operations

    def run(self):
        log.debug(self.list_operations)
