import os
import os.path
import csv
import mysql.connector
from mysql.connector import errorcode
import sys
from datetime import datetime

setup="Setups\\"
setup+=sys.argv[1]
date=sys.argv[2]

    #config auslesen
config_file=open("Konfiguartion.txt","r")
    #zeile für zeile einlesen, am "=" trennen, in dictonary speichern
config=dict(line.strip().split("=") for line in config_file)
for key in config.keys():
    print(config[key])

    #Datenbankverbindung
#connection = mysql.connector.connect(**config)

    #Setup-Datei lesen
setup_file=open(setup, "r")
setup_dict=dict(line.strip().split(":") for line in setup_file)
for key in setup_dict.keys():
    csv_file=open(r"csv\\"+setup_dict[key], "r")
    csv=list(line.strip().split(";") for line in csv_file)
    print(csv[0])