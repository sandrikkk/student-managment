import math
import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
import logger
from sql.connection_handler import sql_connection,sql_names

class Students:
    def __init__(self, window):
        self.window = window
        self.window.title("სტუდენტთა შეფასების პროგრამული სისტემა")

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        width = int(screen_width * 0.81)
        height = int(screen_height * 0.75)
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        self.window.geometry(f"{width}x{height}+{x}+{y}")
        self.window.resizable(True, True)

        titlelabel = Label(self.window, text="სტუდენტთა შეფასების პროგრამული სისტემა", font=('Helvetica', 30, 'bold'), bg='#864879',
                           fg='black', bd=5, relief=GROOVE)
        titlelabel.pack(side=TOP, fill=X)

        frame1 = Frame(self.window, bg="#219F94", relief=RIDGE, bd=3)
        frame1.place(relx=0.30, rely=0.1, relwidth=0.7, relheight=0.62)

        frame2 = Frame(self.window, relief=RIDGE, bd=3)
        frame2.place(relx=0.01, rely=0.1, relwidth=0.29, relheight=0.7)

        frame3 = Frame(self.window, bg='#C8F2EF', relief=RIDGE, bd=2)
        frame3.place(relx=0.30, rely=0.715, relwidth=0.70, relheight=0.036)

        frame4 = Frame(self.window, relief=RIDGE, bd=3)
        frame4.place(relx=0.01, rely=0.75, relwidth=0.98, relheight=0.27)

        # ---------------------------------Entry - ის ცვლადები---------------------------------
        self.student_id = StringVar()
        # self.frame1_entry = ttk.Entry(frame1)
        self.saxeli = StringVar()
        self.gvari = StringVar()
        self.kursis_saxeli = StringVar()
        self.qulata_jami = IntVar()
        self.procenti = StringVar()
        self.statusi = StringVar()

        self.python = IntVar()
        self.csharp = IntVar()
        self.cplusplus = IntVar()
        self.java = IntVar()
        self.javascript = IntVar()
        self.inf_usf = IntVar()
        self.qselebi = IntVar()

        # ---------------------------------ღილაკების ლოგიკა--------------------------------------

        # ---------------------------------ინფორმაცია სტუდენტზე---------------------------------
        frame1_label = Label(frame1, text="სტუდენტის ID:", bg="#219F94", font=('cooper black', 15, 'bold'))
        frame1_label.grid(row=0, column=0, padx=0, pady=7, sticky='w')

        frame1_entry = Entry(frame1, bd=5, relief=RIDGE, width=20, textvariable=self.student_id)
        frame1_entry.grid(row=0, column=1, padx=0, pady=5)

        self.frame1_entry = ttk.Entry(frame1)


        frame1_label1 = Label(frame1, text="სახელი:", bg="#219F94", font=('cooper black', 15, 'bold'))
        frame1_label1.grid(row=1, column=0, padx=0, pady=7, sticky='w')
        frame1_entry1 = Entry(frame1, bd=5, relief=RIDGE, width=20, textvariable=self.saxeli)
        frame1_entry1.grid(row=1, column=1, padx=0, pady=5)

        frame1_label2 = Label(frame1, text="გვარი:", bg="#219F94", font=('cooper black', 15, 'bold'))
        frame1_label2.grid(row=2, column=0, padx=0, pady=7, sticky='w')
        frame1_entry2 = Entry(frame1, bd=5, relief=RIDGE, width=20, textvariable=self.gvari)
        frame1_entry2.grid(row=2, column=1, padx=0, pady=5)

        frame1_label3 = Label(frame1, text="მიმართულება:", bg="#219F94", font=('cooper black', 15, 'bold'))
        frame1_label3.grid(row=3, column=0, padx=0, pady=7, sticky='w')
        frame1_combobox = ttk.Combobox(frame1, font=('cooper black', 12, 'bold'), width=25,
                                       textvariable=self.kursis_saxeli)
        frame1_combobox['values'] = ('Software Engieniring', 'Computer Engienering', "Artifical Intelligent")
        frame1_combobox.grid(row=3, column=1, padx=5, pady=5)

        frame1_label4 = Label(frame1, text="ქულათა ჯამი:", bg="#219F94", font=('cooper black', 15, 'bold'))
        frame1_label4.grid(row=4, column=0, padx=0, pady=7, sticky='w')
        frame1_entry4 = Entry(frame1, bd=5, relief=RIDGE, width=20, state=DISABLED, textvariable=self.qulata_jami)
        frame1_entry4.grid(row=4, column=1, padx=0, pady=5)

        frame1_label5 = Label(frame1, text="პროცენტი:", bg="#219F94", font=('cooper black', 15, 'bold'))
        frame1_label5.grid(row=5, column=0, padx=0, pady=6, sticky='w')
        frame1_entry5 = Entry(frame1, bd=5, relief=RIDGE, width=20, state=DISABLED, textvariable=self.procenti)
        frame1_entry5.grid(row=5, column=1, padx=0, pady=5)

        frame1_label6 = Label(frame1, text="სტატუსი:", bg="#219F94", font=('cooper black', 15, 'bold'))
        frame1_label6.grid(row=6, column=0, padx=0, pady=6, sticky='w')
        frame1_entry6 = Entry(frame1, bd=5, relief=RIDGE, width=20, state=DISABLED, textvariable=self.statusi)
        frame1_entry6.grid(row=6, column=1, padx=0, pady=5)

        # ---------------------------------ინფორმაცია საგნებზე---------------------------------
        frame1_label6 = Label(frame1, text="Python :", bg="#219F94", font=('cooper black', 15, 'bold'))
        frame1_label6.grid(row=0, column=2, padx=40, pady=10, sticky='w')
        frame1_entry6 = Entry(frame1, bd=5, relief=RIDGE, width=20, textvariable=self.python)
        frame1_entry6.grid(row=0, column=3, padx=10, pady=5)

        frame1_label7 = Label(frame1, text="C#:", bg="#219F94", font=('cooper black', 15, 'bold'))
        frame1_label7.grid(row=1, column=2, padx=40, pady=10, sticky='w')
        frame1_entry7 = Entry(frame1, bd=5, relief=RIDGE, width=20, textvariable=self.csharp)
        frame1_entry7.grid(row=1, column=3, padx=10, pady=5)

        frame1_label8 = Label(frame1, text="Java:", bg="#219F94", font=('cooper black', 15, 'bold'))
        frame1_label8.grid(row=2, column=2, padx=40, pady=10, sticky='w')
        frame1_entry8 = Entry(frame1, bd=5, relief=RIDGE, width=20, textvariable=self.java)
        frame1_entry8.grid(row=2, column=3, padx=10, pady=5)

        frame1_label9 = Label(frame1, text="C++:", bg="#219F94", font=('cooper black', 15, 'bold'))
        frame1_label9.grid(row=3, column=2, padx=40, pady=10, sticky='w')
        frame1_entry9 = Entry(frame1, bd=5, relief=RIDGE, width=20, textvariable=self.javascript)
        frame1_entry9.grid(row=3, column=3, padx=10, pady=5)

        frame1_label10 = Label(frame1, text="JavaScript:", bg="#219F94", font=('cooper black', 15, 'bold'))
        frame1_label10.grid(row=4, column=2, padx=40, pady=6, sticky='w')
        frame1_entry10 = Entry(frame1, bd=5, relief=RIDGE, width=20, textvariable=self.cplusplus)
        frame1_entry10.grid(row=4, column=3, padx=10, pady=5)

        frame1_label11 = Label(frame1, text="კომპ.ქსელები:", bg="#219F94", font=('cooper black', 15, 'bold'))
        frame1_label11.grid(row=5, column=2, padx=40, pady=6, sticky='w')
        frame1_entry11 = Entry(frame1, bd=5, relief=RIDGE, width=20, textvariable=self.qselebi)
        frame1_entry11.grid(row=5, column=3, padx=10, pady=5)

        frame1_label12 = Label(frame1, text="ინფ. უსაფ:", bg="#219F94", font=('cooper black', 15, 'bold'))
        frame1_label12.grid(row=6, column=2, padx=40, pady=10, sticky='w')
        frame1_entry12 = Entry(frame1, bd=5, relief=RIDGE, width=20, textvariable=self.inf_usf)
        frame1_entry12.grid(row=6, column=3, padx=10, pady=5)

        # Configure grid row and column weights to make the frame responsive
        frame1.grid_rowconfigure(0, weight=1)
        frame1.grid_rowconfigure(1, weight=1)
        frame1.grid_rowconfigure(2, weight=1)
        frame1.grid_rowconfigure(3, weight=1)
        frame1.grid_rowconfigure(4, weight=1)
        frame1.grid_rowconfigure(5, weight=1)
        frame1.grid_rowconfigure(6, weight=1)
        frame1.grid_columnconfigure(0, weight=1)
        frame1.grid_columnconfigure(1, weight=1)
        frame1.grid_columnconfigure(2, weight=1)
        frame1.grid_columnconfigure(3, weight=1)

        # --------------------------------
        # frame2 - ის კომპონენტებზე მუშაობა
        # --------------------------------
        frame2_label = Label(frame2, text="სტუდენტის შედეგები", font='arial 15 bold', fg='black', relief=GROOVE, bd=5)
        frame2_label.grid(row=0, column=0, sticky='ew')

        frame2_scroll = Scrollbar(frame2, orient=VERTICAL)
        frame2_scroll.grid(row=1, column=1, sticky='ns')

        self.textarea = Text(frame2, font='arial 12 bold', yscrollcommand=frame2_scroll.set)
        self.textarea.grid(row=1, column=0, sticky='nsew')

        frame2_scroll.config(command=self.textarea.yview)

        # Configure grid row and column weights to make the frame responsive
        frame2.grid_rowconfigure(0, weight=0)
        frame2.grid_rowconfigure(1, weight=1)
        frame2.grid_columnconfigure(0, weight=1)

        # --------------------------------
        # frame3 - ის კომპონენტებზე მუშაობა
        # --------------------------------
        frame3_button = Button(frame3, text='შედეგის შექმნა', font='arial 11 bold', bg="#D1D1D1", fg="black",
                               command=self.bazashidamateba)
        frame3_button.grid(row=0, column=0, padx=40, sticky='ew')

        frame3_button1 = Button(frame3, text='შედეგის განახლება', font='arial 11 bold', bg="#D1D1D1", fg="black",
                                command=self.updatebtn)
        frame3_button1.grid(row=0, column=1, sticky='ew')

        frame3_button2 = Button(frame3, text='გასუფთავება', font='arial 11 bold', bg="#D1D1D1", fg="black",
                                command=self.gasuftaveba)
        frame3_button2.grid(row=0, column=2, padx=40, sticky='ew')

        frame3_button3 = Button(frame3, text='შედეგის წაშლა', font='arial 11 bold', bg="#D1D1D1", fg="black",
                                command=self.delete)
        frame3_button3.grid(row=0, column=3, sticky='ew')

        frame3_button4 = Button(frame3, text='დახურვა', font='arial 11 bold', bg="#D1D1D1", fg="black",
                                command=self.daxurva)
        frame3_button4.grid(row=0, column=4, padx=40, sticky='ew')

        # Configure column weight to make the buttons responsive
        frame3.grid_columnconfigure(0, weight=1)
        frame3.grid_columnconfigure(1, weight=1)
        frame3.grid_columnconfigure(2, weight=1)
        frame3.grid_columnconfigure(3, weight=1)
        frame3.grid_columnconfigure(4, weight=1)

        # --------------------------------
        # frame4 - ის კომპონენტებზე მუშაობა
        # --------------------------------
        frame3_scroll = Scrollbar(frame4, orient=VERTICAL)
        frame3_scroll.grid(row=0, column=1, sticky=N + S)

        self.studentis_cxrili = ttk.Treeview(frame4, columns=(
            'სტუდენტის ID', 'კურსის სახელი', 'Python', 'C#', 'Java', 'JavaScript', "C++",
            'ინფ. უსაფ', "კომპ.ქსელები", 'ქულათა ჯამი', 'პროცენტი', "სტატუსი"
        ))
        self.studentis_cxrili.heading('სტუდენტის ID', text='სტუდენტის ID')
        self.studentis_cxrili.heading('კურსის სახელი', text='კურსის სახელი')
        self.studentis_cxrili.heading('Python', text='Python')
        self.studentis_cxrili.heading('C#', text='C#')
        self.studentis_cxrili.heading('Java', text='Java')
        self.studentis_cxrili.heading('JavaScript', text='JavaScript')
        self.studentis_cxrili.heading('C++', text='C++')
        self.studentis_cxrili.heading('ინფ. უსაფ', text='ინფ. უსაფ')
        self.studentis_cxrili.heading('კომპ.ქსელები', text='კომპ.ქსელები')
        self.studentis_cxrili.heading('სტატუსი', text='სტატუსი')
        self.studentis_cxrili.heading('ქულათა ჯამი', text='ქულათა ჯამი')
        self.studentis_cxrili.heading('პროცენტი', text='პროცენტი')
        self.studentis_cxrili['show'] = 'headings'

        # Set width and anchor for each column
        column_width = 100  # Adjust the value as needed
        columns = ['სტუდენტის ID', 'კურსის სახელი', 'Python', 'C#', 'Java',
                   'JavaScript', 'C++', 'ინფ. უსაფ', 'კომპ.ქსელები', 'ქულათა ჯამი',
                   'პროცენტი', 'სტატუსი']

        for column in columns:
            self.studentis_cxrili.column(column, width=column_width, anchor='center')

        self.studentis_cxrili.grid(row=0, column=0, sticky=N + S + E + W)

        frame4.grid_rowconfigure(0, weight=1)
        frame4.grid_columnconfigure(0, weight=1)

        frame3_scroll.config(command=self.studentis_cxrili.yview)

        self.studentis_cxrili.bind("<ButtonRelease-1>", self.ganaxleba)
        self.DataGamotana()

    def check_subjects(self, integer_fields):
        field_names = []
        for subject, field_value in integer_fields.items():
            value = int(field_value.get())
            if value < 51:
                field_names.append(subject)
                self.statusi.set(f"Fail in {subject}")

        if field_names:
            subjects_str = ", ".join(field_names)
            self.statusi.set(f"Fail in {subjects_str}")
        else:
            self.statusi.set("Pass")
        return self.statusi.get()

    def jami(self):
        integer_fields = {"Python": self.python,
                          "C#": self.csharp,
                          "Java": self.java,
                          "JavaScript": self.javascript,
                          "C++": self.cplusplus,
                          "Information Security": self.inf_usf,
                          "Q-selebi": self.qselebi}

        jami = (self.python.get() +
                self.csharp.get() +
                self.java.get() +
                self.javascript.get() +
                self.cplusplus.get() +
                self.inf_usf.get() +
                self.qselebi.get())

        procenti = (jami / 700) * 100
        procenti = math.floor(procenti)

        self.check_subjects(integer_fields)

        self.qulata_jami.set(str(jami))
        self.procenti.set(str(procenti) + "%")

    def bazashidamateba(self):
        self.frame1_entry.config(state=NORMAL)

        fields = [
            self.student_id.get(),
            self.kursis_saxeli.get(),
            self.python.get(),
            self.csharp.get(),
            self.java.get(),
            self.javascript.get(),
            self.cplusplus.get(),
            self.qselebi.get(),
            self.inf_usf.get()
        ]

        student_id = self.student_id.get()

        try:
            integer_field = int(student_id)
        except ValueError:
            tkinter.messagebox.showerror("Error", "ID უნდა იყოს მთელი რიცხვი!")
            return
        if any(field == "" for field in fields):
            tkinter.messagebox.showerror("Error", "გთხოვთ შეავსოთ ყველა ველი.")
        elif any(int(field) > 100 for field in fields[2:]):
            tkinter.messagebox.showerror("Error", "ქულის ველი არ უნდა აღემადებოდეს 100-ს !")

        else:
            self.jami()
            # self.shedegi()
            connect = sql_connection()
            cur = connect.cursor()
            cur.execute("SELECT * FROM students")
            rows = cur.fetchall()
            for row in rows:
                if row[0] == student_id:
                    tkinter.messagebox.showerror('Error', "დაფიქსირდა ერთნაირი ID !")
                    connect.close()
                    return
            self.shedegi()
            cur.execute("INSERT INTO students VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                student_id,
                self.kursis_saxeli.get(),
                self.python.get(),
                self.csharp.get(),
                self.java.get(),
                self.javascript.get(),
                self.cplusplus.get(),
                self.inf_usf.get(),
                self.qselebi.get(),
                self.qulata_jami.get(),
                self.procenti.get(),
                self.statusi.get(),
                self.saxeli.get(),
                self.gvari.get()
            ))
            connect.commit()
            self.DataGamotana()
            connect.close()
            self.gasuftaveba()

    def daxurva(self):
        daxurva = tkinter.messagebox.askyesno("გასვლა გსურთ?", "გრურთ პროგრამის დახურვა ?")
        if daxurva:
            self.window.destroy()

    def gasuftaveba(self):
        self.frame1_entry.config(state=NORMAL)
        self.student_id.set("")
        self.saxeli.set("")
        self.gvari.set("")
        self.kursis_saxeli.set("")
        self.qulata_jami.set("")
        self.procenti.set("")
        self.statusi.set("")
        self.python.set("")
        self.csharp.set("")
        self.cplusplus.set("")
        self.java.set("")
        self.javascript.set("")
        self.inf_usf.set("")
        self.qselebi.set("")

    def cleartextarea(self):
        self.textarea.delete("1.0", END)

    def DataGamotana(self):
        connect = sql_connection()
        cur = connect.cursor()
        cur.execute("Select * from students")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.studentis_cxrili.delete(*self.studentis_cxrili.get_children())
            for row in rows:
                self.studentis_cxrili.insert('', END, values=row)
            connect.commit()
        connect.close()

    def shedegi(self):
        self.textarea.insert(END, '\n\n************************************************')
        self.textarea.insert(END, f"\n სტუდენტის ID: \t\t {self.student_id.get()}")
        self.textarea.insert(END, f"\n სტუდენტის სახელი: \t\t {self.saxeli.get()}")
        self.textarea.insert(END, f"\n სტუდენტი: \t\t {self.saxeli.get()} {self.gvari.get()}")
        self.textarea.insert(END, f"\n კურსის სახელი: \t\t {self.kursis_saxeli.get()}")
        self.textarea.insert(END, f"\n Python: \t\t {self.python.get()}")
        self.textarea.insert(END, f"\n C#: \t\t {self.csharp.get()}")
        self.textarea.insert(END, f"\n Java: \t\t {self.java.get()}")
        self.textarea.insert(END, f"\n JavaScript: \t\t {self.javascript.get()}")
        self.textarea.insert(END, f"\n C++: \t\t {self.cplusplus.get()}")
        self.textarea.insert(END, f"\n ინფორმაციული უსაფრთხოება: \t\t {self.inf_usf.get()}")
        self.textarea.insert(END, f"\n ქსელები: \t\t {self.qselebi.get()}")
        self.textarea.insert(END, f"\n სტატუსი: \t {self.statusi.get()}")
        self.textarea.insert(END, '\n\n================================')
        self.textarea.insert(END, f"\n ქულათა ჯამი: \t\t {self.qulata_jami.get()}")
        self.textarea.insert(END, f"\n ქულათა პროცენტი: \t\t {self.procenti.get()}")
        self.textarea.insert(END, '\n\n================================')
        self.textarea.insert(END, '\n\n************************************************')

        logger.write_log(self)



    def delete(self):
        if self.student_id.get() == "":
            messagebox.showerror("Error", 'გთხოვთ შემოიტანოთ წასაშლელი Student-ის ID')
        else:
            connect = sql_connection()
            cur = connect.cursor()
            cur.execute("DELETE FROM students WHERE student_id=%s", self.student_id.get())
            connect.commit()
            connect.close()
            self.DataGamotana()

    def ganaxleba(self, event):
        ganaxleba = self.studentis_cxrili.focus()
        content = self.studentis_cxrili.item(ganaxleba)
        row = content['values']
        self.student_id.set(row[0])
        self.kursis_saxeli.set(row[1])
        self.python.set(row[2])
        self.csharp.set(row[3])
        self.java.set(row[4])
        self.cplusplus.set(row[5])
        self.javascript.set(row[6])
        self.inf_usf.set(row[7])
        self.qselebi.set(row[8])
        self.qulata_jami.set(row[9])
        self.procenti.set(row[10])
        self.statusi.set(row[11])
        self.saxeli.set(row[12])
        self.gvari.set(row[13])

        # Hide the entry box

        self.frame1_entry.config(state=DISABLED, textvariable=self.student_id)
        self.frame1_entry.grid(row=0, column=1, padx=0, pady=5)

    def updatebtn(self):
        self.frame1_entry.config(state=NORMAL)

        # Establish a connection to the MySQL database
        connect = sql_connection()
        # Create a cursor object to execute SQL queries
        cursor = connect.cursor()

        integer_fields = {
            "Python": self.python,
            "C#": self.csharp,
            "Java": self.java,
            "JavaScript": self.javascript,
            "C++": self.cplusplus,
            "Information Security": self.inf_usf,
            "Q-selebi": self.qselebi
        }
        a = self.check_subjects(integer_fields)
        self.statusi.set(a)
        # Get the values from the entry-boxes
        student_id = self.student_id.get()
        kursis_saxeli = self.kursis_saxeli.get()
        python = self.python.get()
        csharp = self.csharp.get()
        java = self.java.get()
        javascript = self.javascript.get()
        cplusplus = self.cplusplus.get()
        inf_usf = self.inf_usf.get()
        qselebi = self.qselebi.get()
        qulata_jami = self.qulata_jami.get()
        procenti = self.procenti.get()
        statusi = self.statusi.get()
        saxeli = self.saxeli.get()
        gvari = self.gvari.get()

        query = """
        UPDATE students SET
        kursis_saxeli = %s,
        python = %s,
        csharp = %s,
        java = %s,
        javascript = %s,
        cplusplus = %s,
        inf_usf = %s,
        qselebi = %s,
        qulata_jami = %s,
        procenti = %s,
        statusi = %s,
        saxeli = %s,
        gvari = %s
        WHERE student_id = %s
        """

        values = (
            kursis_saxeli, python, csharp, java, javascript, cplusplus,
            inf_usf, qselebi, qulata_jami, procenti, statusi, saxeli, gvari, student_id
        )
        cursor.execute(query, values)

        connect.commit()

        cursor.close()
        connect.close()
        logger.write_log(self,is_update=True)
        # Update other fields
        self.qulata_jami.set(str(qulata_jami))
        self.procenti.set(str(procenti) + "%")

        self.DataGamotana()
        self.gasuftaveba()

        print("Record updated successfully!")


window = Tk()
student = Students(window)
window.mainloop()
