"""
Shared settings for the 3-step pipeline:
    01_data_cleaning.ipynb -> 02_sql_analysis.ipynb -> 03_eda.ipynb
Every notebook imports this file, so paths / DB settings live in ONE place.
"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# ---- input -------------------------------------------------------------
RAW_CSV = BASE_DIR / "indian_ecommerce_customer_behavior.csv"

# ---- files passed from one notebook to the next -----------------------
OUTPUT_DIR = BASE_DIR / "output"
SQL_OUT_DIR = OUTPUT_DIR / "sql_results"
CLEAN_CSV = OUTPUT_DIR / "customer_behavior_clean.csv"      # 01 -> 02, 03
TREATED_CSV = OUTPUT_DIR / "customer_behavior_treated.csv"  # 01 -> 03 (outliers capped + log cols)
QUERIES_SQL = BASE_DIR / "queries.sql"                      # used by 02

OUTPUT_DIR.mkdir(exist_ok=True)
SQL_OUT_DIR.mkdir(exist_ok=True)

# ---- database ----------------------------------------------------------
# "mysql"  -> your MySQL server (needs: pip install sqlalchemy pymysql)
# "sqlite" -> local file, no server needed (handy for quick testing)
DB_BACKEND = os.getenv("DB_BACKEND", "mysql")
MYSQL_URL = os.getenv("MYSQL_URL", "mysql+pymysql://root:12345@localhost:3305/ecommerce_db")
SQLITE_PATH = OUTPUT_DIR / "ecommerce.db"
TABLE_NAME = "customer_behavior"


def get_connection():
    """Return a connection/engine that pandas.read_sql / to_sql can use."""
    if DB_BACKEND == "sqlite":
        import sqlite3
        return sqlite3.connect(SQLITE_PATH)
    from sqlalchemy import create_engine
    return create_engine(MYSQL_URL)


def require(path, step):
    """Stop with a clear message if an earlier notebook has not been run yet."""
    if not Path(path).exists():
        raise FileNotFoundError(f"{path} not found. Run {step} first.")
