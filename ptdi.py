import os
import csv
import psycopg2

def main():
    # 1. Datenbankverbindung
    conn = psycopg2.connect(
        host="localhost",
        database="database_name",
        user="user_name",
        password="password"
    )
    cur = conn.cursor()

    # 2. Konfigurationsdatei auslesen
    with open("config.cfg", "r") as config_file:
        config = dict(line.strip().split("=") for line in config_file)










    # 3. Setup-Datei lesen
    with open(config["setup_file"], "r") as setup_file:
        setup = dict(line.strip().split("=") for line in setup_file)

    # 4. Dateipfade auf Existenz der Datei prüfen
    csv_file_path = setup["csv_file_path"]
    if not os.path.isfile(csv_file_path):
        print(f"Error: CSV file not found at path {csv_file_path}")
        return

    # 5. CSV-Datei in Datenbank schreiben
    table_name = setup["table_name"]
    with open(csv_file_path, "r") as csv_file:
        reader = csv.reader(csv_file)
        headers = next(reader)
        headers_str = ", ".join(headers)
        headers_str = "(" + headers_str + ")"

        query = f"INSERT INTO {table_name} {headers_str} VALUES %s"
        cur.executemany(query, reader)
        conn.commit()

    print("Data imported successfully")

if name == "main":
    main()