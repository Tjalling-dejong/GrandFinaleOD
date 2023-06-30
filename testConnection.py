def main():
    import readData
    qrypath = "SQL/Emissies.sql"
    return readData(qrypath, geodata=False)

if __name__ == "__main__":
    main()