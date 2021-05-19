import os

from src.utils.io_utils import get_abs_path, get_all_data_from_yaml
from src.logger import get_logger, init_default_handler


_global_config_abs_path = get_abs_path(
    rel_path="configs/globals.cfg.yaml", caller_script_directory=__file__
)


_global_config_data = get_all_data_from_yaml(_global_config_abs_path)


base_config_data = _global_config_data.get("dev")
# update overrides for the current environment
base_config_data.update(_global_config_data.get(os.getenv("ENVIRONMENT", "dev")))


_log_level = base_config_data.get("log_level")
log = get_logger(__name__, log_level=_log_level)
init_default_handler(log, log_level=_log_level)
