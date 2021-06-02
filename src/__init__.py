from src.io.file_io import get_abs_path
from src.parsers.global_config_parser import GlobalConfigParser
from src.logger import get_logger, init_default_handler


_global_config_abs_path = get_abs_path(
    rel_path="configs/globals.cfg.yaml", caller_script_directory=__file__
)


base_config = GlobalConfigParser().parse(_global_config_abs_path)

_log_level = base_config.get("log_level", "DEBUG")
log = get_logger(__name__, log_level=_log_level)
init_default_handler(log, log_level=_log_level)

log.info("Logging set up successfully")
