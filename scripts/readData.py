def readData(query, geodata = True):
    import geopandas as gpd
    import pandas as pd
    import pyodbc
    
    server_name = "grandefinale.database.windows.net"
    user_name = "grandefinaleadmin"
    passwd = "Welkombijdegrandefinale!"

    # def sql_data(table, server_name, database_name, driver, ): 
    constr= (f"Server={server_name};Trusted_Connection=yes;UID={user_name};PWD={passwd}")
    conn = pyodbc.connect(constr)
    
    if geodata:
        data = gpd.read_postgis(query, conn, geom_col='geometry')
    else: 
        data = pd.read_sql(query, conn)
    conn.close()
    return data

