import os
import csv
import mysql.connector
from mysql.connector import errorcode
import sys
from datetime import datetime

setup=sys.argv[1]
date=sys.argv[2]

    

config_file=open("Konfiguartion.txt","r")
con=dict(line.strip().split("=") for line in config_file)
#print(con["host"]
    #dict(line.strip().split("=") for line in config_file)
# 1. Datenbankverbindung
#connection = mysql.connector.connect(user=config["user"],
#                                     password=config["password"],
#                                     host=config["host"],
#                                     database=config["database"])
    # 3. Setup-Datei lesen
# with open(config["setup_file"], "r") as setup_file:
# setup = dict(line.strip().split("=") for line in setup_file)

    # 4. Dateipfade auf Existenz der Datei prüfen
#csv_file_path = setup["csv_file_path"]
#if not os.path.isfile(csv_file_path):
 #   print(f"Error: CSV file not found at path {csv_file_path}")

    # 5. CSV-Datei einlesen
csv_file=open(r"Setups\Teilnehmer.csv", "r")
csv=list(line.strip().split("/") for line in csv_file)
print(setup)
print(date)