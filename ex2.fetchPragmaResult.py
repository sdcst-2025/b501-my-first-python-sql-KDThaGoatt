#!python3
import sqlite3


# this is the code from example1
file = 'dbase.db'
connection = sqlite3.connect(file)
cursor = connection.cursor()
query = "PRAGMA table_info(customers);"
cursor.execute(query)
result = cursor.fetchall()

"""
you will have noticed that the data is a complex data
structure that consists of a list of tuples.  Let's take a look
at each of the tuples.
"""
for i in result:
    print(i)

"""
When we do a pragma request, we are asking for the structure of the
database table.  This pragma request gives us 4 results, which means
that there are 4 columns in the table if we consider it as a spreadsheet
Each tuple is telling us some important information about the data
The first data point/column is the column number
The second data point/column is the name of the data structure
The 3rd data point/column is the type of data that this will store
The 4th data point/column tells us whether NULL results are allowed 0=false
The 5th data point/column tells us if there is a default value and what it is
The 6th and last data point/column tells us if the column is a primary key

example:
(0,'id','INTEGER',0,None,1)
means that records will have a field called "id" that is an integer
value.  It can not be a NULL value and has no default value, but it
is a primary key.  All values must be unique

(1, 'name', 'tinytext', 0, None, 0)
means that there is a field called "name" that is a tinytext (text of
maximum 255 characters).  It can not be a NULL value and has no default.
It is not a primary key, so there can be duplicate values in the
table
"""




