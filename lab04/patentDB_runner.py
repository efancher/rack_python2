#!/usr/bin/env python
#!*-* coding:utf-8 *-*

"""Some stuff

Usage: patentDB_runner.py --create
patentDB_runner.py --delete
patentDB_runner.py --load
patentDB_runner.py --find_by_author
"""

import MySQLdb
import getpass
import docopt
import csv

class PatentData(object):
    
    def __init__(self, last_name, first_name, patent_number, filing_date):
        self.last_name = last_name
        self.first_name = first_name
        self.patent_number = patent_number
        self.filing_data = filing_date

    def get_patent_dict():
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "patent_number": self.patent_number,
            "filing_date": self.filing_date}

class PatentDB(object):
    def __init__(self):
        self.lab_conn = MySQLdb.connect(host="104.130.144.149",
            user="python2.class",
            passwd=getpass.getpass(),
            db="python2_class_db") 
 
    def define_DB(self):
        create_table = """CREATE TABLE PatentData 
(
last_name VARCHAR(40),
first_name VARCHAR(40),
patent_number VARCHAR(40),
filing_date DATE
)"""    
         
        cursor = self.lab_conn.cursor()   
        #cursor.execute("DROP TABLE IF EXISTS PatentData")
        cursor.execute(create_table)

    def load_DB(self):
        insert_string = """
INSERT INTO PatentData (last_name, first_name, patent_number, filing_date)
VALUES
        ('{0}','{1}','{2}','{3}')
"""
        cursor = self.lab_conn.cursor()
        with open('patent_data.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            inserted_count = 0
            for row in reader:
                print(row)
                cursor.execute(insert_string.format(
                    row["last_name"],
                    row["first_name"],
                    row["patent_number"],
                    row["filing_date"]))
                inserted_count = inserted_count + cursor.rowcount
            self.lab_conn.commit()
            print("inserted {0} rows".format(inserted_count))

    def find_by_author(self):
        select_string = "select patent_number from PatentData where last_name='{0}' and first_name='{1}'"
        cursor = self.lab_conn.cursor() 
        print(select_string.format("smith", "joe"))
        cursor.execute(select_string.format("smith", "joe"))
        print("fetch {0} rows".format(cursor.rowcount))
        for result in cursor.fetchall():
            print(result)
    def find_by_patent_number(self):
        pass

    def find_by_filing_date(self):
        pass

    def delete_DB(self):
        cursor = self.lab_conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS PatentData")
if __name__ == "__main__":
    arguments = docopt.docopt(__doc__)    
    print(arguments)
    mydb = PatentDB()
    if arguments["--create"]:
        mydb.define_DB()
    
    if arguments["--delete"]:
        mydb.delete_DB()


    if arguments["--load"]:
        mydb.load_DB()

    if arguments["--find_by_author"]:
        mydb.find_by_author()
