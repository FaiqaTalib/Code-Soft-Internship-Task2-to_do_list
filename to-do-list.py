from tkinter import *
import tkinter.messagebox

root=Tk()
root.title("T_D_L")
root.geometry("600x500")
root.config(bg="white")

def add_btn():
    task=entry.get()
    
    if task!="":
        libox.insert(tkinter.END,task)
        entry.delete(0,tkinter.END)
    else:
        
        tkinter.messagebox.showwarning(title="Warning",message="Must add a task first")

def del_btn():
    select=libox.curselection()
    if select:
        libox.delete(select[0])

def edit_btn():
    tsk=libox.curselection()
    if tsk:
        tsk=tsk[0]
        newtsk=entry.get()
        if newtsk:
            libox.delete(tsk)
            libox.insert(tsk,newtsk)
            entry.delete(0,END)
        else:
            messagebox.showwarning("Please enter a new task")
    

frame1=Frame(root)
frame1.grid()

txt1=Label(root,text="To Do List...",bg="#355E3B",justify='left',font=("Rosewood Std Regular",25),width=33,height=3)
txt1.grid()

txt2=Label(root,text="Add items in list",bg="white",justify="left",font=("Rosewood Std Regular",20))
txt2.grid()

entry=Entry(root,width=50)
entry.grid(padx=10) 

add_btn=Button(root,width=15,height=2,text="Submit",command=add_btn)
add_btn.grid(padx=10)

txt3=Label(root,text="Tasks in list",justify='left',bg="white",font=("Rosewood Std Regular",20))
txt3.grid()

libox=tkinter.Listbox(root,height=10,width=60)
libox.grid()

edit=Button(root,text="Edit",bg="green",command=edit_btn)
edit.grid()

dele=Button(root,text="Delete",bg="red",command=del_btn)
dele.grid()

root.mainloop()
