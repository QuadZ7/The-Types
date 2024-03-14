import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import webbrowser


def createconnection() :
    global conn,cursor
    conn = sqlite3.connect('userinfo.db')
    cursor = conn.cursor()

def mainwindow() :
    root = Tk()
    w = 1100
    h = 800
    x = root.winfo_screenwidth()/2 - w/2
    y = root.winfo_screenheight()/2 - h/2
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    root.config(bg='black')
    root.title("The Types")
    root.iconbitmap('images\logo.ico')
    root.option_add('*font',"Kanit")
    root.rowconfigure((0,1,2,3),weight=1)
    root.columnconfigure((0,1,2,3),weight=1)
    root.resizable(False,False)
    return root

def callback(url):
   webbrowser.open_new_tab(url)

def widgedlogin() :
    global userentry,pwdentry,forgot_pass_button
    root.title("The Types")
    loginframe = Frame(root,bg='black')
    loginframe.rowconfigure((0,1,2,3),weight=1)
    loginframe.columnconfigure((0,1),weight=1)
    loginframe.grid(row=1,column=1,columnspan=2,rowspan=2,sticky='news')

    
    Label(loginframe,image=img2,bg='black').grid(row=0,rowspan=2,column=0,columnspan=2,sticky='news')
    Button(loginframe,text='LOGIN',image=img5,bd=0,bg='black',fg='black',font='Kanit 25 bold',activebackground='black',compound=CENTER,command=loginclick).grid(row=2,column=0,columnspan=2)
    Button(loginframe,text='REGISTER',image=img5,bd=0,bg='black',fg='black',font='Kanit 25 bold',activebackground='black',compound=CENTER,command=regisclick).grid(row=3,column=0,columnspan=2,sticky='n')
    forgot_pass_button = Label(loginframe,text='forgot password',bg='black',fg='white',font='Kanit 15 bold')
    forgot_pass_button.grid(row=4,column=0,columnspan=2,sticky='n')
    forgot_pass_button.bind("<Button-1>",lambda e:forgotclick())

#ฟังก์ชั่นป่มล็อกอินหน้าแรกสุด
def loginclick():
    global userentry,loginmenu,pwdentry
    loginmenu=Frame(root,bg='black')
    loginmenu.rowconfigure((0,1,2,3,4,5,6,7),weight=1)
    loginmenu.columnconfigure((0,1,2),weight=1)
    loginmenu.grid(row=0,column=0,rowspan=4,columnspan=4,sticky='news')

    Label(loginmenu,text='account login',image=img2,bg='black',font='Kanit 35 bold',compound=TOP,fg='white').grid(row=0,column=0,columnspan=3,sticky='news')
    
    Label(loginmenu,text='username:',fg='white',font='Kanit 20 bold',bg='black').grid(row=1,column=0,columnspan=3,sticky='n')
    userentry = Entry(loginmenu,width=25,textvariable=userinfo)
    userentry.grid(row=2,column=0,columnspan=3,sticky='n',ipady=7)

    Label(loginmenu,text='password:',fg='white',font='Kanit 20 bold',bg='black').grid(row=3,column=0,columnspan=3,sticky='n')
    pwdentry = Entry(loginmenu,width=25,show='*',textvariable=pwdinfo)
    pwdentry.grid(row=4,column=0,columnspan=3,sticky='n',ipady=7)

    Button(loginmenu,text='LOGIN',image=img6,bd=0,bg='black',fg='black',font='Kanit 25 bold',activebackground='black',compound=CENTER,command=reallogin).grid(row=5,column=0,columnspan=3,sticky='n')

    forgot_pass_button = Label(loginmenu,text='forgot password',bg='black',fg='white',font='Kanit 15 bold')
    forgot_pass_button.grid(row=6,column=0,columnspan=3,sticky='n')
    forgot_pass_button.bind("<Button-1>",lambda e:forgotclick())

    login_back = Button(loginmenu,text='cancle',image=img7,bd=0,bg='black',fg='black',font='Kanit 25 bold',activebackground='black',compound=CENTER,command=cancleloginclick)
    login_back.grid(row=7,column=0)

#ฟังก์ชั่นป่มลงทะเบียนหน้าแรกสุด
def regisclick():
    global firstname,lastname,Male,Female,Other,newuser,newpwd,cfpwd
    global regismenu

    regismenu=Frame(root,bg='black')
    regismenu.rowconfigure((0,1,2,3,4,5,6,7,8,9,10),weight=1)
    regismenu.columnconfigure((0,1,2),weight=1)
    regismenu.grid(row=0,column=0,rowspan=4,columnspan=4,sticky='news')

    #Header
    Label(regismenu,image=img8,bg='black').grid(row=0,column=0,columnspan=3)

    #firstname entry
    Label(regismenu,text='First name:',bg='black',fg='white',font='Kanit 15 bold').grid(row=1,column=0,sticky='e')
    firstname = Entry(regismenu)
    firstname.grid(row=1,column=1,ipadx=25)

    #Lastname entry
    Label(regismenu,text='Last name:',bg='black',fg='white',font='Kanit 15 bold').grid(row=2,column=0,sticky='ne')
    lastname = Entry(regismenu)
    lastname.grid(row=2,column=1,ipadx=25,sticky='n')

    Label(regismenu,text='Gender : ',bg='black',fg='white',font='Kanit 15 bold').grid(row=3,column=0,sticky='ne')
    Male = Radiobutton(regismenu,text='Male', value='Male',bg='black',fg='white',font='Kanit 15 bold',selectcolor='black',variable=Gender)
    Male.grid(row=3,column=1,sticky='n')
    Female = Radiobutton(regismenu,text='Female', value='Female',bg='black',fg='white',font='Kanit 15 bold',selectcolor='black',variable=Gender)
    Female.grid(row=4,column=1,sticky='n')
    Other = Radiobutton(regismenu,text='Other', value='Other',bg='black',fg='white',font='Kanit 15 bold',selectcolor='black',variable=Gender)
    Other.grid(row=5,column=1,sticky='n')

    Label(regismenu,text="Username:",bg='black',fg='white',font='Kanit 15 bold').grid(row=6,column=0,sticky='ne')
    newuser = Entry(regismenu)
    newuser.grid(row=6,column=1,ipadx=25,sticky='n')

    Label(regismenu,text="Password:",bg='black',fg='white',font='Kanit 15 bold').grid(row=7,column=0,sticky='ne')
    newpwd = Entry(regismenu,show='*')
    newpwd.grid(row=7,column=1,ipadx=25,sticky='n')

    Label(regismenu,text="Confirm Password:",bg='black',fg='white',font='Kanit 15 bold').grid(row=8,column=0,sticky='ne')
    cfpwd = Entry(regismenu,show='*')
    cfpwd.grid(row=8,column=1,ipadx=25,sticky='n')

    Button(regismenu,image=img9,bd=0,bg='black',activebackground='black',command=regisnowclick).grid(row=9,column=0,columnspan=3,sticky='n')

    regis_back = Button(regismenu,text='cancle',image=img7,bd=0,bg='black',fg='black',font='Kanit 25 bold',activebackground='black',compound=CENTER,command=cancleregisclick)
    regis_back.grid(row=10,column=0)

