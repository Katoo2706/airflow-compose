# dags/config/constants.py

class Constants:
    """
    Constants used throughout the project.
    """

    # Path to the dbt project directory
    DBT_PROJECT_DIR = "/opt/airflow/dbt_psql"

    # Other constants can be added here as needed
    # DBT_TARGET = "dev"
    # DBT_PROFILES_DIR = "/opt/airflow/dbt_profiles"


class DbtCommandTypes:
    """
    Enum-like class for DBT command types.
    """
    RUN = "run"
    TEST = "test"
    SEED = "seed"
    DOCS_GENERATE = "docs generate"
    DEPS = "deps"
    SNAPSHOT = "snapshot"
    LIST = "list"
    ALL_COMMANDS = [
        RUN,
        TEST,
        SEED,
        DOCS_GENERATE,
        DEPS,
        SNAPSHOT,
        LIST
    ]
