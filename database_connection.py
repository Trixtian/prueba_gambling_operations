from sqlalchemy import create_engine

def get_db_connection():
    # Asegúrate de que la cadena de conexión esté correctamente formateada
    connection_string = 'mysql+mysqlconnector://root:Tr1xt14n71@localhost:3306/gambling_operations'  
    engine = create_engine(connection_string)
    connection = engine.connect()
    return connection