#ปุ่มฟังก์ชั่นล็อกอินหลังจากกรอกข้อมูลแล้ว
def reallogin():
    global user_result
    
    user = userinfo.get()
    pwd = pwdinfo.get()
    #check the user entry and login
    if user == "" :
        messagebox.showwarning("Admin:","Please enter Username")
        userentry.focus_force()
    else :
        sql = "select * from userinfo where username=?"
        cursor.execute(sql,[user])
        result = cursor.fetchall()
        if result :
            if pwd == "" :
                messagebox.showwarning("Admin:","Please enter password")
                pwdentry.focus_force()
            else :
                sql = "select * from userinfo where username=? and password=? "
                cursor.execute(sql,[user,pwd])   #case1
                user_result = cursor.fetchone()
                if user_result :
                    messagebox.showinfo("Admin:","login Successfully")
                    homepage()
                else :
                    messagebox.showwarning("Admin:","Incorrect Username or Password")
                    pwdentry.select_range(0,END)
                    pwdentry.focus_force()
        else :
            messagebox.showerror("Admin:","Username not found")
            userentry.select_range(0,END)
            userentry.focus_force()

def regisnowclick():
    if firstname.get() == '':
        messagebox.showwarning('Admin','Enter student ID first')
    elif lastname.get() == '':
        messagebox.showwarning('Admin','Enter firstname first')
    elif Gender.get() == '':
        messagebox.showwarning('Admin','Select gender first')
    elif newuser.get() == '':
        messagebox.showwarning('Admin','Enter username first')
    elif newpwd.get() == '':
        messagebox.showwarning('Admin','Enter password first')
    else:
        #add data to student table
        sql = '''
                    insert into userinfo("username","password","firstname","lastname","gender")
                    values (?,?,?,?,?)
            
                    '''
        nuser = newuser.get()
        pwdn = newpwd.get()
        fname = firstname.get()
        lname = lastname.get()
        if Gender.get() == 'Male':
            tgender = 'Male'
        elif Gender.get() == 'Female':
            tgender = 'Female'
        elif Gender.get() == 'Other':
            tgender = 'Other'

        cursor.execute(sql,[nuser,pwdn,fname,lname,tgender])
        conn.commit()

        
        messagebox.showinfo("Admin:","Registration successfully")
        regismenu.destroy()


#ฟังกชั่นไปหน้าหลังจากล็อกอินเสร็จ
def homepage():
    global homeframe,homehead,homebot
    #หน้าโฮมข้างบน
    homeframe=Frame(root,bg='black')
    homeframe.rowconfigure((0,1,2,3,4),weight=1)
    homeframe.columnconfigure((0,1,2,3),weight=1)
    homeframe.grid(row=0,rowspan=4,column=0,columnspan=4,sticky='news')

    homehead=Frame(homeframe,bg='white')
    homehead.rowconfigure(0,weight=1)
    homehead.columnconfigure((0,1,2),weight=1)
    homehead.grid(row=0,column=0,columnspan=4,sticky='news')

    #หน้าโฮมข้างล่าง
    homebot=Frame(homeframe,bg='black')
    homebot.rowconfigure((0,1,2,3,4,5,6,7),weight=1)
    homebot.columnconfigure((0,1,2,3),weight=1)
    homebot.grid(row=1,rowspan=3,column=0,columnspan=4,sticky='news')
    
    homeback = Label(homehead,text='BACK',bg='white',fg='black',font='Kanit 20 bold')
    homeback.grid(row=0,column=0,sticky='w',padx=20)
    homeback.bind("<Button-1>",lambda e:homeexit())

    homeheader = Label(homehead,text='HOME',bg='white',fg='black',font='Kanit 35 bold')
    homeheader.grid(row=0,column=0,columnspan=3,sticky='n')

    homeback = Label(homehead,text='PROFILE',bg='white',fg='black',font='Kanit 20 bold')
    homeback.grid(row=0,column=2,sticky='e',padx=20)
    homeback.bind("<Button-1>",lambda e:enterPF())

    Label(homebot,text='Please choose the test',bg='black',fg='white',font='Kanit 35 bold').grid(row=0,column=0,columnspan=4)

    # 2 tests
    test1 = Label(homebot,image=img10,bg='black')
    test1.grid(row=1,column=0,columnspan=2)
    test1.bind("<Button-1>",lambda e:test1click())

    test2 = Label(homebot,image=img11,bg='black')
    test2.grid(row=1,column=2,columnspan=2)
    test2.bind("<Button-1>",lambda e:test2click())

################################################
################### test 1 #####################
################################################

def test1click():
    global test1page,mbti
    mbti = ''
    test1page=Frame(homeframe,bg='black')
    test1page.rowconfigure((0,1,2,3,4,5,6,7),weight=1)
    test1page.columnconfigure((0,1,2,3),weight=1)
    test1page.grid(row=1,rowspan=3,column=0,columnspan=4,sticky='news')
    
    Label(test1page,text='MBTI test',bg='black',fg='white',font='Kanit 30 bold').grid(row=1,column=0,columnspan=4)

    Button(test1page,text='ชอบเข้าสังคม',image=img7,bd=0,bg='black',activebackground='black',compound=CENTER,command=E).grid(row=2,rowspan=2,column=0,columnspan=2,sticky='e',ipadx=10)
    Button(test1page,text='ชอบเก็บตัว',image=img7,bd=0,bg='black',activebackground='black',compound=CENTER,command=I).grid(row=2,rowspan=2,column=2,columnspan=2,sticky='w',ipadx=10)

