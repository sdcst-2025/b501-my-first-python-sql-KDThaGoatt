#!python3
import sqlite3

file = 'dbase.db'
connection = sqlite3.connect(file)
print(connection)

cursor = connection.cursor()

cursor.execute('delete from customers') 
# note, you don't want to delete the table data regularly, 
# this is just for demo purposes do we don't end up with
# duplicate records every time we run this program

data = [
    ['Joe Mantenga','joe@sdss.ca',12345],
    ['Hanna Montana','miley@cyrus.com',32],
    ['Amanda Huggenkis','cool1@gmail.com',12],
    ['Michael Jackson','singer@thriller.com',1],
    ['Peter Nesmith','bassist@monkees.org',89],
    ['Casey Fried','cfried@kitties.com',34],
    ['Megan Finger','mfin@google.com',33],
    ['Randy Fisher','fisherran@spoons.net',1993],
    ['Donald Green','dg@camborf.com',91],
    ['Sam Sung','samsung@apple.com',913],
    ['Jock Hamz','jhamz@tester.net',999],
    ['Wayne Gretkzy','wayne@oilers.ca',99],
    ['Joseph Palpatine','emperor@oldrepublic.org',2],
    ['Malcolm Reynolds','captain@serenity.ship',76]
    ]
for i in data:
    query = f"insert into customers (name,email,cnum) values ('{i[0]}','{i[1]}',{i[2]});"
    print(query)
    cursor.execute(query)
connection.commit()
query = "select * from customers"
cursor.execute(query)
result = cursor.fetchall()
print(result)
for i in result:
    print(i)