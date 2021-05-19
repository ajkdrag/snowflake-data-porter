from src import log


def main():
    from src.parsers.config_parsers import SnowflakeConfigParser
    from src.io import snowflake_io

    test_path = "/media/ajkdrag/Overdrive/vs_workspace/projects/SnowflakeDataPorter/src/configs/snowflake_conn.cfg.yaml"
    snowflake_params = SnowflakeConfigParser.parse(test_path)
    log.debug(snowflake_params)

    connection_obj = snowflake_io.create_new_connection(snowflake_params)
    cursor = snowflake_io.execute(connection_obj, "select current_date();");
    log.info(cursor.fetchone())

if __name__ == "__main__":
    log.info("Testing snowflake connection")
    main()
