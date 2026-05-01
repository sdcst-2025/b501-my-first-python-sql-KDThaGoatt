#!python3
import sqlite3

file = 'dbase.db'
connection = sqlite3.connect(file)
print("If you successfully connect to a database file,\nyou will see the SQL connection obect below:")
print("------------------------------------")
print(connection)
print("------------------------------------")

print()
print()
print()

# create a cursor to send commands to the sqlite connection
cursor = connection.cursor()

# now we can send commands to the cursor.
# we will generate the command or query just like a string
# note that the commands must end with a ;
# uncomment the next line and try running this program
#query = "PRAGMA table_info(customers);"

# you will notice that nothing happened. All we did was create a
# command and didn't do anything with it
# once we have a command created, we can send it to the cursor
# and execuite it
# uncomment the next line and run this program again
#cursor.execute(query)

# again, nothing has happened. Requests and database commands
# happen behind the scenes. You won't see anything because we didn't
# say to do anything with the result of the query
# since this command is trying to retrieve data, let's retrieve
# the data and store it in a variable
# uncomment the next 2 lines and see the result
#result = cursor.fetchall()
#print(result)

# Open the example2 file and we will start looking at what the data
# contains



