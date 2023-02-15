import os
import os.path
import csv
import mysql.connector
from mysql.connector import errorcode
import sys
from datetime import datetime

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
print(refdate)
config.popitem()
for key in config.keys():
    print(config[key])
    
    #Setup-Datei lesen
setup_file=open(setup, "r")
setup_dict=dict(line.strip().split(":") for line in setup_file)
for key in setup_dict.keys():
    csv_file=open(r"csv\\"+setup_dict[key], "r")
    csv=list(line.strip().split(";") for line in csv_file)
    print(csv[0])

    #Datenbankverbindung
connection = mysql.connector.connect(**config) 

#es gibt ein Problem mit unserer mysql version, 
#wir kommen bis zur datenbank, werden aber am PW abgewiesen, obwohl es in workbench einwandfrei funktioniert    