def E():
    global mbti
    mbti += 'E'

    test1page=Frame(homeframe,bg='black')
    test1page.rowconfigure((0,1,2,3,4,5,6,7),weight=1)
    test1page.columnconfigure((0,1,2,3),weight=1)
    test1page.grid(row=1,rowspan=3,column=0,columnspan=4,sticky='news')
    
    Label(test1page,text='MBTI test',bg='black',fg='white',font='Kanit 30 bold').grid(row=1,column=0,columnspan=4)

    Button(test1page,text='อยู่กับความเป็นจริง',image=img7,bd=0,bg='black',activebackground='black',compound=CENTER,command=S).grid(row=2,rowspan=2,column=0,columnspan=2,sticky='e',ipadx=10)
    Button(test1page,text='มีวิศัยทัศน์',image=img7,bd=0,bg='black',activebackground='black',compound=CENTER,command=N).grid(row=2,rowspan=2,column=2,columnspan=2,sticky='w',ipadx=10)


def I():
    global mbti
    mbti += 'I'

    test1page=Frame(homeframe,bg='black')
    test1page.rowconfigure((0,1,2,3,4,5,6,7),weight=1)
    test1page.columnconfigure((0,1,2,3),weight=1)
    test1page.grid(row=1,rowspan=3,column=0,columnspan=4,sticky='news')
    
    Label(test1page,text='MBTI test',bg='black',fg='white',font='Kanit 30 bold').grid(row=1,column=0,columnspan=4)

    Button(test1page,text='อยู่กับความเป็นจริง',image=img7,bd=0,bg='black',activebackground='black',compound=CENTER,command=S).grid(row=2,rowspan=2,column=0,columnspan=2,sticky='e',ipadx=10)
    Button(test1page,text='มีวิศัยทัศน์',image=img7,bd=0,bg='black',activebackground='black',compound=CENTER,command=N).grid(row=2,rowspan=2,column=2,columnspan=2,sticky='w',ipadx=10)


def S():
    global mbti
    mbti += 'S'

    test1page=Frame(homeframe,bg='black')
    test1page.rowconfigure((0,1,2,3,4,5,6,7),weight=1)
    test1page.columnconfigure((0,1,2,3),weight=1)
    test1page.grid(row=1,rowspan=3,column=0,columnspan=4,sticky='news')
    
    Label(test1page,text='MBTI test',bg='black',fg='white',font='Kanit 30 bold').grid(row=1,column=0,columnspan=4)

    Button(test1page,text='ใช้ความคิด',image=img7,bd=0,bg='black',activebackground='black',compound=CENTER,command=T).grid(row=2,rowspan=2,column=0,columnspan=2,sticky='e',ipadx=10)
    Button(test1page,text='ใช้ความรู้สึก',image=img7,bd=0,bg='black',activebackground='black',compound=CENTER,command=F).grid(row=2,rowspan=2,column=2,columnspan=2,sticky='w',ipadx=10)


def N():
    global mbti
    mbti += 'N'

    test1page=Frame(homeframe,bg='black')
    test1page.rowconfigure((0,1,2,3,4,5,6,7),weight=1)
    test1page.columnconfigure((0,1,2,3),weight=1)
    test1page.grid(row=1,rowspan=3,column=0,columnspan=4,sticky='news')
    
    Label(test1page,text='MBTI test',bg='black',fg='white',font='Kanit 30 bold').grid(row=1,column=0,columnspan=4)

    Button(test1page,text='ใช้ความคิด',image=img7,bd=0,bg='black',activebackground='black',compound=CENTER,command=T).grid(row=2,rowspan=2,column=0,columnspan=2,sticky='e',ipadx=10)
    Button(test1page,text='ใช้ความรู้สึก',image=img7,bd=0,bg='black',activebackground='black',compound=CENTER,command=F).grid(row=2,rowspan=2,column=2,columnspan=2,sticky='w',ipadx=10)


def T():
    global mbti
    mbti += 'T'

    test1page=Frame(homeframe,bg='black')
    test1page.rowconfigure((0,1,2,3,4,5,6,7),weight=1)
    test1page.columnconfigure((0,1,2,3),weight=1)
    test1page.grid(row=1,rowspan=3,column=0,columnspan=4,sticky='news')
    
    Label(test1page,text='MBTI test',bg='black',fg='white',font='Kanit 30 bold').grid(row=1,column=0,columnspan=4)

    Button(test1page,text='มีระเบียบแบบแผน',image=img7,bd=0,bg='black',activebackground='black',compound=CENTER,command=J).grid(row=2,rowspan=2,column=0,columnspan=2,sticky='e',ipadx=10)
    Button(test1page,text='ยืดหยุ่น',image=img7,bd=0,bg='black',activebackground='black',compound=CENTER,command=P).grid(row=2,rowspan=2,column=2,columnspan=2,sticky='w',ipadx=10)


def F():
    global mbti
    mbti += 'F'

    test1page=Frame(homeframe,bg='black')
    test1page.rowconfigure((0,1,2,3,4,5,6,7),weight=1)
    test1page.columnconfigure((0,1,2,3),weight=1)
    test1page.grid(row=1,rowspan=3,column=0,columnspan=4,sticky='news')
    
    Label(test1page,text='MBTI test',bg='black',fg='white',font='Kanit 30 bold').grid(row=1,column=0,columnspan=4)

    Button(test1page,text='มีระเบียบแบบแผน',image=img7,bd=0,bg='black',activebackground='black',compound=CENTER,command=J).grid(row=2,rowspan=2,column=0,columnspan=2,sticky='e',ipadx=10)
    Button(test1page,text='ยืดหยุ่น',image=img7,bd=0,bg='black',activebackground='black',compound=CENTER,command=P).grid(row=2,rowspan=2,column=2,columnspan=2,sticky='w',ipadx=10)

