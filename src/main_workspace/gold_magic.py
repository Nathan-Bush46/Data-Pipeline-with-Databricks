from pyspark.sql import SparkSession


def gold_data(database, table_name):
    """
    Load data and make new data with mean.

    Args:
        database (str): Databricks database.
        table_name (str): Name of the table to load.

    Returns:
        None
    """
    # Initialize SparkSession
    spark = SparkSession.builder.getOrCreate()

    # Check if the table exists
    if not spark.catalog.tableExists(f"{database}.{table_name}"):
        print(
            f"Error: Table {database}.{table_name} does not exist. "
            "Please verify the table name and database."
        )
        return

    # Construct and execute the query to display the table data
    query = f"SELECT *, AVG(USD) OVER() AS mean_usd FROM `{database}`.`{table_name}`"
    print(f"Executing query: {query}")

    # Display the data
    # display(spark.sql(query))

    # Additional data insights
    print("\nTable Schema:")
    spark.sql(query).printSchema()

    print("\nData Summary:")
    spark.sql(query).describe().show()
    # Create a new table with the mean column
    new_table_name = f"{table_name}_with_mean"
    spark.sql(f"CREATE TABLE IF NOT EXISTS {database}.{new_table_name} AS {query}")
    print(f"New table {database}.{new_table_name} created successfully.")


if __name__ == "__main__":
    # Define database and table names
    database_name = "nathan_db"
    table_name1 = "gold"

    # Execute the load function
    gold_data(database_name, table_name1)
