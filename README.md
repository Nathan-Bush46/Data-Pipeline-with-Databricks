# IDS-databricks 

[![Docker Image CI](https://github.com/Nathan-Bush46/Data-Pipeline-with-Databricks/actions/workflows/docker-image.yml/badge.svg)](https://github.com/Nathan-Bush46/Data-Pipeline-with-Databricks/actions/workflows/docker-image.yml)


#  Databricks Job Execution

Link to the default job on Databricks (Simple ETL): https://dbc-c95fb6bf-a65d.cloud.databricks.com/jobs/57070255739871?o=3670519680858392

## Overview
The `main.py` script orchestrates the execution of Databricks jobs for data processing, cleaning, visualization, and reporting. Each job is executed sequentially, and the results are stored in the Databricks environment.

Additionally, `test_main.py` is provided for testing the functionality of `main.py`, including API interactions and table creation.

* Python files that create, query, and test a databricks workflow
    * [`create table`](src/main_workspace/extract.py): Creates a basic table from data found ['here'](https://raw.githubusercontent.com/MainakRepositor/Datasets/refs/heads/master/Gold%20Rates/annual_gold_rate.csv)
        * Shows use of some SQL queries
    * [`load`](src/main_workspace/load.py): prints a table from the table. To test and show the table is there.
    * [`gold`](src/main_workspace/gold_magic.py): creates a new table with the mean gold price in USD
    * [`test_main`](src/tests/test_main.py): Does a testing using Python. This tests that the operations on a database behave as expected. 
---

## How to Use `main.py`

### Prerequisites
1. **Databricks Environment**: Ensure you have access to a Databricks workspace. with an .env file
2. **Personal Access Token**: Generate a personal access token from Databricks.
3. **Job Configuration**: Update local `.env` script with the correct Databricks URL and Job IDs.
By default, you should have these in your .env file:

```{bash}
DATABRICKS_ACCESS_TOKEN = <Personal Access Token>
SERVER_HOST = dbc-c95fb6bf-a65d.cloud.databricks.com
HTTP_PATH = /sql/1.0/warehouses/2d6f41451e6394c0
JOB_ID = 914595435648149
```

### Steps to Run
1. **Run the Script**:
   Execute `main.py` from your terminal or Python environment:
   ```bash
   make run
   ```
2. **Monitor Jobs**:
   The script will start each job and monitor its progress until completion.
3. **Check Results**:
   After successful execution, the outputs (Delta tables, visualizations, and reports) will be available in your Databricks workspace.

---

## What the Jobs Do


## How to run tests

### Overview
The `test_main.py` 

1. **Install Dependencies**:
   - Ensure `pytest` and all other dependencies are installed:
     ```bash
     make install
     ```

2. **Environment Configuration**:
   Ensure that `.env` is correctly configured before running the tests.

### Running the Tests
1. Run the tests using `pytest`:
   ```bash
   pytest test_main.py
   # or 
   make test
   ```

## Set up instructions using VS code + Docker: 
### Docker
1. For Windows, Mac, and maybe Linux, you download Docker Desktop. links can be found [here](https://docs.docker.com/engine/install/). Follow set up instructions and start the application.

2. In vs code add Dev Containers and Docker extensions 

3. clone repo, restart vs code, and open repo in vs code.

4. should see a pop up to (re)open in devcontainer. Click it and let it run. It takes a bit of time for the first run but is much faster after that. Done.

#### Alternatives to Docker
If you choose not to run docker, use a python virtual environment to prevent conflict with local packages and run the makefile.
 

### makefile  
* install

* testing:

    tests all "\*test\*.py" files in src/test/ using py.test then tests all files using py.test --nbval-lax

* lint

* format

# run

* all 

## Things included are:

* [`Makefile`](Makefile)

* `Pylint` and `Ruff` for lintning

* `.devcontainer` with [`Dockerfile`](/.devcontainer/Dockerfile), [`postinstall.sh`](/.devcontainer/postinstall.sh), and [`devcontainer.json`](/.devcontainer/devcontainer.json)`

*  [`settings.json`](.vscode/settings.json) for testing

*  A base set of libraries in [`requirements.txt`](requirements.txt)