def J():
    global mbti
    mbti += 'J'

    test1page=Frame(homeframe,bg='black')
    test1page.rowconfigure((0,1,2,3,4,5,6,7),weight=1)
    test1page.columnconfigure((0,1,2,3),weight=1)
    test1page.grid(row=1,rowspan=3,column=0,columnspan=4,sticky='news')

    Label(test1page,text='congratulations\nyou got',bg='black',fg='white',font='Kanit 30 bold').grid(row=1,column=0,columnspan=4)

    sql = "select * from userinfo where username=?;"
        #execute step
    cursor.execute(sql,[user_result[0]])
        #fetch result
    result = cursor.fetchone()
    if result :
        #define sql select command of course name for duplicating
        sql = "select * from userinfo where username=?;"
        #execute step
        cursor.execute(sql,[user_result[0]])
            #fetch result
        result = cursor.fetchone()

        if result :
                #define sql for updating of day,room fields
            sql = """
                                update userinfo
                                set mbti=?
                                where username=?;
            """
            finalmbti = mbti  
                #execute step
            cursor.execute(sql,[finalmbti,user_result[0]])
                #commit step
            conn.commit()

        Label(test1page,text=mbti,bg='black',fg='white',font='Kanit 50 bold').grid(row=2,rowspan=2,column=0,columnspan=4)

        linken = Label(test1page, text="<< Learn about MBTI here >>",bg='black',fg='white',font='Kanit 30 bold', cursor="hand2")
        linken.grid(row=4,rowspan=2,column=0,columnspan=4)
        linken.bind("<Button-1>", lambda e:callback("https://www.urbinner.com/post/what-is-mbti"))

def P():
    global mbti
    mbti += 'P'

    test1page=Frame(homeframe,bg='black')
    test1page.rowconfigure((0,1,2,3,4,5,6,7),weight=1)
    test1page.columnconfigure((0,1,2,3),weight=1)
    test1page.grid(row=1,rowspan=3,column=0,columnspan=4,sticky='news')

    Label(test1page,text='congratulations\nyou got',bg='black',fg='white',font='Kanit 30 bold').grid(row=1,column=0,columnspan=4)

    sql = "select * from userinfo where username=?;"
        #execute step
    cursor.execute(sql,[user_result[0]])
        #fetch result
    result = cursor.fetchone()
    if result :
        #define sql select command of course name for duplicating
        sql = "select * from userinfo where username=?;"
        #execute step
        cursor.execute(sql,[user_result[0]])
            #fetch result
        result = cursor.fetchone()

        if result :
                #define sql for updating of day,room fields
            sql = """
                                update userinfo
                                set mbti=?
                                where username=?;
            """
            finalmbti = mbti  
                #execute step
            cursor.execute(sql,[finalmbti,user_result[0]])
                #commit step
            conn.commit()

        Label(test1page,text=mbti,bg='black',fg='white',font='Kanit 50 bold').grid(row=2,rowspan=2,column=0,columnspan=4)

        linken = Label(test1page, text="<< Learn about MBTI here >>",bg='black',fg='white',font='Kanit 30 bold', cursor="hand2")
        linken.grid(row=4,rowspan=2,column=0,columnspan=4)
        linken.bind("<Button-1>", lambda e:callback("https://www.urbinner.com/post/what-is-mbti"))


################################################
################### test 2 #####################
################################################

def test2click():
    global test2page
    test2page=Frame(homeframe,bg='black')
    test2page.rowconfigure((0,1,2,3,4,5,6,7),weight=1)
    test2page.columnconfigure((0,1,2,3),weight=1)
    test2page.grid(row=1,rowspan=3,column=0,columnspan=4,sticky='news')
    
    Label(test2page,text='Are you optimistic to the point of being delusional?',bg='black',fg='white',font='Kanit 20 bold').grid(row=1,column=0,columnspan=4)

    Button(test2page,text='Yes',image=img7,bd=0,bg='black',activebackground='black',compound=CENTER,command=q11).grid(row=2,column=0,columnspan=2,sticky='e',ipadx=10)
    Button(test2page,text='No',image=img7,bd=0,bg='black',activebackground='black',compound=CENTER,command=q02).grid(row=2,column=2,columnspan=2,sticky='w',ipadx=10)

def q02():
    global test2page
    test2page=Frame(homeframe,bg='black')
    test2page.rowconfigure((0,1,2,3,4,5,6,7),weight=1)
    test2page.columnconfigure((0,1,2,3),weight=1)
    test2page.grid(row=1,rowspan=3,column=0,columnspan=4,sticky='news')
    
    Label(test2page,text='When you are upset do you throw a trantrum like a lil baby?',bg='black',fg='white',font='Kanit 20 bold').grid(row=1,column=0,columnspan=4)

    Button(test2page,text='Yes',image=img7,bd=0,bg='black',activebackground='black',compound=CENTER,command=q21).grid(row=2,column=0,columnspan=2,sticky='e',ipadx=10)
    Button(test2page,text='No',image=img7,bd=0,bg='black',activebackground='black',compound=CENTER,command=q03).grid(row=2,column=2,columnspan=2,sticky='w',ipadx=10)

def q03():
    global test2page
    test2page=Frame(homeframe,bg='black')
    test2page.rowconfigure((0,1,2,3,4,5,6,7),weight=1)
    test2page.columnconfigure((0,1,2,3),weight=1)
    test2page.grid(row=1,rowspan=3,column=0,columnspan=4,sticky='news')
    
    Label(test2page,text='Do you have a stick up your ass?',bg='black',fg='white',font='Kanit 20 bold').grid(row=1,column=0,columnspan=4)

    Button(test2page,text='Yes',image=img7,bd=0,bg='black',activebackground='black',compound=CENTER,command=q31).grid(row=2,column=0,columnspan=2,sticky='e',ipadx=10)
    Button(test2page,text='No',image=img7,bd=0,bg='black',activebackground='black',compound=CENTER,command=a3).grid(row=2,column=2,columnspan=2,sticky='w',ipadx=10)

