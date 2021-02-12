import mysql.connector as mysql
from tkinter import *
from tkinter import messagebox
import hashlib
import random


#===================================================== class start ==================================================================

class StartWindow:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1350x750+0+0")
        self.master.title("Quiz App")
        self.master.wm_iconbitmap('..\Quiz_App\Resources/app.ico')
        self.master.config(bg="#009FBF")

        f0=Frame(self.master, height=1080, width=1920, bg="#C3FDB8", relief="ridge", bd=10)
        f0.propagate(0)
        f0.pack()
        self.man= PhotoImage(file="..\Quiz_App\Resources/front.png")        
        imgman=Label(f0, image=self.man, bg="#C3FDB8", height=620, width=1325).place(x=0,y=0)

        self.start = Button(f0, text="START", width=107, height=2, fg="WHITE", bg="#4CC552",
                            font=("Times New Roman", 16, "bold italic"), command=self.f_start).place(x=17, y=643)

    def f_start(self):
        self.newWindow = Toplevel(self.master)
        self.newWindow.resizable(0, 0)
        self.app = MainWindow(self.newWindow)


#================================ class mainwindow ====================================================================================
class MainWindow:

    def __init__(self, master):
        self.master = master
        self.master.geometry("1350x750+0+0")
        self.master.title("Quiz App")
        self.master.wm_iconbitmap('..\Quiz_App\Resources/app.ico')
        self.master.config(bg="#009FBF")

        f=Frame(self.master, height=1080, width=1920, bg="#C3FDB8", relief="ridge", bd=10)
        f.propagate(0)
        f.pack()
        self.man= PhotoImage(file="..\Quiz_App\Resources\imag.png")
        imgman=Label(f, image=self.man, bg="#C3FDB8").place(x=100,y=20)


        self.mainTitle= Label(f, text="THE MIND-BLOWING & ASTONISHING QUIZ", fg="#FF2400", bg="#C3FDB8", font=("Algerian", 25, "bold italic")).place(x=540, y=220)
        self.regis=Button(f, text="Register", width=18, height=4, fg="royalblue4", bg="lavender", font=("Helvetica",11,"bold italic"), command=self.f_reg).place(x=680, y=400)
        self.login=Button(f, text="Login", height=4, width=18, fg="royalblue4", bg="lavender", font=("Helvetica",11,"bold italic"),command=self.f_login).place(x=920, y=400)

    def f_reg(self):
            self.newWindow = Toplevel(self.master)
            self.newWindow.resizable(0, 0)
            self.app = Register(self.newWindow)

    def f_login(self):
            self.login = Toplevel(self.master)
            self.login.resizable(0, 0)
            self.log = Login(self.login)

#==================================class Register===================================================================================

class Register:

    def __init__(self, master):
        global mReg
        mReg = master
        self.master = master
        self.master.geometry("1350x750+0+0")
        self.master.title("Quiz App - Registration")
        self.master.wm_iconbitmap('..\Quiz_App\Resources/app.ico')
        self.master.config(bg="#C3FDB8")
        global f1
        f1 = Frame(self.master, height=1080, width=1920, bg="#C3FDB8", relief="ridge", bd=10)
        f1.propagate(0)
        f1.pack()

        self.regNow = PhotoImage(file="..\Quiz_App\Resources/RegisterNow.png")
        imgRegNow = Label(f1, image=self.regNow, bg="#C3FDB8").place(x=620, y=5)

        self.mainTitle = Label(f1, text="Register Yourself Here", bg="#C3FDB8", fg="brown",font=("Times New Roman", 30, "bold italic underline")).place(x=50, y=10)
        self.name = Label(f1, text="First Name : ", bg="#C3FDB8", font=("Times New Roman", 11, "bold"))
        self.lname = Label(f1, text="Last Name : ", bg="#C3FDB8", font=("Times New Roman", 11, "bold"))
        self.email = Label(f1, text="Email ID : ", bg="#C3FDB8", font=("Times New Roman", 11, "bold"))
        self.uname = Label(f1, text="Username : ", bg="#C3FDB8", font=("Times New Roman", 11, "bold"))
        self.pw = Label(f1, text="Enter Password : ", bg="#C3FDB8", font=("Times New Roman", 11, "bold"))

        self.var = IntVar()

        self.tname = Entry(f1, width=30)
        self.tlname = Entry(f1, width=30)
        self.temail = Entry(f1, width=30)
        self.tuname = Entry(f1, width=30)
        self.tpw = Entry(f1, width=30, show="*")

        self.submit = Button(f1, text="Submit", width=17, height=4, fg="royalblue4", bg="lavender",
                             font=("Helvetica", 11, "bold italic"), command=self.c_submit)
        self.cancel = Button(f1, text="Cancel", width=17, height=4, fg="royalblue4", bg="lavender",
                             font=("Helvetica", 11, "bold italic"), command=self.c_cancel)

        self.checkB = Checkbutton(f1, text='Show Password', bg="#C3FDB8", fg="royalblue4",
                                  font=("Helvetica", 11, "bold italic"), variable=self.var, onvalue=1,
                                  offvalue=0, command=self.Showpasswd)

