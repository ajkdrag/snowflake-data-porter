from os import getenv
from src.parsers import BaseConfigParser
from src.utils.exceptions import GlobalConfigParseException


class GlobalConfigParser(BaseConfigParser):
    def parse(self, path_to_global_config):
        try:
            _global_config = self.get_all_data_from_yaml(path_to_global_config)
            base_config = _global_config.get("dev")
            # update overrides for the current environment
            environment = getenv("ENVIRONMENT", "dev")
            if environment in _global_config:
                base_config.update(_global_config.get(environment))
            return base_config
        except OSError as err:
            raise GlobalConfigParseException from err