def q31():
    global test2page
    test2page=Frame(homeframe,bg='black')
    test2page.rowconfigure((0,1,2,3,4,5,6,7),weight=1)
    test2page.columnconfigure((0,1,2,3),weight=1)
    test2page.grid(row=1,rowspan=3,column=0,columnspan=4,sticky='news')
    
    Label(test2page,text='Do you have a HUGE stick up your ass?',bg='black',fg='white',font='Kanit 20 bold').grid(row=1,column=0,columnspan=4)

    Button(test2page,text='Yes',image=img7,bd=0,bg='black',activebackground='black',compound=CENTER,command=a1).grid(row=2,column=0,columnspan=2,sticky='e',ipadx=10)
    Button(test2page,text='No',image=img7,bd=0,bg='black',activebackground='black',compound=CENTER,command=a5).grid(row=2,column=2,columnspan=2,sticky='w',ipadx=10)

def a1():
    global test2page
    test2page=Frame(homeframe,bg='black')
    test2page.rowconfigure((0,1,2,3,4,5,6,7),weight=1)
    test2page.columnconfigure((0,1,2,3),weight=1)
    test2page.grid(row=1,rowspan=3,column=0,columnspan=4,sticky='news')

    Label(test2page,text='congratulations\nyou got',bg='black',fg='white',font='Kanit 30 bold').grid(row=1,column=0,columnspan=4)

    sql = "select * from userinfo where username=?;"
        #execute step
    cursor.execute(sql,[user_result[0]])
        #fetch result
    result = cursor.fetchone()
    if result :
        #define sql select command of course name for duplicating
        sql = "select * from userinfo where username=?;"
        #execute step
        cursor.execute(sql,[user_result[0]])
            #fetch result
        result = cursor.fetchone()

        if result :
                #define sql for updating of day,room fields
            sql = """
                                update userinfo
                                set enneagrame=?
                                where username=?;
            """
            eng = 'type 1'  
                #execute step
            cursor.execute(sql,[eng,user_result[0]])
                #commit step
            conn.commit()

    Label(test2page,text='type 1',bg='black',fg='white',font='Kanit 50 bold').grid(row=2,rowspan=2,column=0,columnspan=4)

    linken = Label(test2page, text="<< Learn about Enneagram here >>",bg='black',fg='white',font='Kanit 30 bold', cursor="hand2")
    linken.grid(row=4,rowspan=2,column=0,columnspan=4)
    linken.bind("<Button-1>", lambda e:callback("https://www.urbinner.com/post/what-is-enneagram"))


def a5():
    global test2page
    test2page=Frame(homeframe,bg='black')
    test2page.rowconfigure((0,1,2,3,4,5,6,7),weight=1)
    test2page.columnconfigure((0,1,2,3),weight=1)
    test2page.grid(row=1,rowspan=3,column=0,columnspan=4,sticky='news')

    Label(test2page,text='congratulations\nyou got',bg='black',fg='white',font='Kanit 30 bold').grid(row=1,column=0,columnspan=4)

    sql = "select * from userinfo where username=?;"
        #execute step
    cursor.execute(sql,[user_result[0]])
        #fetch result
    result = cursor.fetchone()
    if result :
        #define sql select command of course name for duplicating
        sql = "select * from userinfo where username=?;"
        #execute step
        cursor.execute(sql,[user_result[0]])
            #fetch result
        result = cursor.fetchone()

        if result :
                #define sql for updating of day,room fields
            sql = """
                                update userinfo
                                set enneagrame=?
                                where username=?;
            """
            eng = 'type 5'  
                #execute step
            cursor.execute(sql,[eng,user_result[0]])
                #commit step
            conn.commit()

    Label(test2page,text='type 5',bg='black',fg='white',font='Kanit 50 bold').grid(row=2,rowspan=2,column=0,columnspan=4)

    linken = Label(test2page, text="<< Learn about Enneagram here >>",bg='black',fg='white',font='Kanit 30 bold', cursor="hand2")
    linken.grid(row=4,rowspan=2,column=0,columnspan=4)
    linken.bind("<Button-1>", lambda e:callback("https://www.urbinner.com/post/what-is-enneagram"))

def a3():
    global test2page
    test2page=Frame(homeframe,bg='black')
    test2page.rowconfigure((0,1,2,3,4,5,6,7),weight=1)
    test2page.columnconfigure((0,1,2,3),weight=1)
    test2page.grid(row=1,rowspan=3,column=0,columnspan=4,sticky='news')

    Label(test2page,text='congratulations\nyou got',bg='black',fg='white',font='Kanit 30 bold').grid(row=1,column=0,columnspan=4)

    sql = "select * from userinfo where username=?;"
        #execute step
    cursor.execute(sql,[user_result[0]])
        #fetch result
    result = cursor.fetchone()
    if result :
        #define sql select command of course name for duplicating
        sql = "select * from userinfo where username=?;"
        #execute step
        cursor.execute(sql,[user_result[0]])
            #fetch result
        result = cursor.fetchone()

        if result :
                #define sql for updating of day,room fields
            sql = """
                                update userinfo
                                set enneagrame=?
                                where username=?;
            """
            eng = 'type 3'  
                #execute step
            cursor.execute(sql,[eng,user_result[0]])
                #commit step
            conn.commit()

    Label(test2page,text='type 3',bg='black',fg='white',font='Kanit 50 bold').grid(row=2,rowspan=2,column=0,columnspan=4)

    linken = Label(test2page, text="<< Learn about Enneagram here >>",bg='black',fg='white',font='Kanit 30 bold', cursor="hand2")
    linken.grid(row=4,rowspan=2,column=0,columnspan=4)
    linken.bind("<Button-1>", lambda e:callback("https://www.urbinner.com/post/what-is-enneagram"))

def q21():
    global test2page
    test2page=Frame(homeframe,bg='black')
    test2page.rowconfigure((0,1,2,3,4,5,6,7),weight=1)
    test2page.columnconfigure((0,1,2,3),weight=1)
    test2page.grid(row=1,rowspan=3,column=0,columnspan=4,sticky='news')
    
    Label(test2page,text='Are you remotely likeable?',bg='black',fg='white',font='Kanit 20 bold').grid(row=1,column=0,columnspan=4)

    Button(test2page,text='Yes',image=img7,bd=0,bg='black',activebackground='black',compound=CENTER,command=a6).grid(row=2,column=0,columnspan=2,sticky='e',ipadx=10)
    Button(test2page,text='No',image=img7,bd=0,bg='black',activebackground='black',compound=CENTER,command=q22).grid(row=2,column=2,columnspan=2,sticky='w',ipadx=10)