#=====================button, textbox, label position================================================================

        self.name.place(x=50, y=100)
        self.tname.place(x=200, y=100)
        self.lname.place(x=50, y=150)
        self.tlname.place(x=200, y=150)
        self.email.place(x=50, y=200)
        self.temail.place(x=200, y=200)
        self.uname.place(x=50, y=250)
        self.tuname.place(x=200, y=250)
        self.pw.place(x=50, y=300)
        self.tpw.place(x=200, y=300)
        self.submit.place(x=50, y=420)
        self.cancel.place(x=250, y=420)
        self.checkB.place(x=195, y=330)
#======================================================================================================================

    def Showpasswd(self):
        if (self.var.get()):
            self.tpw.config(show="")
        else:
            self.tpw.config(show="*")


    def check(self, l1):
        ht = 50
        f = 0
        s = 0
        for i in range(5):
            ht = ht + 50
            if len(l1[i]) == 0:
                self.l = Label(f1, text="! You cannot leave this empty", fg='red', bg="#C3FDB8")
                self.l.place(x=400, y=ht)
            else:
                self.l = Label(f1, text="! You cannot leave this empty", bg="#C3FDB8", fg="#C3FDB8")
                self.l.place(x=400, y=ht)
                f = f + 1
        if (l1[2].find("@" and ".")== -1 and  len(l1[2]) != 0):
            self.l = Label(f1, text="! Please enter a valid email id", bg="#C3FDB8", fg="red")
            self.l.place(x=400, y=200)
            s = 1
        elif (len(l1[2]) > 0):
            self.l = Label(f1, text="! Please enter a valid email id", bg="#C3FDB8", fg="#C3FDB8")
            self.l.place(x=400, y=200)
        if len(l1[4]) < 5 and len(l1[4]) != 0:
            self.l = Label(f1, text="! Password must atleast have 5 characters", bg="#C3FDB8", fg="red")
            self.l.place(x=400, y=300)
        elif (len(l1[4]) > 0):
            self.l = Label(f1, text="! Password must atleast have 5 characters", bg="#C3FDB8", fg="#C3FDB8")
            self.l.place(x=400, y=300)
        if (f == 5 and len(l1[4]) >= 5 and s == 0):
            return 1
        else:
            return 0

        

    def c_submit(self):
        conn = mysql.connect(host='localhost', database='quizdb', user='root', password='12345')
        cursor = conn.cursor()
        name = self.tname.get()
        lname = self.tlname.get()
        email = self.temail.get()
        uname = self.tuname.get()
        pw = self.tpw.get()
        p = hashlib.sha1((uname[:5] + pw).encode('utf-8')).hexdigest()
        l1 = [name, lname, email, uname, pw]
        c = self.check(l1)
        if c == 1:
            str = "select * from reg where uname='%s'"
            val = (uname)
            cursor.execute(str % val)
            row = cursor.fetchone()
            if row is not None:
                self.l = Label(f1, text="Username Already Taken, Try Another!", bg="#C3FDB8", fg="red")
                self.l.place(x=400, y=250)
                
            else:
                try:
                    s = "insert into reg(name,lname,email,uname,p,score) values('%s','%s','%s','%s','%s','%d')"
                    val= (name, lname, email, uname, p, 0)
                    cursor.execute(s % val)
                    conn.commit()
                    print("DEBUG: 1 ROW ADDED")
                    self.tname.delete(0, 'end')
                    self.tlname.delete(0, 'end')
                    self.temail.delete(0, 'end')
                    self.tuname.delete(0, 'end')
                    self.tpw.delete(0, 'end')
                    messagebox.showinfo("Success", "Registration Successful!")
                    
