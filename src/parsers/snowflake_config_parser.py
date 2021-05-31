from src.utils.exceptions import SnowflakeConfigParseException
from src.parsers import BaseConfigParser


class SnowflakeConfigParser(BaseConfigParser):
    def parse(self, path_to_snowflake_config):
        try:
            return self.get_all_data_from_yaml(path_to_snowflake_config)
        except OSError as err:
            raise SnowflakeConfigParseException from err