def a6():
    global test2page
    test2page=Frame(homeframe,bg='black')
    test2page.rowconfigure((0,1,2,3,4,5,6,7),weight=1)
    test2page.columnconfigure((0,1,2,3),weight=1)
    test2page.grid(row=1,rowspan=3,column=0,columnspan=4,sticky='news')

    Label(test2page,text='congratulations\nyou got',bg='black',fg='white',font='Kanit 30 bold').grid(row=1,column=0,columnspan=4)

    sql = "select * from userinfo where username=?;"
        #execute step
    cursor.execute(sql,[user_result[0]])
        #fetch result
    result = cursor.fetchone()
    if result :
        #define sql select command of course name for duplicating
        sql = "select * from userinfo where username=?;"
        #execute step
        cursor.execute(sql,[user_result[0]])
            #fetch result
        result = cursor.fetchone()

        if result :
                #define sql for updating of day,room fields
            sql = """
                                update userinfo
                                set enneagrame=?
                                where username=?;
            """
            eng = 'type 6'  
                #execute step
            cursor.execute(sql,[eng,user_result[0]])
                #commit step
            conn.commit()

    Label(test2page,text='type 6',bg='black',fg='white',font='Kanit 50 bold').grid(row=2,rowspan=2,column=0,columnspan=4)

    linken = Label(test2page, text="<< Learn about Enneagram here >>",bg='black',fg='white',font='Kanit 30 bold', cursor="hand2")
    linken.grid(row=4,rowspan=2,column=0,columnspan=4)
    linken.bind("<Button-1>", lambda e:callback("https://www.urbinner.com/post/what-is-enneagram"))

def q22():
    global test2page
    test2page=Frame(homeframe,bg='black')
    test2page.rowconfigure((0,1,2,3,4,5,6,7),weight=1)
    test2page.columnconfigure((0,1,2,3),weight=1)
    test2page.grid(row=1,rowspan=3,column=0,columnspan=4,sticky='news')
    
    Label(test2page,text='Do you leave the house?',bg='black',fg='white',font='Kanit 20 bold').grid(row=1,column=0,columnspan=4)

    Button(test2page,text='Yes',image=img7,bd=0,bg='black',activebackground='black',compound=CENTER,command=a8).grid(row=2,column=0,columnspan=2,sticky='e',ipadx=10)
    Button(test2page,text='No',image=img7,bd=0,bg='black',activebackground='black',compound=CENTER,command=a4).grid(row=2,column=2,columnspan=2,sticky='w',ipadx=10)

def a8():
    global test2page
    test2page=Frame(homeframe,bg='black')
    test2page.rowconfigure((0,1,2,3,4,5,6,7),weight=1)
    test2page.columnconfigure((0,1,2,3),weight=1)
    test2page.grid(row=1,rowspan=3,column=0,columnspan=4,sticky='news')

    Label(test2page,text='congratulations\nyou got',bg='black',fg='white',font='Kanit 30 bold').grid(row=1,column=0,columnspan=4)

    sql = "select * from userinfo where username=?;"
        #execute step
    cursor.execute(sql,[user_result[0]])
        #fetch result
    result = cursor.fetchone()
    if result :
        #define sql select command of course name for duplicating
        sql = "select * from userinfo where username=?;"
        #execute step
        cursor.execute(sql,[user_result[0]])
            #fetch result
        result = cursor.fetchone()

        if result :
                #define sql for updating of day,room fields
            sql = """
                                update userinfo
                                set enneagrame=?
                                where username=?;
            """
            eng = 'type 8'  
                #execute step
            cursor.execute(sql,[eng,user_result[0]])
                #commit step
            conn.commit()

    Label(test2page,text='type 8',bg='black',fg='white',font='Kanit 50 bold').grid(row=2,rowspan=2,column=0,columnspan=4)

    linken = Label(test2page, text="<< Learn about Enneagram here >>",bg='black',fg='white',font='Kanit 30 bold', cursor="hand2")
    linken.grid(row=4,rowspan=2,column=0,columnspan=4)
    linken.bind("<Button-1>", lambda e:callback("https://www.urbinner.com/post/what-is-enneagram"))


def a4():
    global test2page
    test2page=Frame(homeframe,bg='black')
    test2page.rowconfigure((0,1,2,3,4,5,6,7),weight=1)
    test2page.columnconfigure((0,1,2,3),weight=1)
    test2page.grid(row=1,rowspan=3,column=0,columnspan=4,sticky='news')

    Label(test2page,text='congratulations\nyou got',bg='black',fg='white',font='Kanit 30 bold').grid(row=1,column=0,columnspan=4)

    sql = "select * from userinfo where username=?;"
        #execute step
    cursor.execute(sql,[user_result[0]])
        #fetch result
    result = cursor.fetchone()
    if result :
        #define sql select command of course name for duplicating
        sql = "select * from userinfo where username=?;"
        #execute step
        cursor.execute(sql,[user_result[0]])
            #fetch result
        result = cursor.fetchone()

        if result :
                #define sql for updating of day,room fields
            sql = """
                                update userinfo
                                set enneagrame=?
                                where username=?;
            """
            eng = 'type 4'  
                #execute step
            cursor.execute(sql,[eng,user_result[0]])
                #commit step
            conn.commit()

    Label(test2page,text='type 4',bg='black',fg='white',font='Kanit 50 bold').grid(row=2,rowspan=2,column=0,columnspan=4)

    linken = Label(test2page, text="<< Learn about Enneagram here >>",bg='black',fg='white',font='Kanit 30 bold', cursor="hand2")
    linken.grid(row=4,rowspan=2,column=0,columnspan=4)
    linken.bind("<Button-1>", lambda e:callback("https://www.urbinner.com/post/what-is-enneagram"))


def q11():
    global test2page
    test2page=Frame(homeframe,bg='black')
    test2page.rowconfigure((0,1,2,3,4,5,6,7),weight=1)
    test2page.columnconfigure((0,1,2,3),weight=1)
    test2page.grid(row=1,rowspan=3,column=0,columnspan=4,sticky='news')
    
    Label(test2page,text='Do you let people walk over you?',bg='black',fg='white',font='Kanit 20 bold').grid(row=1,column=0,columnspan=4)

    Button(test2page,text='Yes',image=img7,bd=0,bg='black',activebackground='black',compound=CENTER,command=q12).grid(row=2,column=0,columnspan=2,sticky='e',ipadx=10)
    Button(test2page,text='No',image=img7,bd=0,bg='black',activebackground='black',compound=CENTER,command=a7).grid(row=2,column=2,columnspan=2,sticky='w',ipadx=10)

