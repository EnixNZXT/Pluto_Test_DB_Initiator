import os
import os.path
import csv
import mysql.connector
#from mysql.connector import errorcode
import sys
from datetime import datetime
    
    #speichern der übergabeparameter
setup="Setups\\"
setup+=sys.argv[1]
setup+=".txt"
date=sys.argv[2]
    
    #config auslesen
config_file=open("Konfiguartion.txt","r")
    
    #zeile für zeile einlesen, am "=" trennen, in dictonary speichern
config=dict(line.strip().split("=") for line in config_file)
    #das referenzdatum wird aus dem dictonary gelesen, 
    #in eine varibale gepeichert, dann entfernt um den rest des Dictonarys an die connection fkt zu übergeben
refdate=config["referenzdatum"]
config.popitem()
    #Datenbankverbindung
connection = mysql.connector.connect(**config) 
sql_cursor=connection.cursor() 
    #Setup-Datei lesen
setup_file=open(setup, "r")
setup_dict=dict(line.strip().split(":") for line in setup_file)
for key in setup_dict.keys():
    csv_file=open(r"csv\\"+setup_dict[key], "r")
    setupTables=str(setup_dict[key]).strip(".csv")
    setupTableList=list(setupTables.split(","))
    csv=dict(line.strip().split(":") for line in csv_file)
    TABLE=setup_dict[key].strip(".csv")
    TRUNCATE=f"TRUNCATE {TABLE}"
    sql_cursor.execute(TRUNCATE)
    connection.commit()
    
    for i in csv.keys():
        COLUMN=csv["0"].replace(";",", ")
        VALUES=csv[i].replace(";",", ")
        INSERT=f"INSERT INTO {TABLE} ({COLUMN}) VALUES ({VALUES})"
        sql_cursor.execute(INSERT)
        connection.commit() 
        