#========================================================================================================                    
                    self.newWindow = Toplevel(self.master)
                    self.newWindow.resizable(0, 0)
                    self.app = MainWindow(self.newWindow)
#========================================================================================================
                    
                except:
                    conn.rollback()
        
        cursor.close()
        conn.close()
        

    def c_cancel(self):
        mReg.destroy()

#=======================================class login ==============================================================================
class Login:
    def __init__(self,master):
        global mLogin
        mLogin= master
        self.master=master
        self.master.geometry("1350x750+0+0")
        self.master.title("Quiz App - Login")
        self.master.wm_iconbitmap('..\Quiz_App\Resources/app.ico')
        self.master.config(bg="#009FBF")

        global f2
        f2=Frame(self.master, height=1080, width=1920, bg="#C3FDB8", relief="ridge", bd=10)
        f2.propagate(0)
        f2.pack()

        self.log = PhotoImage(file="..\Quiz_App\Resources/log.png")
        imgLog = Label(f2, image=self.log, bg="#C3FDB8").place(x=750, y=100)

        self.l1 = Label(f2, text="Enter Username :", bg="#C3FDB8", font=("Times New Roman", 20))
        self.l2 = Label(f2, text="Enter Password :", bg="#C3FDB8", font=("Times New Roman", 20))

        self.e1 = Entry(f2, width=30)
        self.e2 = Entry(f2, width=30, show="*")

        self.b1= Button(f2, text="Login", width=15, height=3, fg="royalblue4", bg="lavender",font=("Helvetica", 11, "bold italic"), command=self.clicked)
        self.b2= Button(f2, text="Cancel", width=15, height=3, fg="royalblue4", bg="lavender",font=("Helvetica", 11, "bold italic"), command=self.cancelLogin)

        self.var = IntVar()
        self.checkB = Checkbutton(f2, text='Show Password', bg="#C3FDB8", fg="royalblue4",
                                  font=("Helvetica", 11, "bold italic"), variable=self.var, onvalue=1,
                                  offvalue=0, command=self.Showpasswd)

        self.l1.place(x=100, y=180)
        self.e1.place(x=310, y=190)
        self.l2.place(x=100, y=230)
        self.e2.place(x=310, y=240)
        self.b1.place(x=130, y=340)
        self.b2.place(x=310, y=340)
        self.checkB.place(x=305, y=270)

    def Showpasswd(self):
        if (self.var.get()):
            self.e2.config(show="")
        else:
            self.e2.config(show="*")

    def cancelLogin(self):
        mLogin.destroy()
        

    def clicked(self):
        conn = mysql.connect(host='localhost', database='quizdb', user='root', password='12345')
        cursor = conn.cursor()
        u = self.e1.get()
        pw = self.e2.get()
        self.e1.delete(0, 200)
        self.e2.delete(0, 200)
        p = hashlib.sha1((u[:5] + pw).encode('utf-8')).hexdigest()
        s = "select * from reg where uname='%s' and p='%s'"
        val = (u, p)
        cursor.execute(s % val)
        result = cursor.fetchall()
        if result:
            self.goinaccount(u)
        else:
            messagebox.showerror("Error", "Invalid Username or Password, Try Again!")
#================================================================================================
            self.newWindow = Toplevel(self.master)
            self.newWindow.resizable(0, 0)
            self.app = Login(self.newWindow)
#================================================================================================            
        cursor.close()
        conn.close()

    def goinaccount(self, u):
        self.accWindow = Toplevel(mLogin)
        self.accWindow.resizable(0, 0)
        self.acWin = Account(self.accWindow, u)

