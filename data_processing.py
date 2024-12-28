import pandas as pd
from database_connection import get_db_connection

# Función para ejecutar consultas SQL y cargar los datos en un DataFrame
def run_query(query):
    connection = get_db_connection()
    return pd.read_sql(query, connection)

# Cargar datos de FTD
def load_ftd_data():
    from queries import FTD_QUERY
    return run_query(FTD_QUERY)

# Cargar datos de CPA
def load_cpa_data():
    from queries import CPA_QUERY
    return run_query(CPA_QUERY)
