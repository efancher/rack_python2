#!/usr/bin/env python
#!*-* coding:utf-8 *-*

"""

:mod:`lab04_DBAPI` -- DBAPI (PEP-249)
=========================================

LAB04 Learning Objective: Familiarization with DB-API
      Optional Objective: Use the re module for step b

 a. Define a new data-only class called PatentData with the following attributes:
     #. last_name
     #. first_name
     #. patent_number
     #. filing_date

     PatentData has a method get_patent_dict() that returns a dict of instance data
     using attribute names as the keys.

 b. Now a choice. You can either use patent_data.sgm as the data source (use
    the *re* module to source instances of PatentData) OR make up your own PatentData 
    instances per a) above.

 c. Implement a new class called PatentDB with the following methods:
       #. define_DB() with appropriate SQL statements. Raises DefineDBError
          exception with a message if error occurs
       #. load_DB() with appropriate SQL statements to load the file of
          PatentData serialized records from the json file. Raises
          LoadError exception with message if error occurs
       #. find_by_author() :  Use SQL SELECT statements to return a list of
          patent numbers held by the given author, else None
       #. find_by_patent_number():Use SQL SELECT statements to return all
          attributes of the given patents as a list, else raise a PatentNotFoundError
          exception
       #. find_by_filing_date()Use SQL SELECT statements to return a list of
          patent numbers filed on the given date (ISO8601 format), else None

 d. Save PatentDB in a module called patentDB_runner.py with a main() function,
    and argparse (or docopt) code to support arguments for all method inputs.

 e. Create a mini patent database using the patentDB_runner module:
       #. Define database with PatentDB.defineDB()
       #. Populate with PatentDB.load_DB()
       #. Test find_by_patent_number() 

"""

def class PatentData(object):
    
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
            "filing_data": self.filing_date}

def class PatentDB(object):
    def define_DB(self):
        pass

    def load_DB(self):
        pass

    def find_by_author(self):
        pass
    
    def find_by_patent_number(self):
        pass

    def find_by_filing_date(self):
        pass


if __name__ == "__main__":
    pass
