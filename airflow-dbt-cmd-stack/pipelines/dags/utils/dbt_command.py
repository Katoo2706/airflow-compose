# dags/utils/dbt_command.py

import subprocess

from config.constants import Constants


def run_dbt(command, dbt_project_dir=Constants.DBT_PROJECT_DIR):
    dbt_command = f"cd {dbt_project_dir} && {command}"
    result = subprocess.run(dbt_command, shell=True, capture_output=True, text=True)

    print(result.stdout)
    if result.returncode == 0:
        print("DBT process executed successfully")
    if result.returncode != 0:
        raise ValueError(f"DBT process failed with return code: {result.returncode}")
