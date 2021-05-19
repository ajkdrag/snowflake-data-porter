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

    parser.add_argument(
        "--wrk_dir",
        action="store",
        help="working directory",
        required=True,
        type=str,
    )

    args = parser.parse_args()
    pipeline_manager = PipelineManager(config_path=args.config, wrk_dir=args.wrk_dir)
    pipeline_manager.setup()
    pipeline_manager.buildPipeline()
    pipeline_manager.triggerPipeline()
    pipeline_manager.writeResults()


if __name__ == "__main__":
    log.info("======== Started Execution ===========")
    main()
