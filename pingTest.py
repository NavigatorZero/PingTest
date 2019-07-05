from tkinter import *
from tkinter import messagebox
import platform    # For getting the operating system name
import subprocess
import os

hostname=1


def show_message():
    response = os.system("ping " + message.get())
#and then check the response...
    if response == 0:
      Check.select()
    else:
      Check.deselect()

    response1 = os.system("ping " + message1.get())
#and then check the response...
    if response1 == 0:
      Check1.select()
    else:
      Check1.deselect()

    response2 = os.system("ping " + message2.get())
#and then check the response...
    if response2 == 0:
      Check2.select()
    else:
      Check2.deselect()
      
    response3 = os.system("ping " + message3.get())
#and then check the response...
    if response3 == 0:
      Check3.select()
    else:
      Check3.deselect()
      
    response4 = os.system("ping " + message4.get())
#and then check the response...
    if response4 == 0:
      Check4.select()
    else:
      Check4.deselect()
      
    

    response5 = os.system("ping " + message5.get())
#and then check the response...
    if response5 == 0:
      
      Check5.select()
    else:
      Check5.deselect()

    response6 = os.system("ping " + message6.get())
#and then check the response...
    if response6 == 0:
      Check6.select()
    else:
      Check6.deselect()







 
 
root = Tk()
root.title("Пинг bySavelev))))))")
root.geometry("300x500")
 
message = StringVar()
message1 = StringVar()
message2 = StringVar()
message3 = StringVar()
message4 = StringVar()
message5 = StringVar()
message6 = StringVar()
message7 = StringVar()
message8 = StringVar()






message_entry = Entry(textvariable=message)
message_entry.grid(row=10, column=10, sticky=W)
Check=Checkbutton(root,text="Ip1", padx=0, pady=0)
Check.grid(row=10, column=11, sticky=W)

message_entry1 = Entry(textvariable=message1)
message_entry1.grid(row=20, column=10, sticky=W)
Check1=Checkbutton(root,text="Ip2",onvalue=1, offvalue=0, padx=0, pady=0)
Check1.grid(row=20, column=11, sticky=W)

message_entry2 = Entry(textvariable=message2)
message_entry2.grid(row=30, column=10, sticky=W)
Check2=Checkbutton(root,text="Ip3",onvalue=1, offvalue=0, padx=0, pady=0)
Check2.grid(row=30, column=11, sticky=W)

message_entry3 = Entry(textvariable=message3)
message_entry3.grid(row=40, column=10, sticky=W)
Check3=Checkbutton(root,text="Ip4",onvalue=1, offvalue=0, padx=0, pady=0)
Check3.grid(row=40, column=11, sticky=W)

message_entry4 = Entry(textvariable=message4)
message_entry4.grid(row=50, column=10, )
Check4=Checkbutton(root,text="Ip5",onvalue=1, offvalue=0, padx=0, pady=0)
Check4.grid(row=50, column=11, sticky=W)

message_entry5 = Entry(textvariable=message5)
message_entry5.grid(row=60, column=10, sticky=W)
Check5=Checkbutton(root,text="Ip6",onvalue=1, offvalue=0, padx=0, pady=0)
Check5.grid(row=60, column=11, sticky=W)

message_entry6 = Entry(textvariable=message6)
message_entry6.grid(row=70, column=10, sticky=W)
Check6=Checkbutton(root,text="Ip7",onvalue=1, offvalue=0, padx=0, pady=0)
Check6.grid(row=70, column=11, sticky=W)




 
message_button = Button(text="Пинг", command=show_message)
message_button.place(relx=.5, rely=.9, anchor="c")
 
root.mainloop()
