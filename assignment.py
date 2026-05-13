#!python
import sqlite3

"""
Create a program that will store the database for a veterinary
Each record needs to have the following information:
id unique integer identifier
pet name
pet species (cat, bird, dog, etc)
pet breed (persian, beagle, canary, etc)
owner name
owner phone number
owner email
owner balance (amount owing)
date of first visit

create a program that will allow the user to:
insert a new record into the database and save it automatically
retrieve a record by their id and display all of the information
retrieve a record by the email and display all of the information
retrieve a record by phone number and display all of the information

You will need to create the table yourself. Consider what data types you will
need to use.
"""

cont = True
runs = 0

class database:


    def insert(self):
        pet_name = input("Enter your pet's name: ")
        pet_species = input("Enter your pet's species (cat, bird, dog, etc): ")
        pet_breed = input("Enter your pet's breed (persian, beagle, canary, etc): ")
        owner_name = input("Enter your name: ")
        owner_phone_number = input("Enter your phone number: ")
        owner_email = input("Enter your email: ")
        owner_balance = input("Enter the amount you owe: ")
        date_first_visit = input("Enter the date of your first visit: ")
        query = f"insert into vet (petname,petspecies,petbreed,ownername,ownerphonenumber,owneremail,ownerbalance,datefirstvisit) values ('{pet_name}','{pet_species}','{pet_breed}','{owner_name}','{owner_phone_number}','{owner_email}','{owner_balance}','{date_first_visit}');"
        self.cursor.execute(query)
        self.connection.commit()

    def idret(self):
        id_input = input("Which id do you want to retrieve for?: ")
        query = f"select * from vet where id=('{id_input}');"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        print(f"{'ID':3} {'Pet Name':10} {'Pet Species':12} {'Pet Breed':15} {'Owner Name':15} {'Owner Phone Number':20} {'Owner Email':25} {'Owner Balance':15} {'First Visit':11}")
        for i in result:
            print(f"{i[0]:<3} {i[1]:10} {i[2]:12} {i[3]:15} {i[4]:15} {i[5]:20} {i[6]:25} {i[7]:15} {i[8]:11}")

    def emailret(self):
        email_input = input("Which email do you want to retrieve for?: ")
        query = f"select * from vet where owneremail=('{email_input}');"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        print(f"{'ID':3} {'Pet Name':10} {'Pet Species':12} {'Pet Breed':15} {'Owner Name':15} {'Owner Phone Number':20} {'Owner Email':25} {'Owner Balance':15} {'First Visit':11}")
        for i in result:
            print(f"{i[0]:<3} {i[1]:10} {i[2]:12} {i[3]:15} {i[4]:15} {i[5]:20} {i[6]:25} {i[7]:15} {i[8]:11}")

    def pnret(self):
        phone_number_input = input("Which phone number do you want to retrieve for?: ")
        query = f"select * from vet where ownerphonenumber=('{phone_number_input}');"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        print(f"{'ID':3} {'Pet Name':10} {'Pet Species':12} {'Pet Breed':15} {'Owner Name':15} {'Owner Phone Number':20} {'Owner Email':25} {'Owner Balance':15} {'First Visit':11}")
        for i in result:
            print(f"{i[0]:<3} {i[1]:10} {i[2]:12} {i[3]:15} {i[4]:15} {i[5]:20} {i[6]:25} {i[7]:15} {i[8]:11}")

    def __init__(self):
        file = 'dbase.db'
        self.connection = sqlite3.connect(file)
        self.cursor = self.connection.cursor()
        query = "create table if not exists vet (id integer primary key autoincrement, petname tinytext, petspecies tinytext, petbreed tinytext, ownername tinytext, ownerphonenumber varchar(20), owneremail tinytext, ownerbalance varchar(20), datefirstvisit varchar(20));"
        self.cursor.execute(query)

        print("Would you like to \nA: Insert a new record into the database \nB: Retrieve a record by id \nC: Retrieve a record by email \nD: Retrieve a record by phone number")
        question = input("Type A, B, C, or D: ")
        if question == 'A' or question == 'a':
            self.insert()
        elif question == 'B' or question == 'b':
            self.idret()
        elif question == 'C' or question == 'c':
            self.emailret()
        elif question == 'D' or question == 'd':
            self.pnret()
        else:
            print("unrecognized command")

while cont == True:
    if runs == 0:
        database()
        runs += 1
    else:
        ask = input("Continue? (type y/n): ")
        if ask == 'y' or ask == 'Y' or ask == 'yes' or ask == 'Yes':
            database()
        elif ask == 'n' or ask == 'N' or ask == 'no' or ask == 'No':
            break
        else:
            print("unrecognized command")
