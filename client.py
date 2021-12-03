import requests
import tkinter as tk
from tkinter import ttk

class HttpClient:
    @staticmethod
    def get_users(port):
        response = requests.get("http://localhost:" + port + "/users")
        return response

    @staticmethod
    def get_user(port, uid):
        response = requests.get("http://localhost:" + port + "/user",
                                json={'uid': uid})
        return response

    @staticmethod
    def create(port, name, password):
        response = requests.post("http://localhost:" + port + "/user",
                                 json={'name': name, 'password': password})
        return response

    @staticmethod
    def delete(port, uid, name, password):
        response = requests.delete("http://localhost:" + port + "/user",
                                   json={'uid': uid,
                                         'name': name,
                                         'password': password})
        return response


class ClientApp:
    def __init__(self, master=None):
        # build ui
        self.main = tk.Tk() if master is None else tk.Toplevel(master)
        self.top = ttk.Frame(self.main)
        self.connection = ttk.Labelframe(self.top)
        self.host_label = ttk.Label(self.connection)
        self.host_label.configure(text='Host')
        self.host_label.pack(side='top')
        self.host_entry = ttk.Entry(self.connection)
        self.host_entry.pack(side='top')
        self.port_label = ttk.Label(self.connection)
        self.port_label.configure(text='Port')
        self.port_label.pack(side='top')
        self.port_entry = ttk.Entry(self.connection)
        self.port_entry.pack(side='top')
        self.connection.configure(labelanchor='nw', relief='flat', text='Connection')
        self.connection.pack(side='top')
        self.top.pack(side='top')
        self.middle = ttk.Frame(self.main)
        self.actions = ttk.Labelframe(self.middle)
        self.button1 = ttk.Button(self.actions)
        self.button1.configure(text='Get user')
        self.button1.pack(side='left')
        self.button2 = ttk.Button(self.actions)
        self.button2.configure(text='Get users')
        self.button2.pack(side='left')
        self.button3 = ttk.Button(self.actions)
        self.button3.configure(text='Create user')
        self.button3.pack(side='left')
        self.button4 = ttk.Button(self.actions)
        self.button4.configure(text='Delete user')
        self.button4.pack(side='left')
        self.actions.configure(height='200', takefocus=False, text='Actions', width='200')
        self.actions.pack(side='left')
        self.middle.configure(relief='flat', takefocus=False)
        self.middle.pack(side='top')
        self.bottop = ttk.Frame(self.main)
        self.forms = ttk.Frame(self.bottop)
        self.forms.configure(height='200', width='200')
        self.forms.pack(side='top')
        self.output = ttk.Frame(self.bottop)
        self.output.configure(height='200', width='200')
        self.output.pack(side='top')
        self.bottop.configure(height='200', width='200')
        self.bottop.pack(side='top')
        self.main.minsize(300, 200)

        # Main widget
        self.mainwindow = self.main
        self.mainwindow.title("Distributed Register")

    def run(self):
        self.mainwindow.mainloop()

    def render_find_users(self):
        pass

    def render_find_user_form(self):
        pass

    def render_create_user_form(self):
        pass

    def render_delete_user_from(self):
        pass

if __name__ == '__main__':
    app = ClientApp()
    app.run()
