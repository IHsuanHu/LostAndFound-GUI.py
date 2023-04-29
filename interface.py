
'''
input data interface
'''
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry

window = Tk()
window.title("Lost and Found System")

def getvalue():
    item = itemValue.get()
    date = dateValue.get()
    color = colorValue.get()
    location = locationValue.get()
    note = noteValue.get()
    print(item, date, color, location, note)
#items
itemValue = StringVar()
useritems = Label(window, text= 'Item', justify= RIGHT, 
                  font=('Times', 20)).grid(row=0, column= 0, sticky= W)

useritemsans = ttk.Combobox(window, values=['Bottle', 'Umbrella', 'Coat', 
   'laptop', 'Cellphone', 'Wallet','Charger', 'Bag', 'Mug or Cup', 'Others']
            , textvariable= itemValue).grid(row=0, column= 1, sticky= E)


#date
dateValue = StringVar()
Label(window,text='Date',justify= RIGHT,font=('Times', 20)).grid(row= 1
                                , column= 0, sticky= W)
DateEntry(window,selectmode='day', textvariable= dateValue).grid(row=1,
                            column=1,sticky= E)


#color
colorValue = StringVar()
Label(window, text= 'Color', justify= RIGHT, 
                  font=('Times', 20)).grid(row=2, column= 0, sticky= W)
ttk.Combobox(window, values= ['Pink', 'Red', 'Orange', 'Yellow', 'Green', 
    'Blue', 'Dark Blue', 'Purple', 'Brown', 'Gray', 'Black','White',
     'Beige'], textvariable= colorValue).grid(row= 2, column= 1, sticky= E)

#location
locationValue = StringVar() 
Label(window, text= 'Location', justify= RIGHT, 
      font=('Times', 20)).grid(row= 3, column= 0, sticky= W)

ttk.Combobox(window, values= ['First Floor', 'Second Floor', 'Thrid Floor'], 
             textvariable= locationValue).grid(row= 3, column= 1, sticky= E)

#note
noteValue = StringVar()
Label(window, text= 'Note', justify= RIGHT, 
                 font=('Times', 20)).grid(row= 4, column= 0, sticky= W)
ttk.Entry(window, textvariable= noteValue).grid(row=4, column=1, sticky= E)


syinput = Button(window, text='Confirm', command= getvalue).grid(row=5, 
                                column= 0, sticky= W)
syexit = Button(window, text='  Exit  ', command= window.destroy).grid(row=5, 
                                        column= 1, sticky= E)

window.mainloop()


# from tkinter import *
# from tkinter.ttk import *
 
# # creates a Tk() object
# master = Tk()
 
# # sets the geometry of main
# # root window
# master.geometry("200x200")
 
 
# # function to open a new window
# # on a button click
# def openNewWindow():
     
#     # Toplevel object which will
#     # be treated as a new window
#     newWindow = Toplevel(master)
 
#     # sets the title of the
#     # Toplevel widget
#     newWindow.title("New Window")
 
#     # sets the geometry of toplevel
#     newWindow.geometry("200x200")
 
#     # A Label widget to show in toplevel
#     Label(newWindow,
#           text ="This is a new window").pack()
 
 
# label = Label(master,
#               text ="This is the main window")
 
# label.pack(pady = 10)
 
# # a button widget which will open a
# # new window on button click
# btn = Button(master,
#              text ="Click to open a new window",
#              command = openNewWindow)
# btn.pack(pady = 10)
 
# # mainloop, runs infinitely
# mainloop()

