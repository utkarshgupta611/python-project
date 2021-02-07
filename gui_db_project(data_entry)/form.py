from tkinter import *
import csv
import sqlite3

# Tkinter window
root = Tk()

# last step --> function to collect user inputs
def getvalues():
    print(f'{namevalue.get()} , {phonevalue.get()} , {agevalue.get()} , {emailvalue.get()} , {professionvalue.get()} , {checkvalue.get()}')
    print(f'name-> {namevalue.get()} , phone_no.-> {phonevalue.get()} , age ->{agevalue.get()} , email->{emailvalue.get()} , profession->{professionvalue.get()} , male->{checkvalue.get()}')
    with open('record.txt', 'a') as f:
        f.write(f'{namevalue.get()} , {phonevalue.get()} , {agevalue.get()} , {emailvalue.get()} , {professionvalue.get()} , {checkvalue.get()}\n')

# display
root.geometry("655x255")
root.maxsize(width=655, height=555)
root.title("Data Entry")

# Label --> Heading
Label(root, text='Form', font="comicsansms 19 bold", padx=335, pady=20).grid(row=0, column=1)

# Entry Detail column
Name = Label(root, text='NAME').grid(row=1, column=0)
phone_no = Label(root, text='CONTACT_NUMBER').grid(row=2, column=0)
age = Label(root, text='AGE').grid(row=3, column=0)
email = Label(root, text='E-MAIL').grid(row=4, column=0)
profession = Label(root, text='PROFESSION').grid(row=5, column=0)

# Value of Detail column
namevalue = StringVar()
phonevalue = IntVar()
agevalue = IntVar()
emailvalue = StringVar()
professionvalue = StringVar()

# Entry column or space
name_entry = Entry(root, textvariable=namevalue).grid(row=1, column=1)
phone_entry = Entry(root, textvariable=phonevalue).grid(row=2, column=1)
age_entry = Entry(root, textvariable=agevalue).grid(row=3, column=1)
email_entry = Entry(root, textvariable=emailvalue).grid(row=4, column=1)
profession_entry = Entry(root, textvariable=professionvalue).grid(row=5, column=1)

# Gender check box
checkvalue = StringVar()
gender = Label(root, text='MALE').grid(row=6, column=0)
gender_entry = Checkbutton(root, textvariable=checkvalue).grid(row=6, column=1)

# Submit Button
submit = Button(root, text='SUBMIT', command=getvalues).grid(row=7, column=1)

root.mainloop()

# Step up database using sqlite3 library

# Intializing connection and cursor
conn = sqlite3.connect('employeetab.db')
print('Connected with Database.........')
cursor = conn.cursor()
sqlstr = '''
        CREATE TABLE IF NOT EXISTS employee_chart(
        Name  TEXT ,
        Phone_number TEXT,
        Age TEXT,
        Email TEXT,
        profession TEXT,
        Male TEXT)'''
cursor.execute(sqlstr)
with open ('record.txt') as datafile:
    read_csv = csv.reader(datafile)
    for row in read_csv:
        print(row)
        cursor.execute("INSERT INTO employee_chart VALUES ('{Name}', '{Phone_number}', '{Age}', '{Email}', '{profession}', '{Male}')".format(Name=row[0], Phone_number=row[1], Age=row[2], Email=row[3], profession=row[4], Male=row[5]))

        cursor.execute("SELECT * FROM employee_chart")
result = cursor.fetchall()

print('printing database .. querry........')

for row in result:
    print(row)