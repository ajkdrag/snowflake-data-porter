from src.parsers import BaseConfigParser


class SnowflakeConfigParser(BaseConfigParser):
    def parse(self, path_to_snowflake_config):
        return self.get_all_data_from_yaml(path_to_snowflake_config)