#===============================Account ========================================================================
class Account:

    def __init__(self, master, u):
        global mAcc
        self.u = u
        self.master = master
        mAcc = master
        self.master.geometry("1350x750+0+0")
        self.master.title("Quiz App - Welcome")
        self.master.wm_iconbitmap('..\Quiz_App\Resources/app.ico')
        self.master.config(bg="#009FBF")
        f3 = Frame(mAcc, height=1080, width=1920, bg="#C3FDB8", relief="ridge", bd=10)
        f3.propagate(0)
        f3.pack()
        conn = mysql.connect(host='localhost', database='quizdb', user='root', password='12345')
        cursor = conn.cursor()
        q = "select score from reg where uname='%s'"
        val = (u)
        cursor.execute(q % val)
        self.prevScore = cursor.fetchone()
        cursor.close()
        conn.close()
        
        self.greet = Label(f3, text="Hey " + u + ", Welcome Back!!!", bg="#C3FDB8",fg="brown", font=("Helvetica", 30, "bold italic")).place(x=100, y=200)
        self.lastScore = Label(f3, text="Your Last Quiz Score = " + str(self.prevScore[0]), bg="#C3FDB8", font=("Helvetica", 30, "bold italic")).place(x=100, y=300)
        self.takeQuiz = Button(f3, text="Take Quiz", width=20, height=5, fg="royalblue4", bg="lavender", font=("Helvetica", 11, "bold italic"), command=self.goinside)
        self.takeQuiz.place(x=140, y=430)
        self.logout = Button(f3, text="Logout", width=20, height=5, fg="royalblue4", bg="lavender", font=("Helvetica", 11, "bold italic"), command=self.logout)
        self.logout.place(x=390, y=430)

        self.grt = PhotoImage(file="..\Quiz_App\Resources/es.png")
        imgGrt = Label(f3, image=self.grt, bg="#C3FDB8").place(x=800, y=100)
        

    def goinside(self):
        self.quizWindow = Toplevel(self.master)
        self.quizWindow.resizable(0, 0)
        self.qw = Quiz(self.quizWindow, self.u)

    def logout(self):
        mAcc.destroy()


