import os
import mysql.connector

#this is all a test
#build a new data base 

testdata = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
        )



db = testdata.cursor()
#bild a new database named plants
db.execute("CREATE DATABASE IF NOT EXISTS plants")


#connect to database and make a new table (Tring to find a better way of doing this)
setdata = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="plants"
        )
table = setdata.cursor()

table.execute("CREATE TABLE IF NOT EXISTS pointpl (id VARCHAR(30) NOT NULL, fileName VARCHAR(255))")

#pull data from data store 
#data store might be faster to just preload all locations and pull as need and not use data base?
#os.system('mkdir clouddata')

fp = open("eastplants","r")

test = fp.readline().rstrip()
test = fp.readline().rstrip()
print("this is plant one location")
print(test)
#for i in range(10):
test = test.replace("C- ","")
print(test)
#print('iget -N 0 -PVT' + test)
#just to test getting one file from datastore (will fix harded code file path)
os.system('iget -N 0 -PVT' + test+"/2020-03-02__01-12-17-360_cropped.ply")    


for x in db:
    print(x)


