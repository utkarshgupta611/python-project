from tkinter import *
root = Tk()

#FUNCTION
def getvalsss():
    print(f"{namevalue.get()} ,{phonevalue.get()}, {gendervalue.get()}, {emergencyvalue.get()}, {transcationmodevalue.get()}, {foodservicevalue.get()}")
    #                    \>  use a to continue the record
    with open('record.txt','a') as f:
        f.write(f"{namevalue.get()}, {phonevalue.get()}, {gendervalue.get()}, {emergencyvalue.get()}, {transcationmodevalue.get()}, {foodservicevalue.get()}\n")

#display
root.geometry("455x355")
root.maxsize(width=655 ,height=555)
root.title("travel form")

#label -- top row
Label(root, text='Form', font="comicsansms 19 bold", padx=335, pady=20).grid(row=0, column=2)

#entry from
name = Label(root,text="name")
phone = Label(root, text="phone")
gender = Label(root, text="gender")
emergency = Label(root, text="emergency")
transcationmode =Label(root, text="transcationmode")

#closing entry form
name.grid(row=1, column=1)
phone.grid(row=2, column=1)
gender.grid(row=3, column=1)
emergency.grid(row=4, column=1)
transcationmode.grid(row=5, column=1)

#value textvariable for entry
namevalue= StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
transcationmodevalue = StringVar()
foodservicevalue = IntVar()

#entry variable
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderrentry = Entry(root, textvariable=gendervalue)
emergencyentry = Entry(root, textvariable=emergencyvalue)
transcationmodeentry = Entry(root, textvariable=transcationmodevalue)

#closing entry variable
nameentry.grid(row=1, column=2)
phoneentry.grid(row=2, column=2)
genderrentry.grid(row=3, column=2)
emergencyentry.grid(row=4, column=2)
transcationmodeentry.grid(row=5, column=2)

#check button assigned
foodservice= Checkbutton(text ="pre book", variable=foodservicevalue)
foodservice.grid(row=6, column=2)

#submit
submit = Button(root, text="submit", command=getvalsss)
submit.grid(row=7, column=2)



root.mainloop()