import argparse
from src import log
from src.controller.pipeline_manager import PipelineManager


def main():
    parser = argparse.ArgumentParser(
        description="Utility tool for moving data from local to snowflake tables and vice versa."
    )
    parser.add_argument(
        "--config",
        action="store",
        help="config file absolute path",
        required=True,
        type=str,
    )

    args = parser.parse_args()
    pipeline_manager = PipelineManager(config_path=args.config)
    pipeline_manager.parse_config()
    pipeline_manager.buildPipeline()
    pipeline_manager.triggerPipeline()


if __name__ == "__main__":
    log.info("Testing snowflake connection")
    main()
