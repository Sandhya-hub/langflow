 api-key     Creates an API key for the default superuser if AUTO_LOGIN is enabled.                     │
│ copy-db     Copy the database files to the current directory.                                          │
│ migration   Run or test migrations.                                                                    │
│ run         Run Langflow.                                                                              │
│ superuser   Create a superuser. 


python -m venv langflow_env
source langflow_env/bin/activate  # On Windows use `langflow_env\Scripts\activate`


pip install langflow

mkdir langflow
mkdir tests