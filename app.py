import customtkinter as ctk
import json

#user information
name = "Alex"
password = '1234'


class InfoForm(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)





class MyTabView(ctk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # create tabs
        self.add("tab 1")
        self.add("tab 2")



class Sidebar(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.configure(width=400)

        newinvbtn = ctk.CTkButton(self, text='NEW HELP TICKET')
        newinvbtn.pack(padx=20, pady=10)


class MainFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(3, weight=1)

        header = ctk.CTkLabel(self, text="New Help Ticket", width=700)
        header.grid(row=0, column=0, columnspan=4, sticky='nsew', pady=10)

        emplName = ctk.CTkEntry(self, placeholder_text="Employee Name:")
        emplName.grid(row=2, column=0, sticky='nsew', padx=5)

        emplID = ctk.CTkEntry(self, placeholder_text='Employee Email:')
        emplID.grid(row=2, column=1, sticky='nsew', padx=5)

        emplEmail = ctk.CTkEntry(self, placeholder_text='Employee ID Number:')
        emplEmail.grid(row=2, column=2, sticky='nsew', padx=5)

        optionmenu = ctk.CTkOptionMenu(self, values=["option 1", "option 2"])
        optionmenu.grid(row=2, column=3, sticky='nsew', padx=5)

        subjectline = ctk.CTkEntry(self, placeholder_text='Subject:', height=30)
        subjectline.grid(row=3, column=0, columnspan=4, sticky='new', padx=5, pady=10)

        description = ctk.CTkTextbox(self, height=350)
        description.insert("0.0", "Description of problem")
        description.grid(row=3, column=0, columnspan=4, rowspan=5, sticky='ESW', padx=5)
        #search = ctk.CTkEntry(self, placeholder_text='Search', width=700)
        #search.grid(row=0, column=0, sticky='nsew')

        def SaveTicket():
            n = open('ticket number.txt', 'r')
            tic = int(n.read())

            ticno = tic + 1

            f = open(f'ticket {str(ticno)}.txt', "w")

            x = f'Name-{emplName.get()}\nID-{emplID.get()}\nEmail-{emplEmail.get()}\nSubject-{subjectline.get()}\nDescription-{description.get("0.0", "end")}'

            a = open('ticket number.txt', 'w')
            a.write(str(ticno))

            f.write(x)


        savebtn = ctk.CTkButton(self, text='SUBMIT', command=SaveTicket, height=25)
        savebtn.grid(row=8, column=0, columnspan=4, sticky="sew", padx=5, pady=5)


        #tab_view = MyTabView(master=self)
        #tab_view.grid(row=1, column=0, sticky='nsew')




class Main(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('950x550')
        self.title ('Help Desk Ticket')

        #configure grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        #UI

        #sidebar
        sidebar = Sidebar(master=self)
        sidebar.grid(row=0, column=0, rowspan=2, sticky="nsew", padx=10, pady=10)

        #main frame
        main_frame = MainFrame(master=self)
        main_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)





Main().mainloop()
