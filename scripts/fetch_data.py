import duckdb
import pandas as pd

if __name__ == "__main__":
    conn = duckdb.connect("dev.duckdb")
    conn.execute("CREATE TABLE sales AS SELECT * FROM 'data/AMZ_SALES.csv'")
    conn.close()
