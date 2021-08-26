from os import truncate
from tkinter import *
from tkinter import messagebox
import re
from tkinter.scrolledtext import ScrolledText
#--------------------------all function------------------------------
info_list=[]
def insert_val():
    name=name_entry.get()
    contact=number_entry.get()
    contact_validator=re.compile(r'^[6-9]\d{9}$')
    contact_valdate=contact_validator.findall(contact)
    if len(contact_valdate)==0:
        messagebox.showerror("showerror","Please enter correct contact number")
    else:
        info_list=[]
        con_list=[]
        read_file=open("main.txt",'r')
        read_file.seek(0)
        data=list(read_file)
        for i in data:
            info_list.append(i.split("--->"))

        for j in range(len(info_list)):
            con_list.append(info_list[j][1])

        if str(contact)+"\n" in con_list:
            messagebox.showerror("showerror","Information alredy registerd or please check contact number")

        else:
            file1=open("main.txt","a")
            file1.write(name+"--->"+str(contact)+"\n")
            file1.close()
            messagebox.showinfo("showinfo","data entered successfully")


#--------------------Check button----------------------------------
def check_fun():
    information.delete(0,END)
    file2=open('main.txt','r')
    file2.seek(0)
    info_list=list(file2)
    for i in info_list:
        information.insert(0,i)
    file2.close()


#-----------------------Clear---------------------------
def clear_fun():
    number_entry.delete(0,END)
    name_entry.delete(0,END)



root=Tk()
root.geometry("600x600")
root.minsize(600,600)
root.maxsize(600,600)

head_lab=LabelFrame(root,text="ENTER YOUR INFORMATION HERE",height=600,width=1000,relief=RIDGE,
font=('verdana', 10, 'bold'),borderwidth=3,highlightbackground="white", highlightcolor="white",
highlightthickness=5)
head_lab.place(x=50,y=0)

#----------------------for name of customer-------------------------
name_label=Label(head_lab,text="Enter name",font=('verdana', 10))
name_label.place(x=40,y=40)
name_entry=Entry(head_lab,width=20,bd=4)
name_entry.place(x=130,y=40)

#-----------------------for contact number of customer---------------------
number_label=Label(head_lab,text="Enter contact number",font=('verdana', 10))
number_label.place(x=40,y=80)
number_entry=Entry(head_lab,width=20,bd=4)
number_entry.place(x=190,y=80)

#-----------------------Inserting button------------------------------------
insert_but=Button(head_lab,text="Insert",width=40,bg="Blue",command=insert_val)
insert_but.place(x=40,y=120)

#-----------------------inner frame------------------------------------------
inner_frame=LabelFrame(head_lab,text="View your information here",font=('verdana', 10, 'bold'),relief=RIDGE,height=200,width=800)
inner_frame.place(x=0,y=160)
information = Listbox(inner_frame, width=62, height=20, relief=SUNKEN, borderwidth=3, font=('courier', 9, ''))
information.pack(side = LEFT, fill = BOTH)
scrollbar = Scrollbar(inner_frame, width=62, relief=SUNKEN, borderwidth=3)
scrollbar.pack(side = RIGHT, fill = BOTH)
information.config(yscrollcommand = scrollbar.set)
  
# setting scrollbar command parameter 
# to listbox.yview method its yview because
# we need to have a vertical view
scrollbar.config(command = information.yview)

check_btn=Button(head_lab,text="Check",width=15,bg="Blue",height=2,command=check_fun)
check_btn.place(x=55,y=515)
clear_btn=Button(head_lab,text="Clear",width=15,bg="Blue",height=2,command=clear_fun)
clear_btn.place(x=210,y=515)
        

root.mainloop()