def a7():
    global test2page
    test2page=Frame(homeframe,bg='black')
    test2page.rowconfigure((0,1,2,3,4,5,6,7),weight=1)
    test2page.columnconfigure((0,1,2,3),weight=1)
    test2page.grid(row=1,rowspan=3,column=0,columnspan=4,sticky='news')

    Label(test2page,text='congratulations\nyou got',bg='black',fg='white',font='Kanit 30 bold').grid(row=1,column=0,columnspan=4)

    sql = "select * from userinfo where username=?;"
        #execute step
    cursor.execute(sql,[user_result[0]])
        #fetch result
    result = cursor.fetchone()
    if result :
        #define sql select command of course name for duplicating
        sql = "select * from userinfo where username=?;"
        #execute step
        cursor.execute(sql,[user_result[0]])
            #fetch result
        result = cursor.fetchone()

        if result :
                #define sql for updating of day,room fields
            sql = """
                                update userinfo
                                set enneagrame=?
                                where username=?;
            """
            eng = 'type 7'  
                #execute step
            cursor.execute(sql,[eng,user_result[0]])
                #commit step
            conn.commit()

    Label(test2page,text='type 7',bg='black',fg='white',font='Kanit 50 bold').grid(row=2,rowspan=2,column=0,columnspan=4)

    linken = Label(test2page, text="<< Learn about Enneagram here >>",bg='black',fg='white',font='Kanit 30 bold', cursor="hand2")
    linken.grid(row=4,rowspan=2,column=0,columnspan=4)
    linken.bind("<Button-1>", lambda e:callback("https://www.urbinner.com/post/what-is-enneagram"))
    


def q12():
    global test2page
    test2page=Frame(homeframe,bg='black')
    test2page.rowconfigure((0,1,2,3,4,5,6,7),weight=1)
    test2page.columnconfigure((0,1,2,3),weight=1)
    test2page.grid(row=1,rowspan=3,column=0,columnspan=4,sticky='news')
    
    Label(test2page,text='Are you secretly the most pridful prick to ever exist?',bg='black',fg='white',font='Kanit 20 bold').grid(row=1,column=0,columnspan=4)

    Button(test2page,text='Yes',image=img7,bd=0,bg='black',activebackground='black',compound=CENTER,command=a2).grid(row=2,column=0,columnspan=2,sticky='e',ipadx=10)
    Button(test2page,text='No',image=img7,bd=0,bg='black',activebackground='black',compound=CENTER,command=a9).grid(row=2,column=2,columnspan=2,sticky='w',ipadx=10)

def a2():
    global test2page
    test2page=Frame(homeframe,bg='black')
    test2page.rowconfigure((0,1,2,3,4,5,6,7),weight=1)
    test2page.columnconfigure((0,1,2,3),weight=1)
    test2page.grid(row=1,rowspan=3,column=0,columnspan=4,sticky='news')

    Label(test2page,text='congratulations\nyou got',bg='black',fg='white',font='Kanit 30 bold').grid(row=1,column=0,columnspan=4)

    sql = "select * from userinfo where username=?;"
        #execute step
    cursor.execute(sql,[user_result[0]])
        #fetch result
    result = cursor.fetchone()
    if result :
        #define sql select command of course name for duplicating
        sql = "select * from userinfo where username=?;"
        #execute step
        cursor.execute(sql,[user_result[0]])
            #fetch result
        result = cursor.fetchone()

        if result :
                #define sql for updating of day,room fields
            sql = """
                                update userinfo
                                set enneagrame=?
                                where username=?;
            """
            eng = 'type 2'  
                #execute step
            cursor.execute(sql,[eng,user_result[0]])
                #commit step
            conn.commit()

    Label(test2page,text='type 2',bg='black',fg='white',font='Kanit 50 bold').grid(row=2,rowspan=2,column=0,columnspan=4)

    linken = Label(test2page, text="<< Learn about Enneagram here >>",bg='black',fg='white',font='Kanit 30 bold', cursor="hand2")
    linken.grid(row=4,rowspan=2,column=0,columnspan=4)
    linken.bind("<Button-1>", lambda e:callback("https://www.urbinner.com/post/what-is-enneagram"))

def a9():
    global test2page
    test2page=Frame(homeframe,bg='black')
    test2page.rowconfigure((0,1,2,3,4,5,6,7),weight=1)
    test2page.columnconfigure((0,1,2,3),weight=1)
    test2page.grid(row=1,rowspan=3,column=0,columnspan=4,sticky='news')

    Label(test2page,text='congratulations\nyou got',bg='black',fg='white',font='Kanit 30 bold').grid(row=1,column=0,columnspan=4)

    sql = "select * from userinfo where username=?;"
        #execute step
    cursor.execute(sql,[user_result[0]])
        #fetch result
    result = cursor.fetchone()
    if result :
        #define sql select command of course name for duplicating
        sql = "select * from userinfo where username=?;"
        #execute step
        cursor.execute(sql,[user_result[0]])
            #fetch result
        result = cursor.fetchone()

        if result :
                #define sql for updating of day,room fields
            sql = """
                                update userinfo
                                set enneagrame=?
                                where username=?;
            """
            eng = 'type 9'  
                #execute step
            cursor.execute(sql,[eng,user_result[0]])
                #commit step
            conn.commit()

    Label(test2page,text='type 9',bg='black',fg='white',font='Kanit 50 bold').grid(row=2,rowspan=2,column=0,columnspan=4)

    linken = Label(test2page, text="<< Learn about Enneagram here >>",bg='black',fg='white',font='Kanit 30 bold', cursor="hand2")
    linken.grid(row=4,rowspan=2,column=0,columnspan=4)
    linken.bind("<Button-1>", lambda e:callback("https://www.urbinner.com/post/what-is-enneagram"))
    
def test2back():
    homepage()

################################################

