from tkinter import *

tut_root = Tk()
#"widthxhieght"
tut_root.geometry("455x400")
tut_root.title("my newspapper")
# width,hieght
# tut_root.maxsize(400,400)
# tut_root.minsize(200,200)

#heading
heading_label = Label(text="THE NEWSPAPPER",bg ="black" ,
                      fg="white",font="comicsansms 19 bold",
                      borderwidth=3, relief=SUNKEN)
heading_label.pack(side='top', fill='x', padx=34, pady=14)
#new1
news1_label = Label(text="Farmers Reject Amit Shah Talks Offer Hinging On Venue Change: 10 Points",
                    bg ="red" ,fg="white",font="comicsansms 19 bold",
                      borderwidth=3, relief=SUNKEN)
news1_label.pack(side='top', fill='x', padx=34, pady=14)
#news2
news2_label = Label(text="Man Charred to Death While Sleeping in Car Near Farmers' Protest at Delhi-Haryana Border",
                    bg ="red" ,fg="white",font="comicsansms 19 bold",
                      borderwidth=3, relief=SUNKEN)
news2_label.pack(side='top', fill='x', padx=34, pady=14)
#news3
news3_label = Label(text="Bird Watching, Cherry Blossoms: PM Modi On Connect With Nature Amid Pandemic",
                    bg ="red" ,fg="white",font="comicsansms 19 bold",
                      borderwidth=3, relief=SUNKEN)
news3_label.pack(side='top', fill='x', padx=34, pady=14)

#news4
news4_label = Label(text="Bird Watching, Cherry Blossoms: PM Modi On Connect With Nature Amid Pandemic",
                    bg ="red" ,fg="white",font="comicsansms 19 bold",
                      borderwidth=3, relief=SUNKEN)
news4_label.pack(side='top', fill='x', padx=34, pady=14)

#news5
news5_label = Label(text="and how its work ",
                    bg ="red" ,fg="white",font="comicsansms 19 bold",
                      borderwidth=3, relief=SUNKEN)
news5_label.pack(side='top', fill='x', padx=34, pady=14)
# #image
# photo=PhotoImage(file="12.png")

# azure_label = Label(image=photo)
# azure_label.pack(side='bottom', fill='x', padx=34, pady=14)


tut_root.mainloop()