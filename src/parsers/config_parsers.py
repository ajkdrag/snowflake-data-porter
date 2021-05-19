from os import getenv
from src.io.file_io import get_all_data_from_yaml


class SnowflakeConfigParser:
    @staticmethod
    def parse(path_to_snowflake_config):
        return get_all_data_from_yaml(path_to_snowflake_config)



class GlobalConfigParser:
    @staticmethod
    def parse(path_to_global_config):
        _global_config = get_all_data_from_yaml(path_to_global_config)
        base_config = _global_config.get("dev")
        # update overrides for the current environment
        base_config.update(_global_config.get(getenv("ENVIRONMENT", "dev")))
        return base_config
