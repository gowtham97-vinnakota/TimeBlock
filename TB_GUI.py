from tkinter import *
from tkinter import 

app = Tk()
app.title('TimeBlock')
mainframe_1 = ttk.Frame(app, padding=30, borderwidth=10, relief=SUNKEN)
greet = ttk.Label(mainframe_1, text='Greetings', anchor='center', justify='center', padding=[75, 20])
greet['background'] = 'green'

user = ttk.Label(mainframe_1, text='User', anchor='center', justify='center', padding=[75, 20])
user['background'] = 'yellow'

weekly = ttk.Button(mainframe_1, text='WEEK', padding=[50, 30])
daily = ttk.Button(mainframe_1, text='DAY', padding=[50, 30])

setting = ttk.Button(mainframe_1, text='Settings')
tip = ttk.Button(mainframe_1, text='Tips')

mainframe_1.grid(row=0, column=0, sticky='nwes')

greet.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky='nwes')
user.grid(row=1, column=1, padx=10, pady=10, sticky='nwes')

weekly.grid(row=2, column=0, padx=10, pady=10, sticky='nwes')
daily.grid(row=2, column=2, padx=10, pady=10, sticky='nwes')

setting.grid(row=3, column=0, padx=30, pady=30)
tip.grid(row=3, column=1, padx=30, pady=30)

# for child in mainframe_1.winfo_children():
#     child.grid_configure()

app.columnconfigure(0, weight=1)
app.rowconfigure(0, weight=1)

mainframe_1.columnconfigure(0, minsize='5c', weight=2)
mainframe_1.columnconfigure(1, minsize='5c', weight=2)
mainframe_1.columnconfigure(2, minsize='5c', weight=2)

mainframe_1.rowconfigure(1, minsize='2c', weight=1)
mainframe_1.rowconfigure(0, minsize='2c', weight=1)
mainframe_1.rowconfigure(2, minsize='2c', weight=1)
#mainframe_1.rowconfigure(3, minsize=50, weight=1)
app.mainloop()
