import tkinter as tk
from tkinter import ttk
from client_app.http_client import HttpClient
from threading import Thread

class ClientApp:
    def __init__(self, master=None):
        # build ui
        self.main = tk.Tk() if master is None else tk.Toplevel(master)
        self.top = ttk.Frame(self.main)
        self.connection = ttk.Labelframe(self.top)

        # self.host_label = ttk.Label(self.connection)
        # self.host_label.configure(text='Host')
        # self.host_label.pack(side='top')
        #
        # self.host_entry = ttk.Entry(self.connection)
        # self.host_entry.pack(side='top')

        self.port_label = ttk.Label(self.connection)
        self.port_label.configure(text='Port')
        self.port_label.pack(side='top')

        reg = self.connection.register(self.is_num)
        self.port_entry = ttk.Entry(self.connection, validate='key', validatecommand=(reg, '%S'))
        self.port_entry.pack(side='top')

        self.connection.configure(labelanchor='nw', relief='flat', text='Connection')
        self.connection.pack(side='top')

        self.top.pack(side='top')
        self.middle = ttk.Frame(self.main)
        self.actions = ttk.Labelframe(self.middle)

        self.button1 = ttk.Button(self.actions)
        self.button1.configure(text='Get user', command=self.render_find_user_form)
        self.button1.pack(side='left')

        self.button2 = ttk.Button(self.actions)
        self.button2.configure(text='Get users', command=self.render_find_users)
        self.button2.pack(side='left')

        self.button3 = ttk.Button(self.actions)
        self.button3.configure(text='Create user', command=self.render_create_user_form)
        self.button3.pack(side='left')

        self.button4 = ttk.Button(self.actions)
        self.button4.configure(text='Delete user', command=self.render_delete_user_from)
        self.button4.pack(side='left')

        self.actions.configure(height='200', takefocus=False, text='Actions', width='200')
        self.actions.pack(side='left')

        self.middle.configure(relief='flat', takefocus=False)
        self.middle.pack(side='top')

        self.bottom = ttk.Frame(self.main)

        self.forms = ttk.Frame(self.bottom)
        self.forms.pack(side='top')

        self.output = ttk.Frame(self.bottom)
        self.output.pack(side='top')

        self.bottom.pack(side='top')
        self.main.minsize(700, 500)

        # Main widget
        self.mainwindow = self.main
        self.mainwindow.title("Distributed Register")

        self.buttons = [self.button1, self.button2, self.button3, self.button4]

        self.http_client = HttpClient()

    def run(self):
        self.mainwindow.mainloop()

    def render_find_users(self):
        self.clear_frame(self.forms)
        self.clear_frame(self.output)

        port = self.port_entry.get()
        if not port:
            self.txt = ttk.Label(self.output, text="Enter port!")
            self.txt.pack(side='top')
            return

        for button in self.buttons:
            button['state'] = tk.DISABLED

        port = self.port_entry.get()
        thread_rest = Thread(target=self.http_client.get_users, args=(port,))
        thread_rest.start()
        self.monitor(thread_rest, self.render_users_output)

    def render_find_user_form(self):
        self.clear_frame(self.forms)
        self.clear_frame(self.output)

        self.label_form_1 = ttk.Label(self.forms, text="User ID")
        self.label_form_1.pack()
        reg = self.forms.register(self.is_num)
        self.entry_form_1 = ttk.Entry(self.forms, validate='key', validatecommand=(reg, '%S'))
        self.entry_form_1.pack()

        self.button_form = ttk.Button(self.forms, text="Apply", command=self.find_user)
        self.button_form.pack()

    def render_create_user_form(self):
        self.clear_frame(self.forms)
        self.clear_frame(self.output)

        self.label_form_1 = ttk.Label(self.forms, text="User name")
        self.label_form_1.pack()
        self.entry_form_1 = ttk.Entry(self.forms)
        self.entry_form_1.pack()

        self.label_form_2 = ttk.Label(self.forms, text="Password")
        self.label_form_2.pack()
        self.entry_form_2 = ttk.Entry(self.forms)
        self.entry_form_2.pack()

        self.button_form = ttk.Button(self.forms, text="Apply", command=self.create_user)
        self.button_form.pack()

    def render_delete_user_from(self):
        self.clear_frame(self.forms)
        self.clear_frame(self.output)

        self.label_form_1 = ttk.Label(self.forms, text="User ID")
        self.label_form_1.pack()
        reg = self.forms.register(self.is_num)
        self.entry_form_1 = ttk.Entry(self.forms, validate='key', validatecommand=(reg, '%S'))
        self.entry_form_1.pack()

        self.label_form_2 = ttk.Label(self.forms, text="User name")
        self.label_form_2.pack()
        self.entry_form_2 = ttk.Entry(self.forms)
        self.entry_form_2.pack()

        self.label_form_3 = ttk.Label(self.forms, text="Password")
        self.label_form_3.pack()
        self.entry_form_3 = ttk.Entry(self.forms)
        self.entry_form_3.pack()

        self.button_form = ttk.Button(self.forms, text="Apply", command=self.delete_user)
        self.button_form.pack()

    def find_user(self):
        self.clear_frame(self.output)

        port = self.port_entry.get()
        if not port:
            self.txt = ttk.Label(self.output, text="Enter port!")
            self.txt.pack(side='top')
            return

        uid = self.entry_form_1.get()
        if not uid:
            self.txt = ttk.Label(self.output, text="Enter UID!!")
            self.txt.pack(side='top')
            return


        self.buttons.append(self.button_form)
        for button in self.buttons:
            button['state'] = tk.DISABLED

        thread_rest = Thread(target=self.http_client.get_user, args=(port, int(uid),))
        thread_rest.start()
        self.monitor(thread_rest, self.render_user_output)

    def create_user(self):
        self.clear_frame(self.output)

        port = self.port_entry.get()
        if not port:
            self.txt = ttk.Label(self.output, text="Enter port!")
            self.txt.pack(side='top')
            return

        name = self.entry_form_1.get()
        password = self.entry_form_2.get()

        if (not name) or (not password):
            self.txt = ttk.Label(self.output, text="Enter data!")
            self.txt.pack(side='top')
            return

        self.buttons.append(self.button_form)
        for button in self.buttons:
            button['state'] = tk.DISABLED

        port = self.port_entry.get()
        thread_rest = Thread(target=self.http_client.create, args=(port, name, password,))
        thread_rest.start()
        self.monitor(thread_rest, self.render_create_output)

    def delete_user(self):
        self.clear_frame(self.output)

        port = self.port_entry.get()
        if not port:
            self.txt = ttk.Label(self.output, text="Enter port!")
            self.txt.pack(side='top')
            return

        uid = self.entry_form_1.get()
        name = self.entry_form_2.get()
        password = self.entry_form_3.get()

        if (not uid) or (not name) or (not password):
            self.txt = ttk.Label(self.output, text="Enter data!")
            self.txt.pack(side='top')
            return

        self.buttons.append(self.button_form)
        for button in self.buttons:
            button['state'] = tk.DISABLED

        port = self.port_entry.get()
        thread_rest = Thread(target=self.http_client.delete, args=(port, int(uid), name, password,))
        thread_rest.start()
        self.monitor(thread_rest, self.render_delete_output)

    def render_user_output(self):
        if self.http_client.response.status_code != 200:
            self.txt = ttk.Label(self.output, text="User doesn't exist!")
            self.txt.pack(side='top')
            return

        user = self.http_client.response.json()
        print(user)

        self.txt = tk.Text(self.output)
        for key, value in user.items():
            self.txt.insert(tk.END, f"{key}: {value}\n")
        self.txt.pack(side='top')
        self.txt.config(state=tk.DISABLED)

    def render_users_output(self):
        users = self.http_client.response.json()
        print(users)

        self.scroll = ttk.Scrollbar(self.output)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.txt = tk.Text(self.output, yscrollcommand=self.scroll.set)

        for user in users:
            for key, value in user.items():
                self.txt.insert(tk.END, f"{key}: {value}\n")
            self.txt.insert(tk.END, '\n')
        self.txt.pack(side='top', fill=tk.X)
        self.txt.config(state=tk.DISABLED)

        self.scroll.config(command=self.txt.yview())

    def render_create_output(self):
        code = self.http_client.response.status_code
        if code == 400:
            msg = "User already exists!"
        else:
            msg = "Success"
        self.txt = ttk.Label(self.output, text=msg)
        self.txt.pack(side='top')

    def render_delete_output(self):
        code = self.http_client.response.status_code
        if code == 403:
            msg = "No permission"
        elif code == 400:
            msg = "User doesn't exist"
        else:
            msg = "Success"
        self.txt = ttk.Label(self.output, text=msg)
        self.txt.pack(side='top')

    def is_num(self, string):
        return string.isdigit()

    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def monitor(self, thread_rest, render_output):
        if thread_rest.is_alive():
            self.main.after(100, lambda: self.monitor(thread_rest, render_output))
        else:
            for button in self.buttons:
                button['state'] = tk.NORMAL

            if (self.http_client.response == None):
                self.txt = ttk.Label(self.output, text="Wrong port")
                self.txt.pack(side='top')
            else:
                render_output()

            self.http_client.response = None
            self.buttons = self.buttons[:4]

