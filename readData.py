def readData(queryfile, geodata = True, geom_col="geom"):
    import geopandas as gpd
    import pandas as pd
    import pyodbc
    
    server_name = "grandefinale.database.windows.net"
    db_name = "DWH_eMJV"
    user_name = "grandefinaleadmin"
    passwd = "Welkombijdegrandefinale!"

    # def sql_data(table, server_name, database_name, driver, ): 
    constr= (r"Driver={SQL Server};"
             f"Server={server_name};Database={db_name};UID={user_name};PWD={passwd}")
    conn = pyodbc.connect(constr)
    
    fd = open(queryfile, 'r')
    query = fd.read()
    fd.close()

    if geodata:
        data = gpd.read_postgis(query, conn, geom_col=geom_col)
    else: 
        data = pd.read_sql(query, conn)
    conn.close()
    return data

if __name__ == "__main__":
    df = readData("SQL/Emissies.sql", False)
    print(df.head())

    