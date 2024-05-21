from tkinter import *
root = Tk()
root.title("Inheritance")
root.geometry("600x600")

label_name = Label(root, text="User Name : ", font = ("Bell MT", 15, 'bold'), )
label_name.place(relx=0.3,rely=0.2, anchor=CENTER)
entry_name = Entry(root, font = ("Bell MT", 15, 'bold'), )
entry_name.place(relx=0.6,rely=0.2, anchor=CENTER)
label_email = Label(root, text="Email id : ", font = ("Bell MT", 15, 'bold'), )
label_email.place(relx=0.3,rely=0.3, anchor=CENTER)
entry_email = Entry(root, font = ("Bell MT", 15, 'bold'),)
entry_email.place(relx=0.6,rely=0.3, anchor=CENTER)
label = Label(root, font = ("Bell MT", 15, 'bold'))

dictionary = {}
class Users: 
        
    def addUser(key, value):
        global dictionary
        List = {key, value}
        label["text"]=List
        
class GetUsers(Users): 
        
    def getUser(self):
        name = entry_name.get()
        Id = entry_email.get()
        Users.addUser(name, Id)
         
user = GetUsers()
btn = Button(root, text="Add user details", command=user.getUser, )
btn.place(relx=0.5,rely=0.4, anchor=CENTER)
label.place(relx=0.5,rely=0.5, anchor=CENTER)
root.mainloop()

