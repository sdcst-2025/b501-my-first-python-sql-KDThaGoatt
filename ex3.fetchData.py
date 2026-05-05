#!python3
import sqlite3


# this is the code from example2 with 1 change. Can you see the difference?
file = 'dbase.db'
connection = sqlite3.connect(file)
cursor = connection.cursor()
query = "select * from customers where cnum>1000;"
cursor.execute(query)
result = cursor.fetchall()

# We will print the result of the query.
# uncomment the next line and run the program
print(result)

# whoa, note that the result is a bit of a mess.
# uncomment the next block of code and see how it looks
# a bit more organized.  Comment out line 15 so we don't have
# to see that mess
# next code block begins here
#for i in result:
#    print(i)
# next code block ends here

# You will notice that we had a list of tuples
# each tuple is a result that is retrieved from the database table
# We don't know what the elements represent without understanding
# what the table PRAGMA results showed. Let me remind you:
"""
(0, 'id', 'INTEGER', 0, None, 1)
(1, 'name', 'tinytext', 0, None, 0)
(2, 'email', 'tinytext', 0, None, 0)
(3, 'cnum', 'INT', 0, None, 0)
"""
# So this means that:
#  the first element is the id
#  the second element is the name
#  the 3rd element is the email
#  the 4th element is the cnum (customer number)
# We could now use the data in the table and find different ways to
# search it for values, or display it

# Comment out line 22 and 23 and uncomment the next block to see how
# we can display the data nicer:
# --Block begins
print(f"{'ID':>3} {'Name':20} {'Email':25} {'Customer#':10}")
for i in result:
    print(f"{i[0]:3} {i[1]:20} {i[2]:25} {i[3]:<10}")
# --Block ends

# We can also selectively print only those records that match
# a search critera that we set
# Uncomment out the following block to search for records
# that contain names that contain a J
# --Block begins
#print(f"{'ID':>3} {'Name':20} {'Email':25} {'Customer#':10}")
#for i in result:
#    if "J" in i[1]:
#        print(f"{i[0]:3} {i[1]:20} {i[2]:25} {i[3]:<10}")
# --Block ends

# Note: This is an inefficent way to do this. Consider that
# we read in the entire database, and then only picked out
# the elements we wanted
# It would be far more efficient to filter the results
# during the search of the database rather than after we
# retrieved them all!



