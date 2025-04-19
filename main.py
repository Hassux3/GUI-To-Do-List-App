# To-Do-List
from tkinter import *

task_list = []


def open_Tasklist():
    global task_list
    try:
        with open('Task_list.txt', 'r') as f:
            tasks = f.readlines()

            for task in tasks:
                if task != '\n':
                    task_list.append(task)
                listbox.insert(END,f' -->  {task}')
    except:
        f = open('Task_list.txt', 'w')
        f.close

        

def add():
    global task_list
    task = entry_var.get()
    task_entry.delete(0,END)
    task_list.append(task)

    if task:
        with open('Task_list.txt', 'a') as f:
            f.write(f'{task}\n')
        task_list.append(task)
        listbox.insert(END,f' -->  {task}')
    print("task_list: ", task_list)

def delete_task():
    global task_list
    listbox.delete(ANCHOR)
    new_tasks = listbox.get(0,END)

    with open('Task_list.txt', 'w') as taskfile:
        for task_toAdd in new_tasks:
            taskfile.write(task_toAdd[6:]+'\n')


if __name__ == '__main__':
    root = Tk()
    root.title('To-Do-List')
    root.geometry('400x665+400+100')
    root.resizable(False,False)

    icon_image = PhotoImage(file='images/icon.png')
    root.iconphoto(False,icon_image)

    top_image = PhotoImage(file='images/top.png')
    Label(root, image=top_image, font=('Constantia', '30')).place(x=0, y=0)


    Label(root, text='ALL TASKS', font=('Constantia', '35'), fg='white', bg='#39485E').place(x=83, y=15)

    entry_var = StringVar()
    task_entry = Entry(root,textvariable=entry_var, font=('Constantia', '25'))
    task_entry.place(x=0, y=200, width=300, height=50)

    Button(root,text='Add', font=('Forte', '20'), bg='#39485E', fg='white', command=add, bd=0).place(x=300,y=200, width=100, height=50)

    frame = Frame(root, width=400,height=330)
    frame.pack(pady=(250,0), fill=X)

    
    listbox = Listbox(frame, font=('Cambria', '18'), fg='white', bg='#39485E', width=29,cursor='hand2', height=11)
    listbox.pack(side=LEFT,fill=BOTH)

    open_Tasklist()

    scrollbar = Scrollbar(frame, width=20)
    scrollbar.pack(fill=BOTH,side=RIGHT)
    
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)

    delete_image = PhotoImage(file='images/delete.png')

    Button(root, image=delete_image,command=delete_task, bd=0).place(x=160,y=580, height=80)


    
    root.mainloop()
