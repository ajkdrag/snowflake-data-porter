from os import getenv
from src.parsers import BaseConfigParser


class GlobalConfigParser(BaseConfigParser):
    def parse(self, path_to_global_config):
        _global_config = self.get_all_data_from_yaml(path_to_global_config)
        base_config = _global_config.get("dev")
        # update overrides for the current environment
        base_config.update(_global_config.get(getenv("ENVIRONMENT", "dev")))
        return base_config