#=============================== class Quiz ===================================================================================
class Quiz:
    def __init__(self, master, u):
        self.user = u
        global mQuiz
        mQuiz = master
        self.master = master
        self.master.geometry("1350x750+0+0")
        self.master.title("Quiz App - Questions")
        self.master.wm_iconbitmap('..\Quiz_App\Resources/app.ico')
        self.master.config(bg="#C3FDB8")
        global f
        f = Frame(self.master, height=1080, width=1920, bg="#C3FDB8", relief="ridge", bd=10)
        conn = mysql.connect(host='localhost', database='quizdb', user='root', password='12345')
        cursor = conn.cursor()

        global l1, answerstemp
        global questions
        questions = []
        global options
        options = []
        global answers
        answers = []
        answerstemp = []
        s1 = set()

        while len(s1) < 10:
            strQ = ""
            strA = ""
            id = random.randint(1, 30)
            s1.add(id)

        while len(s1) > 0:
            s = "select qstn from questions where QID=%d"
            id = s1.pop()
            val = (id)
            cursor.execute(s % val)
            strQ = strQ.join(list(cursor.fetchone()))
            questions.append(strQ)

            s = "select opA,opB,opC,opD from questions where QID=%d"
            val = (id)
            cursor.execute(s % val)
            options.append(list(cursor.fetchone()))

            s = "select ans from questions where QID=%d"
            val = (id)
            cursor.execute(s % val)
            l = list(cursor.fetchone())
            answerstemp.append(l)

        mydict = {}
        for i in range(10):
            mydict[questions[i]] = options[i]
        for i in range(len(answerstemp)):
            answers.append(answerstemp[i][0])

        print("DEBUG: Answers= ", answers)

        cursor.close()
        conn.close()
        l1 = {}
        for i in range(10):
            l1[i] = 0

        f.propagate(0)
        f.pack()
        self.qno = 0
        self.score1 = 0
        self.ques = self.create_q(f, self.qno)
        self.opts = self.create_options(f)
        self.display_q(self.qno)
        self.Back = Button(f, text="<-- Previous", width=15, height=3, fg="royalblue4", bg="snow2", font=("Helvetica", 11, "bold italic"), command=self.back).place(x=90, y=325)
        self.Next = Button(f, text="Next -->", width=15, height=3, fg="royalblue4", bg="snow2", font=("Helvetica", 11, "bold italic"), command=self.next).place(x=260, y=325)
        self.submit = Button(f, text="Submit", width=34, height=2, fg="ghost white", bg="DeepSkyBlue2", font=("Helvetica", 11, "bold italic"), command=self.submit).place(x=90, y=450)

        self.fin = PhotoImage(file="..\Quiz_App\Resources/qz.png")
        imgFin = Label(f, image=self.fin, bg="#C3FDB8").place(x=800, y=200)

    def create_q(self, master, qno):
        qLabel = Label(master, text=questions[qno], bg='#C3FDB8', font=("Times New Roman", 20))
        qLabel.place(x=30, y=70)
        return qLabel

    def create_options(self, master):
        b_val = 0
        b = []
        ht = 85
        self.opt_selected = IntVar()
        while b_val < 4:
            btn = Radiobutton(master, text="", variable=self.opt_selected, value=b_val + 1, bg='#C3FDB8', font=("Times New Roman", 20))
            b.append(btn)
            ht = ht + 40
            btn.place(x=30, y=ht)
            b_val = b_val + 1
        return b

    def display_q(self, qno):
        b_val = 0
        self.ques['text'] = str(qno + 1) + ". " + questions[qno]
        for op in options[qno]:
            self.opts[b_val]['text'] = op
            b_val = b_val + 1

    def next(self):
        self.qno += 1

        if self.qno >= len(questions):
            self.qno -= 1
            lw = Label(f, text="Warning, You are at the end. Press Submit.", fg='red', bg="#C3FDB8", font=("Times New Roman", 15))
            lw.place(x=90, y=560)
            return lw
            
        else:
            l1[self.qno - 1] = self.opt_selected.get()
            self.opt_selected.set(l1[(self.qno)])
            self.display_q(self.qno)
            lw = Label(f, text="Warning, You are at the end. Press Submit.", fg='#C3FDB8', bg="#C3FDB8",
                       font=("Times New Roman", 15))
            lw.place(x=90, y=560)
            return lw

    def back(self):
        l1[self.qno] = self.opt_selected.get()
        self.qno -= 1
        if self.qno < 0:
            self.qno += 1
            lw2 = Label(f, text="Error, You are already in the start!!!", fg='red', bg="#C3FDB8", font=("Times New Roman", 17))
            lw2.place(x=90, y=560)
            return lw2

        else:
            self.display_q(self.qno)
            c = l1[self.qno]
            self.opt_selected.set(c)
            lw2 = Label(f, text="Error, You are already in the start!!!!", fg='#C3FDB8', bg="#C3FDB8",
                        font=("Times New Roman", 18))
            lw2.place(x=90, y=560)
            return lw2
  

    def submit(self):
        l1[self.qno] = self.opt_selected.get()
        x = 0
        y = True
        for i in range(10):
            if (l1[i] == 0):
                x += 1

        if (x > 0 and x != 1):
            y = messagebox.askyesno("Warning", "You have not attempted " + str(x) + " questions, Are you sure you want to submit?, You won't be able to make changes again.")
        elif (x == 1):
            y = messagebox.askyesno("Warning", "You have not attempted " + str(x) + " questions, Are you sure you want to submit?, You won't be able to make changes again.")
        if (y == True or x == 0):
            s = 0
            for i in range(10):
                if (l1[i] == answerstemp[i][0]):
                    s = s + 1
            print("DEBUG: Score: ", s)


        conn = mysql.connect(host='localhost', database='quizdb', user='root', password='12345')
        cursor = conn.cursor()
        q = "update reg set score='%d' where uname= '%s'"
        val = (s, self.user)
        cursor.execute(q % val)
        conn.commit()
        cursor.close()
        conn.close()

        messagebox.showinfo("Score", "Your Score is: " + str(s) + "/10")
        mQuiz.destroy()
   
if __name__=='__main__':

    root=Tk()
    root.resizable(0, 0)
    MainObj=StartWindow(root)
    root.mainloop()
