import snowflake.connector as connector
from src import log


def create_new_connection(connection_params):
    return connector.connect(
        user=connection_params["user"],
        account=connection_params["account"],
        password=connection_params["password"],
        warehouse=connection_params["warehouse"],
        authenticator=connection_params["authenticator"],
    )


def execute(connection_obj, query):
    cursor = connection_obj.cursor()
    log.info(f"Query -> {query}")
    cursor.execute(query)
    return cursor

def fetch_one(cursor):
    columns = cursor.description
    output = cursor.fetchone()
    return {column[0]: row for column,row in zip(columns, output)}


def close(connection_obj):
    connection_obj.close()
