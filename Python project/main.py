from functools import partial
from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql
import credentials as cr
import custom as cs

class Management:
    def __init__(self,root):
        self.window=root
        self.window.title("Student Management System")
        self.window.geometry("780x480")
        self.window.config(bg = "white")
        
        # customization
        self.color_1=cs.color_1
        self.color_2=cs.color_2
        self.color_3=cs.color_3
        self.color_4=cs.color_4

        self.font_1=cs.font_1
        self.font_2=cs.font_2

        #credentials
        self.host=cr.host
        self.user=cr.user
        self.password=cr.password
        self.database=cr.database

        # title name
        self.title="Student Management System"

        # frame1-left side
        self.frame_1 = Frame(self.window, bg=self.color_1)
        self.frame_1.place(x=0, y=0, width=540, relheight = 1)

        # frame2=right side
        self.frame_2 = Frame(self.window, bg=self.color_2)
        self.frame_2.place(x=540, y=0, relheight = 1,relwidth=1)

        # add butons in frame-2
        self.add_bt = Button(self.frame_2, text='Add New', font=(self.font_1, 12), bd=2 ,command=self.AddStudent, cursor="hand2", bg=self.color_4,fg=self.color_3).place(x=68,y=40,width=100)
        self.view_bt = Button(self.frame_2, text='View Details', font=(self.font_1, 12), bd=2 ,command=self.GetContact_View, cursor="hand2", bg=self.color_4,fg=self.color_3).place(x=68,y=90,width=100)
        self.update_bt=Button(self.frame_2,text='Update',font=(self.font_1,12),bd=2,command=self.GetContact_Update,cursor='hand2',bg=self.color_4,fg=self.color_3).place(x=68,y=140,width=100)
        self.delete_bt=Button(self.frame_2,text="Delete",font=(self.font_1,12),bd=2,command=self.GetContact_Delete,cursor='hand2',bg=self.color_4,fg=self.color_3).place(x=68,y=190,width=100)
        self.clear_bt=Button(self.frame_2,text='clear',font=(self.font_1,12),bd=2,command=self.ClearScreen,cursor='hand2',bg=self.color_4,fg=self.color_3).place(x=68,y=240,width=100)
        self.exit_bt=Button(self.frame_2,text='Exit',font=(self.font_1,12),bd=2,command=self.Exit,cursor='hand2',bg=self.color_4,fg=self.color_3).place(x=68,y=290,width=100)
     
        self.first_title()

    def first_title(self):
        self.title_label=Label(self.frame_1 , text=self.title , font= (self.font_1, 20 , 'bold'), fg=self.color_4 , bg=self.color_1 )
        self.title_label.place(x=70 ,y=30 )

    ''' To add new students data'''
    def AddStudent(self):
        self.ClearScreen()
        self.name=Label(self.frame_1,text='First name',font=(self.font_2,15,'bold'),bg=self.color_1 , fg=self.color_4 )
        self.name.place(x=40,y=30)
        self.name_entry=Entry(self.frame_1,bg=self.color_4,fg=self.color_3 ) #font=(self.font_2,10)
        self.name_entry.place(x=40,y=60,width=200)

        self.surname=Label(self.frame_1,text='Last name',font=(self.font_2,15,'bold'),bg=self.color_1 , fg=self.color_4)
        self.surname.place(x=300,y=30)
        self.surname_entry=Entry(self.frame_1,bg=self.color_4,fg=self.color_3)
        self.surname_entry.place(x=300,y=60,width=200)

        self.course=Label(self.frame_1,text='Course',font=(self.font_2,15,'bold'),bg=self.color_1 , fg=self.color_4)
        self.course.place(x=40,y=100)
        self.course_entry=Entry(self.frame_1,bg=self.color_4,fg=self.color_3)
        self.course_entry.place(x=40,y=130,width=200)

        self.year=Label(self.frame_1,text='Year',font=(self.font_2,15,'bold'),bg=self.color_1 , fg=self.color_4)
        self.year.place(x=300,y=100)
        self.year_entry=Entry(self.frame_1,bg=self.color_4,fg=self.color_3)
        self.year_entry.place(x=300,y=130,width=200)

        self.birth=Label(self.frame_1,text='Birth Date',font=(self.font_2,15,'bold'),bg=self.color_1 , fg=self.color_4)
        self.birth.place(x=40,y=170)
        self.birth_entry=Entry(self.frame_1,bg=self.color_4,fg=self.color_3)
        self.birth_entry.place(x=40,y=200,width=200)

        self.contact=Label(self.frame_1,text='Contact No.',font=(self.font_2,15,'bold'),bg=self.color_1 , fg=self.color_4)
        self.contact.place(x=300,y=170)
        self.contact_entry=Entry(self.frame_1,bg=self.color_4,fg=self.color_3)
        self.contact_entry.place(x=300,y=200,width=200)

        self.email=Label(self.frame_1,text='Email Id',font=(self.font_2,15,'bold'),bg=self.color_1 , fg=self.color_4)
        self.email.place(x=40,y=240)
        self.email_entry=Entry(self.frame_1,bg=self.color_4,fg=self.color_3)
        self.email_entry.place(x=40,y=270,width=200)

        self.prn=Label(self.frame_1, text="University PRN", font=(self.font_2,15,'bold'),bg=self.color_1 , fg=self.color_4)
        self.prn.place(x=300,y=240)
        self.prn_entry=Entry(self.frame_1,bg=self.color_4,fg=self.color_3)
        self.prn_entry.place(x=300,y=270,width=200)

        self.age=Label(self.frame_1, text="Age", font=(self.font_2,15,'bold'),bg=self.color_1 , fg=self.color_4)
        self.age.place(x=40,y=310)
        self.age_entry=Entry(self.frame_1, bg=self.color_4,fg=self.color_3)
        self.age_entry.place(x=40,y=340,width=200)

        self.gender=Label(self.frame_1,text="Gender", font=(self.font_2,15,'bold'),bg=self.color_1 , fg=self.color_4)
        self.gender.place(x=300,y=310)
        self.gender_entry=Entry(self.frame_1, bg=self.color_4 , fg=self.color_3) 
        self.gender_entry.place(x=300,y=340,width=200)

        self.submit_bt_1=Button(self.frame_1, text='Submit'  , font=(self.font_2,15,'bold'),command=self.Submit , cursor= 'hand2', bg=self.color_4,bd=2).place(x=220,y=389,width=100)
 
    ''' To get contact number to view data'''
    def GetContact_View(self):
        self.ClearScreen()
        self.getInfo = Label(self.frame_1, text="Enter Phone Number", font=(self.font_2, 18, "bold"), bg=self.color_1 , fg=self.color_4).place(x=140,y=70)
        self.getInfo_entry = Entry(self.frame_1, font=(self.font_1, 12), bg=self.color_4, fg=self.color_3)
        self.getInfo_entry.place(x=163, y=110, width=200, height=30)
        self.submit_bt_2 = Button(self.frame_1, text='Submit', font=(self.font_2, 10,'bold'), bd=2, command=self.CheckContact_View, cursor="hand2", bg=self.color_4,fg=self.color_3).place(x=220,y=150,width=80)
            
    ''' to get contact number to update data'''        
    def GetContact_Update(self):
        self.ClearScreen()
        self.getInfo = Label(self.frame_1, text="Enter Phone Number", font=(self.font_2, 18, "bold"), bg=self.color_1 , fg=self.color_4).place(x=140,y=70)
        self.getInfo_entry = Entry(self.frame_1, font=(self.font_1, 12), bg=self.color_4, fg=self.color_3)
        self.getInfo_entry.place(x=163, y=110, width=200, height=30)
        self.submit_bt_2 = Button(self.frame_1, text='Submit', font=(self.font_2, 10,'bold'), bd=2, command=self.CheckContact_Update, cursor="hand2", bg=self.color_4,fg=self.color_3).place(x=220,y=150,width=80)
            
    ''' to get contact number to delete data'''
    def GetContact_Delete(self):
        self.ClearScreen()

        self.getInfo = Label(self.frame_1, text="Enter Phone Number", font=(self.font_2, 18, "bold"), bg=self.color_1 , fg=self.color_4).place(x=140,y=70)
        self.getInfo_entry = Entry(self.frame_1, font=(self.font_1, 12), bg=self.color_4, fg=self.color_3)
        self.getInfo_entry.place(x=163, y=110, width=200, height=30)
        self.submit_bt_2 = Button(self.frame_1, text='Submit', font=(self.font_2, 10,'bold'), bd=2, command=self.Delete_data, cursor="hand2", bg=self.color_4,fg=self.color_3).place(x=220,y=150,width=80)

    
    '''to remove all widget from frame_1'''
    def ClearScreen(self):
        
        for widget in self.frame_1.winfo_children():
            widget.destroy()
        

    ''' to exit the window'''
    def Exit(self):
        self.window.destroy()

    
    '''
    Checks whether the contact number is available or not. If available, 
    the function calls the 'show_details' function to view the data .
    '''    
    

    def CheckContact_View(self):
        if self.getInfo_entry.get() == "":
            messagebox.showerror("Error!", "Please enter your contact number",parent=self.window)

        else:
            try:
                connection=mysql.connect( host=self.host , user=self.user , password=self.password , database=self.database )
                curs=connection.cursor()
                curs.execute('SELECT * FROM Student_register WHERE contact= %s',(self.getInfo_entry.get(),))
                row=curs.fetchone()

                if row == None:
                    messagebox.showerror("Error!","Contact number doesn't exists",parent=self.window)

                else:
                    self.show_details(row)
                    connection.close
            
            except Exception as e:
                    messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)

    '''
    Checks whether the contact number is available or not. If available, 
    the function calls the 'GetUpdateDetails' function to get the new data to perform
    update operation.
    '''
    def CheckContact_Update(self):
        if self.getInfo_entry.get() == "":
            messagebox.showerror("Error!", "Please enter your contact number",parent=self.window)

        else:
            try:
                connection=mysql.connect( host=self.host , user=self.user , password=self.password , database=self.database )
                curs=connection.cursor()
                curs.execute('SELECT * FROM Student_register WHERE contact= %s',(self.getInfo_entry.get(),))# we are passing the data in a tuple because sql query onlt accept tuple,list as a input
                row=curs.fetchone()

                if row == None:
                    messagebox.showerror("Error!","Contact number doesn't exists",parent=self.window)

                else:
                    self.GetUpdateDetails(row)
                    connection.close
            
            except Exception as e:
                    messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)

    ''' this function takes the details that the user  want to update to perform update operation'''
    def GetUpdateDetails(self, row):
        self.ClearScreen()

        # Create and place labels and entries
        self.name = Label(self.frame_1, text='First name', font=(self.font_2, 15, 'bold'), bg=self.color_1 , fg=self.color_4)
        self.name.place(x=40, y=30)
        self.name_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.name_entry.insert(0, row[0])
        self.name_entry.place(x=40, y=60, width=200)

        self.surname = Label(self.frame_1, text='Last name', font=(self.font_2, 15, 'bold'), bg=self.color_1 , fg=self.color_4)
        self.surname.place(x=300, y=30)
        self.surname_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.surname_entry.insert(0, row[1])
        self.surname_entry.place(x=300, y=60, width=200)

        self.course = Label(self.frame_1, text='Course', font=(self.font_2, 15, 'bold'), bg=self.color_1 ,  fg=self.color_4)
        self.course.place(x=40, y=100)
        self.course_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.course_entry.insert(0, row[2])
        self.course_entry.place(x=40, y=130, width=200)

        self.year = Label(self.frame_1, text='Year', font=(self.font_2, 15, 'bold'), bg=self.color_1 , fg=self.color_4)
        self.year.place(x=300, y=100)
        self.year_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.year_entry.insert(0, row[3])
        self.year_entry.place(x=300, y=130, width=200)

        self.birth = Label(self.frame_1, text='Birth Date', font=(self.font_2, 15, 'bold'), bg=self.color_1 , fg=self.color_4)
        self.birth.place(x=40, y=170)
        self.birth_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.birth_entry.insert(0, row[4])
        self.birth_entry.place(x=40, y=200, width=200)

        self.contact = Label(self.frame_1, text='Contact No.', font=(self.font_2, 15, 'bold'), bg=self.color_1 , fg=self.color_4)
        self.contact.place(x=300, y=170)
        self.contact_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.contact_entry.insert(0, row[5])
        self.contact_entry.place(x=300, y=200, width=200)

        self.email = Label(self.frame_1, text='Email Id', font=(self.font_2, 15, 'bold'), bg=self.color_1 , fg=self.color_4)
        self.email.place(x=40, y=240)
        self.email_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.email_entry.insert(0, row[6])
        self.email_entry.place(x=40, y=270, width=200)

        self.prn = Label(self.frame_1, text="University PRN", font=(self.font_2, 15, 'bold'), bg=self.color_1 , fg=self.color_4)
        self.prn.place(x=300, y=240)
        self.prn_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.prn_entry.insert(0, row[7])
        self.prn_entry.place(x=300, y=270, width=200)

        self.age = Label(self.frame_1, text="Age", font=(self.font_2, 15, 'bold'), bg=self.color_1 , fg=self.color_4)
        self.age.place(x=40, y=310)
        self.age_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.age_entry.insert(0, row[8])
        self.age_entry.place(x=40, y=340, width=200)

        self.gender = Label(self.frame_1, text="Gender", font=(self.font_2, 15, 'bold'), bg=self.color_1 , fg=self.color_4)
        self.gender.place(x=300, y=310)
        self.gender_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.gender_entry.insert(0, row[9])
        self.gender_entry.place(x=300, y=340, width=200)

        self.submit_bt_3 = Button(self.frame_1, text='Submit', font=(self.font_2, 15, 'bold'),
                                command=partial(self.Update_details, row), cursor='hand2', bg=self.color_4, bd=2)
        self.submit_bt_3.place(x=160, y=389, width=100)

        self.cansel_bt_1 = Button(self.frame_1, text='Cancel', font=(self.font_2, 15, 'bold'),
                                command=self.ClearScreen, cursor='hand2', bg=self.color_4, bd=2)
        self.cansel_bt_1.place(x=300, y=389, width=100)


    def Update_details(self, row):

        if (self.name_entry.get() == "" or self.surname_entry.get() == "" or self.course_entry.get() == "" or 
            self.year_entry.get() == "" or self.birth_entry.get() == "" or self.email_entry.get() == "" or 
            self.prn_entry.get() == "" or self.age_entry.get() == "" or self.gender_entry.get() == ""):
            messagebox.showinfo('Error', 'Sorry! All fields are required.', parent=self.window)

        else:
            try:
                connection = mysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
                curs = connection.cursor()

                curs.execute('SELECT * FROM Student_register WHERE contact = %s', (row[5],))
                existing_row = curs.fetchone()

                if existing_row is None:
                    messagebox.showerror("Error", "Contact Number does not exist", parent=self.window)
                else:
                    curs.execute(
                        "UPDATE Student_register SET f_name=%s, l_name=%s, course=%s, year=%s, birth_date=%s, email=%s, prn=%s, age=%s, gender=%s WHERE contact=%s",
                        (
                            self.name_entry.get(),
                            self.surname_entry.get(),
                            self.course_entry.get(),
                            self.year_entry.get(),
                            self.birth_entry.get(),
                            self.email_entry.get(),
                            self.prn_entry.get(),
                            self.age_entry.get(),
                            self.gender_entry.get(),
                            self.contact_entry.get()  # Use the updated contact number for the WHERE clause
                        )
                    )
                    connection.commit()
                    connection.close()
                    messagebox.showinfo('Done!', 'The data has been updated.')
                    self.ClearScreen()

            except Exception as e:
                messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)



    '''this function showing the students details if the mobile number is exit in the database'''
    def show_details(self,row):
        self.ClearScreen()
        self.name = Label(self.frame_1, text='First name', font=(self.font_2, 15, 'bold'), bg=self.color_1 , fg=self.color_4).place(x=40, y=30)
        self.name_data = Label(self.frame_1, text=row[0], font=(self.font_1, 12), bg=self.color_4, fg=self.color_3).place(x=40, y=60, width=200)

        self.surname = Label(self.frame_1, text='Last name', font=(self.font_2, 15, 'bold'), bg=self.color_1 , fg=self.color_4).place(x=300, y=30)
        self.surname_data = Label(self.frame_1, text=row[1], font=(self.font_1, 12), bg=self.color_4, fg=self.color_3).place(x=300, y=60, width=200)

        self.course = Label(self.frame_1, text='Course', font=(self.font_2, 15, 'bold'), bg=self.color_1 , fg=self.color_4).place(x=40, y=100)
        self.course_data = Label(self.frame_1, text=row[2], font=(self.font_1, 12), bg=self.color_4, fg=self.color_3).place(x=40, y=130, width=200)

        self.year = Label(self.frame_1, text='Year', font=(self.font_2, 15, 'bold'), bg=self.color_1 , fg=self.color_4).place(x=300, y=100)
        self.year_data = Label(self.frame_1, text=row[3], font=(self.font_1, 12), bg=self.color_4, fg=self.color_3).place(x=300, y=130, width=200)

        self.birth = Label(self.frame_1, text='Birth Date', font=(self.font_2, 15, 'bold'), bg=self.color_1,fg=self.color_4).place(x=40, y=170)
        self.birth_data = Label(self.frame_1, text=row[4], font=(self.font_1, 12), bg=self.color_4, fg=self.color_3).place(x=40, y=200, width=200)

        self.contact = Label(self.frame_1, text='Contact No.', font=(self.font_2, 15, 'bold'), bg=self.color_1 , fg=self.color_4).place(x=300, y=170)
        self.contact_data = Label(self.frame_1, text=row[5], font=(self.font_1, 12), bg=self.color_4, fg=self.color_3).place(x=300, y=200, width=200)

        self.email = Label(self.frame_1, text='Email Id', font=(self.font_2, 15, 'bold'), bg=self.color_1 , fg=self.color_4).place(x=40, y=240)
        self.email_data = Label(self.frame_1, text=row[6], font=(self.font_1, 12), bg=self.color_4, fg=self.color_3).place(x=40, y=270, width=200)

        self.prn = Label(self.frame_1, text="University PRN", font=(self.font_2, 15, 'bold'), bg=self.color_1 , fg=self.color_4).place(x=300, y=240)
        self.prn_data = Label(self.frame_1, text=row[7], font=(self.font_1, 12), bg=self.color_4, fg=self.color_3).place(x=300, y=270, width=200)

        self.age = Label(self.frame_1, text="Age", font=(self.font_2, 15, 'bold'), bg=self.color_1 , fg=self.color_4).place(x=40, y=310)
        self.age_data = Label(self.frame_1, text=row[8], font=(self.font_1, 12), bg=self.color_4, fg=self.color_3).place(x=40, y=340, width=200)

        self.gender = Label(self.frame_1, text="Gender", font=(self.font_2, 15, 'bold'), bg=self.color_1 , fg=self.color_4).place(x=300, y=310)
        self.gender_data = Label(self.frame_1, text=row[9], font=(self.font_1, 12), bg=self.color_4, fg=self.color_3).place(x=300, y=340, width=200)
        

    def Delete_data(self):
        if self.getInfo_entry.get() == "":
            messagebox.showerror("Error!", "Please enter your contact number",parent=self.window)
        else:
            try:
                connection = mysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
                curs = connection.cursor()
                curs.execute("select * from student_register where contact=%s", (self.getInfo_entry.get(),))
                row=curs.fetchone()
                
                if row == None:
                    messagebox.showerror("Error!","Contact number doesn't exists",parent=self.window)
                else:
                    if messagebox.askyesno('Confirm',"Are you sure to delete the data? "):
                        curs.execute("delete from student_register where contact=%s", (self.getInfo_entry.get(),))

                        connection.commit()
                        messagebox.showinfo('Done!', "The data has been deleted",parent=self.window)
                    else:
                        messagebox.showinfo('Cancelled', "The deletion has been cancelled", parent=self.window)

                    connection.close()
                    self.ClearScreen()
            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)

    def Submit(self):
        if (self.name_entry.get() == "" or
            self.surname_entry.get() == "" or
            self.course_entry.get() == "" or
            self.year_entry.get() == "" or
            self.birth_entry.get() == "" or
            self.email_entry.get() == "" or
            self.prn_entry.get() == "" or
            self.age_entry.get() == "" or
            self.gender_entry.get() == "" or
            self.contact_entry.get() == ""):    

            messagebox.showinfo('Error', 'Sorry! All fields are required.', parent=self.window)
        else:
            try:
                connection = mysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
                curs = connection.cursor()

                # Check if the contact number already exists
                curs.execute('SELECT * FROM Student_register WHERE contact = %s', (self.contact_entry.get(),))
                row = curs.fetchone()

                if row is not None:
                    messagebox.showerror("Error!", "Contact number already exists", parent=self.window)
                else:
                    # Insert new record
                    curs.execute(
                        "INSERT INTO Student_register (f_name, l_name, course, year, birth_date, contact, email, prn, age, gender) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                        (
                            self.name_entry.get(),
                            self.surname_entry.get(),
                            self.course_entry.get(),
                            self.year_entry.get(),
                            self.birth_entry.get(),
                            self.contact_entry.get(),
                            self.email_entry.get(),
                            self.prn_entry.get(),
                            self.age_entry.get(),
                            self.gender_entry.get()
                        )
                    )
                    connection.commit()
                    messagebox.showinfo('Done', "New student has been added successfully", parent=self.window)
                    self.reset_fields()
                    connection.close()

            except Exception as e:
                messagebox.showerror("Error", f"Error due to {str(e)}", parent=self.window)

    ''' when we added new student data it reset the fields '''
    def reset_fields(self):
        self.name_entry.delete(0,END),
        self.surname_entry.delete(0,END),
        self.course_entry.delete(0,END),
        self.birth_entry.delete(0,END),
        self.contact_entry.delete(0,END),
        self.email_entry.delete(0,END),
        self.prn_entry.delete(0,END),
        self.age_entry.delete(0,END),
        self.gender_entry.delete(0,END),
        self.year_entry.delete(0,END),


if __name__ =='__main__':
    root=Tk()
    obj=Management(root)
    root.mainloop()
