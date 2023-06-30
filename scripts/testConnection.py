def main():
    from readData import readData
    qrypath = "SQL/geometriesBuurten.sql"
    return readData(qrypath, geodata=False)

if __name__ == "__main__":
    main()