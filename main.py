from tkinter import *
import tkinter.messagebox as Messagebox
import pymysql as mysql


def insert():
    id=e_id.get()
    name=e_name.get();
    phone=e_phone.get();

    if(id=="" or name=="" or phone==""):
        Messagebox.showinfo("Insert Status", "All Field are required")
    else:
        conn=mysql.connect(host="localhost", user="root", password="", database="python-tkinter")
        cursor=conn.cursor()
        cursor.execute("insert into student values('"+id+"', '"+name+"', '"+phone+"')")
        cursor.execute("commit");

        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_phone.delete(0, 'end')
        show()
        Messagebox.showinfo("Insert Status", "Inserted Successfully");
        conn.close();
def delete():
    if(e_id.get() == ""):
        Messagebox.showinfo("Delete Status", "ID is compolsory for delete")
    else:
        conn=mysql.connect(host="localhost", user="root", password="", database="python-tkinter")
        cursor=conn.cursor()
        cursor.execute("delete from student where id='"+e_id.get()+"'")
        cursor.execute("commit");

        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_phone.delete(0, 'end')
        show()
        Messagebox.showinfo("Delete Status", "Deleted Successfully");
        conn.close();
def update():
    id=e_id.get()
    name=e_name.get();
    phone=e_phone.get();

    if(id=="" or name=="" or phone==""):
        Messagebox.showinfo("Update Status", "All Field are required")
    else:
        conn=mysql.connect(host="localhost", user="root", password="", database="python-tkinter")
        cursor=conn.cursor()
        cursor.execute("update student set name='"+name+"', phone='"+phone+"' where id='"+id+"'")
        cursor.execute("commit");

        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_phone.delete(0, 'end')
        show()
        Messagebox.showinfo("Updated Status", "Updated Successfully");
        conn.close();

def get():
    if(e_id.get() == ""):
        Messagebox.showinfo("Delete Status", "ID is compolsory for delete")
    else:
        conn=mysql.connect(host="localhost", user="root", password="", database="python-tkinter")
        cursor=conn.cursor()
        cursor.execute("select * from student where id='"+e_id.get()+"'")
        rows=cursor.fetchall()
        for row in rows:
            e_name.insert(0, row[1])
            e_phone.insert(0, row[2])
        conn.close();

def show():
    conn=mysql.connect(host="localhost", user="root", password="", database="python-tkinter")
    cursor=conn.cursor()
    cursor.execute("select * from student")
    rows=cursor.fetchall()
    list.delete(0, list.size())
    for row in rows:
        insertData=str(row[0])+' '+row[1]
        list.insert(list.size()+1, insertData)
    conn.close();
    
root = Tk()
root.geometry("600x300")
root.title("Python-tkinter")

id=Label(root,text='Enter ID', font=('bold',10))
id.place(x=20,y=30)

name=Label(root,text='Enter Name', font=('bold',10))
name.place(x=20,y=60)

phone=Label(root,text='Enter Phone', font=('bold',10))
phone.place(x=20,y=90)

e_id= Entry()
e_id.place(x=150, y=30)

e_name= Entry()
e_name.place(x=150, y=60)

e_phone= Entry()
e_phone.place(x=150, y=90)

insert = Button(root, text="Insert", font=("italic", 10), bg="white", command=insert)
insert.place(x=20, y=140)

delete = Button(root, text="Delete", font=("italic", 10), bg="white", command=delete)
delete.place(x=70, y=140)

update = Button(root, text="Update", font=("italic", 10), bg="white", command=update)
update.place(x=130, y=140)

get = Button(root, text="Get", font=("italic", 10), bg="white", command=get)
get.place(x=190, y=140)

list= Listbox(root)
list.place(x=290, y=30)
show()

root.mainloop()