def enterPF():
    global profilepage

    profilepage=Frame(root,bg='black')
    profilepage.rowconfigure((0,1,2,3,4,5,6,7,8),weight=1)
    profilepage.columnconfigure((0,1,2),weight=1)
    profilepage.grid(row=0,column=0,rowspan=4,columnspan=4,sticky='news')

    Label(profilepage,image=img12,bg='black').grid(row=0,column=0,columnspan=3)

    Label(profilepage,text='Username:',fg='white',font='Kanit 20 bold',bg='black').grid(row=1,column=0,sticky='e')
    Label(profilepage,text=user_result[0],fg='white',font='Kanit 20 bold',bg='black').grid(row=1,column=1,sticky='w',padx=10)

    Label(profilepage,text='Name:',fg='white',font='Kanit 20 bold',bg='black').grid(row=2,column=0,sticky='e')
    Label(profilepage,text=user_result[2]+' '+user_result[3],fg='white',font='Kanit 20 bold',bg='black').grid(row=2,column=1,sticky='w',padx=10)
    
    Label(profilepage,text='Gender:',fg='white',font='Kanit 20 bold',bg='black').grid(row=3,column=0,sticky='e')
    Label(profilepage,text=user_result[4],fg='white',font='Kanit 20 bold',bg='black').grid(row=3,column=1,sticky='w',padx=10)

    Label(profilepage,text='Personality:',fg='white',font='Kanit 20 bold',bg='black').grid(row=4,column=0,sticky='e')

    Label(profilepage,text=user_result[5],image=img13,fg='white',font='Kanit 20 bold',bg='black',compound=TOP).grid(row=5,column=1,sticky='nw',padx=10)
    Label(profilepage,text=user_result[6],image=img14,fg='white',font='Kanit 20 bold',bg='black',compound=TOP).grid(row=5,column=1,columnspan=2,sticky='n',padx=10)

    Button(profilepage,text='BACK',image=img7,bd=0,bg='black',fg='black',font='Kanit 25 bold',activebackground='black',compound=CENTER,command=profileexite).grid(row=8,column=2)
    

def profileexite():
    profilepage.destroy()



#ัฟงกชั่นปุ่ม forgot password
def forgotclick():
    global forgotpage,usernameent,npass,cnpass
    forgotpage=Frame(root,bg='black')
    forgotpage.rowconfigure((0,1,2,3,4,5),weight=1)
    forgotpage.columnconfigure((0,1,2),weight=1)
    forgotpage.grid(row=0,column=0,rowspan=4,columnspan=4,sticky='news')

    #ที่ระบุ uesrname
    Label(forgotpage,text='Enter username:',bg='black',fg='white',font='Kanit 15 bold').grid(row=0,column=0,sticky='e')
    usernameent = Entry(forgotpage)
    usernameent.grid(row=0,column=1)

    Label(forgotpage,text='Enter password:',bg='black',fg='white',font='Kanit 15 bold').grid(row=1,column=0,sticky='e')
    npass = Entry(forgotpage)
    npass.grid(row=1,column=1)

    Label(forgotpage,text='Confirm password:',bg='black',fg='white',font='Kanit 15 bold').grid(row=2,column=0,sticky='e')
    cnpass = Entry(forgotpage)
    cnpass.grid(row=2,column=1)

    changebt = Button(forgotpage,text='change password',image=img5,bd=0,bg='black',fg='black',font='Kanit 25 bold',activebackground='black',compound=CENTER,command=changeclick)
    changebt.grid(row=3,column=0,columnspan=3)



def homeexit():
    homeframe.destroy()
    userentry.delete(0, END)
    pwdentry.delete(0, END)
    userentry.focus_force()

#button for change password
def changeclick():
    if usernameent.get() == "" or npass.get() == "" or cnpass.get() == "":
        messagebox.showwarning("Admin: ","Please fill in the blank")
        usernameent.focus_force()
    else :
        #define sql select command to checking course code exist or not
        sql = "select * from userinfo where username=?;"
        #execute step
        cursor.execute(sql,[usernameent.get()])
        #fetch result
        result = cursor.fetchone()
        if result :
            #define sql select command of course name for duplicating
            sql = "select * from userinfo where username=?;"
            #execute step
            cursor.execute(sql,[usernameent.get()])
            #fetch result
            result = cursor.fetchone()

            if result :
                #define sql for updating of day,room fields
                sql = """
                                update userinfo
                                set password=?
                                where username=?;
                """
                #execute step
                cursor.execute(sql,[npass.get(),usernameent.get()])
                #commit step
                conn.commit()
                messagebox.showinfo("Admin:","Update password successfully")
        else :
            messagebox.showwarning("Admin: ","Username not found please try again.")
            usernameent.select_range(0,END)
            usernameent.focus_force()

    forgotpage.destroy()

#ัฟงกชั่นปุ่ม cancle หน้าlogin
def cancleloginclick():
    loginmenu.destroy()

#ัฟงกชั่นปุ่ม cancle หน้าlogin
def cancleregisclick():
    regismenu.destroy()
    





createconnection()
root = mainwindow()

img1 = PhotoImage(file='images\logo.png')
img2 = PhotoImage(file='images\login_pic.png').subsample(8,8) 
img3 = PhotoImage(file='images/bg.png')
img4 = PhotoImage(file='images\cancle.png')
img5 = PhotoImage(file='images/forBT1.png').subsample(3,3) 
img6 = PhotoImage(file='images/forBT1.png').subsample(4,4)
img7 = PhotoImage(file='images/forBT1.png').subsample(7,7)  
img8 = PhotoImage(file='images/regishead.png')  
img9 = PhotoImage(file='images/regisnow.png').subsample(2,2) 
img10 = PhotoImage(file='images\CF.png').subsample(2,2)  #test 1
img11 = PhotoImage(file='images\ENG.png').subsample(2,2)  #test 2
img12 = PhotoImage(file='images\pf_head.png')
#pic for profile
img13 = PhotoImage(file='images\CF.png').subsample(4,4)  #test 1
img14 = PhotoImage(file='images\ENG.png').subsample(4,4)  #test 2

userinfo = StringVar() #spy for username
pwdinfo = StringVar() #spy for password
Gender = StringVar() #spy for gender

widgedlogin()

root.mainloop()
cursor.close()
conn.close()