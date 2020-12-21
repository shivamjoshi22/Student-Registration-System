from prettytable import PrettyTable
class user:
    def __init__(self,name,password):
        self.__name=name
        self.__pwd=password
    def get_name(self):
        return self.__name
    def get_pwd(self):
        return  self.__pwd

#Student Class
class Student (user) :

    def __init__(self,name,rollno,sem,pwd):
        super().__init__(name,pwd)
        #self.__name=name #private_variables
        self.__rollno=rollno
        self.__sem=sem
        #self.__pwd=pwd

    def get_rollno(self):
        return self.__rollno
    def get_details(self):
        return super().get_name(),self.__sem,self.__rollno,super().get_pwd()
#change-PWD
class chg_pwd:
    def __init__(self,mydb,s):
        self.__mydb=mydb
        self.__s = s
    def change_pwd(self):
        Rollno, Student_Name, Semester, Password = self.__s.get_details()
        pwd = input("enter new password")
        s = "update student_info set pwd=%s where roll_no=%s  "
        b = (pwd, Rollno)
        mycursor = self.__mydb.cursor()
        mycursor.execute(s, b)
        self.__mydb.commit()
        print("Password changed Successfully !!!")
        return '8'

#SignIn Module
class sign_up:
    def __init__(self,mydb):
        self.__mydb=mydb

    def regester_data(self,):
        mycursor = self.__mydb.cursor()
        roll_no = input('Enter User_Rollno = ')
        user_name = input('Enter your name = ')
        semester = input('Enter your semester = ')
        password = input('Enter Password = ')
        s1 = "select * from student_info where roll_no=%s"
        b1 = (roll_no,)
        mycursor.execute(s1, b1)
        validate = mycursor.fetchall()
        if (len(validate) == 0):
            s2 = "insert into student_info values(%s,%s,%s,%s)"
            b2 = (roll_no, user_name, semester, password)
            mycursor.execute(s2, b2)
            print("You have register successfully now you can enter the system by log-in")
            self.__mydb.commit()
        else:
            print("You are already registered...")



#LoGIN Module___________________________________________________________
class Log_in:
    def __init__(self,mydb):
        self.__mydb=mydb

    def check_authentication(self):
        roll_no = input('Enter User_Rollno = ')
        password = input('Enter Password = ')
        mycursor = self.__mydb.cursor()
        s = "select * from student_info where roll_no=%s and pwd=%s"
        b1 = (roll_no, password)
        mycursor.execute(s, b1)
        validate = mycursor.fetchall()
        if (len(validate) != 0):
            print("Hi ", roll_no, " you logged_in successfully in the system!!!!")
            choice = '0'
            while (choice != '8'):
                print('1. press 1 for Select Courses \n2. press 2 for Drop Courses \n3. press 3 for Dashboard '
                      '\n4. press 4 for View Transcript \n5. press 5 for Examination \n6. press 6 for View Attendance '
                      '\n7. press 7 for View current courses ' '\n8. press 8 for Exit')

                s1=Student(validate[0][0],validate[0][1],validate[0][2],validate[0][3])
                choice = input("Enter your choice = ")
                if (choice == '1'):
                    s=SelectCourses(self.__mydb,s1)
                    s.select_courses()
                elif (choice == '2'):
                    d=DropCourse(self.__mydb,s1)
                    d.drop()
                elif (choice == '3'):
                    d=Dashboard(self.__mydb,s1)
                    choice =d.print_details()
                elif (choice == '4'):
                    t=Transcript(self.__mydb,s1)
                    t.show_transcript()
                elif (choice == '5'):
                    e=Eligibility(self.__mydb,s1)
                    e.show_eligibility()
                elif (choice == '6'):
                    a=Attendence(self.__mydb,s1)
                    a.show_attendence()
                elif (choice == '7'):
                    s = ShowCourses(self.__mydb,s1)
                    s.show_courses()

        else:
          print('Invalid username or password. try again')

#1Select_courses Class___________________________________________________________
class SelectCourses:
    def __init__(self,mydb,s):
        self.__mydb=mydb
        self.__s = s
    def select_courses(self):
        Rollno, Student_Name, Semester, Password=self.__s.get_details()

        today = datetime.now()
        if today < datetime(2020, 12, 20):
            mycursor = self.__mydb.cursor()
            s = "select * from  courses_info"
            mycursor.execute(s)
            courses = mycursor.fetchall()
            print("Available courses for you : ")
            t = PrettyTable(["course_id" , "course_name", "Department",  "type" ,"credits"])
            for i in courses:
               t.add_row([i[0],i[1], i[2], i[3],i[4]])
            print(t)
            course_id = input("Enter the course id which you want to register for = ")
            try:
                s1 = "select credits from selected_courses where roll_no=%s and (status=%s or status=%s)"
                b = (Rollno, "current", "repeat")
                mycursor.execute(s1, b)
                count = mycursor.fetchall()
                sum = 0
                for i in count:
                    sum += i[0]

                s1 = "select credits from courses_info where course_id=%s"
                b = (course_id,)
                mycursor.execute(s1, b)
                count = mycursor.fetchall()
                sum += count[0][0]
                print("current credit is", sum)
                # checks that total credit exceed the maximum credit or not
                if sum <= 14:
                    s2 = "select * from selected_courses where roll_no = %s and course_id=%s"
                    b = (Rollno, course_id)
                    mycursor.execute(s2, b)
                    validate = mycursor.fetchall()
                    # checks course is already taken or not
                    if (len(validate) == 0):
                        s3 = "select type,credits from courses_info where course_id=%s"
                        b = (course_id,)
                        mycursor.execute(s3, b)
                        ty_cr = mycursor.fetchall()
                        s3 = "insert into selected_courses values(%s,%s,%s,%s,%s,%s,%s)"
                        b = (Rollno, course_id, 70, 'NULL', ty_cr[0][0], 'current', ty_cr[0][1])
                        mycursor.execute(s3, b)
                        self.__mydb.commit()

                    else:
                        s = "select status from selected_courses where roll_no=%s and course_id=%s"
                        b = (Rollno, course_id)
                        mycursor.execute(s, b)
                        status = mycursor.fetchall()
                        if status[0][0] == "completed":
                            print(" You have already completed this course")
                            v = input("Do you want to repeat the course again??Enter Y or N")
                            if v == "Y":
                                s3 = "select type,credits from courses_info where course_id=%s"
                                b = (course_id,)
                                mycursor.execute(s3, b)
                                ty_cr = mycursor.fetchall()
                                s3 = "insert into selected_courses values(%s,%s,%s,%s,%s,%s,%s)"
                                b1 = (Rollno, course_id, 0, 'NULL', ty_cr[0][0], 'repeat', ty_cr[0][1])
                                mycursor.execute(s3, b1)
                                self.__mydb.commit()
                            else:
                                pass
                        else:
                            print("you already dropped or repeated or already taken this course in current sem")
                else:
                    print("you have exceeded the maximum credit limit")
            except:
                print("enter valid course id")
        else:
            print("Deadline is over for Add/Drop Week")

#2DropCourses------------------------------------------------------------------------------
from datetime import datetime
class DropCourse:
        def __init__(self, mydb,s):
            self.__mydb = mydb
            self.__s = s


        def drop(self):
            Rollno, Student_Name, Semester, Password = self.__s.get_details()
            today = datetime.now()
            if today < datetime(2020, 12, 20):
                mycursor = self.__mydb.cursor()
                print("Enter Course_id which you want to drop")
                c_id = input()
                s = " select * from selected_courses where course_id=%s and roll_no=%s and (status!=%s and status!=%s)"
                b = (c_id, Rollno, "completed", "dropped")
                mycursor.execute(s, b)
                data = mycursor.fetchall()
                if len(data) != 0:
                    s = "update selected_courses set status=%s where roll_no=%s and course_id=%s "
                    b = ("dropped", Rollno, c_id)
                    mycursor.execute(s, b)
                    self.__mydb.commit()
                    print("Dropped Successfully")
                else:
                    print("You have not enrolled in this course OR You have completed the course")
            else:
                print("Deadline is over for Add/Drop Week")



#3DashBoard Module___________________________________________________________________
from prettytable import PrettyTable

class Dashboard:
    def __init__(self,mydb,s):
        self.__mydb=mydb
        self.__s=s
    def print_details(self):
        Rollno,Student_Name,Semester,Password=self.__s.get_details()
        t = PrettyTable(['Rollno', 'Student-Name', 'Semester', 'Password'])
        t.add_row([Rollno,Student_Name,Semester,Password])
        print(t)
        v = input("Do You want to change password? Enter Y or N ")
        if v == "Y":
            obj=chg_pwd(self.__mydb,self.__s)
            return obj.change_pwd()
        else:
            return '9'


#4TranscriptModule------------------------------------------------------------------

from prettytable import PrettyTable
class Transcript:
    def __init__(self,mydb,s):
        self.__mydb=mydb
        self.__s = s

    def show_transcript(self):
        Rollno, Student_Name, Semester, Password = self.__s.get_details()
        mycursor = self.__mydb.cursor()
        s="select course_id,grade,status from selected_courses where roll_no=%s"
        b=(Rollno,)
        mycursor.execute(s,b)
        data=mycursor.fetchall()
        if len(data) != 0:

            t = PrettyTable(['CoursID', 'Grade','Status'])
            for i in range(len(data)):
                t.add_row([data[i][0], data[i][1], data[i][2]])
            print(t)

        else:
            print("Currrently not enrolled to any course")


#5Eligibility________________________________________________________________________________
class Eligibility:
    def __init__(self,mydb,s):
        self.__mydb=mydb
        self.__s = s
    def show_eligibility(self):
        Rollno, Student_Name, Semester, Password = self.__s.get_details()
        mycursor = self.__mydb.cursor()
        s = "select course_id from selected_courses where roll_no=%s and (status=%s or status=%s) and attendence>=%s"
        b = (Rollno,"current","repeat",70)
        mycursor.execute(s, b)
        data = mycursor.fetchall()
        if len(data)!=0:
            #print(data)
            for i in data:
                print(i[0])
            print("______________")
        else:
            print("You are not eligible for exam!")


#6Attendence______________________________________________________________
class Attendence:
    def __init__(self,mydb,s):
        self.__mydb=mydb
        self.__s = s
    def show_attendence(self):
        Rollno, Student_Name, Semester, Password = self.__s.get_details()
        mycursor = self.__mydb.cursor()
        s = "select attendence,course_id from selected_courses where roll_no=%s and (status=%s or status=%s)"
        b = (Rollno,"current","repeat")
        mycursor.execute(s, b)
        data = mycursor.fetchall()
        if len(data) != 0:
            for i in data:
                print(i[1],"Attendence=",i[0])
            print("______________")
        else:
            print("Currently not enrolled in any courses")


#7ViewCourses----------------------------------------------------------------

from prettytable import PrettyTable
class ShowCourses:
    def __init__(self,mydb,s):
        self.__mydb=mydb
        self.__s = s


    def show_courses(self):
        Rollno, Student_Name, Semester, Password = self.__s.get_details()
        mycursor = self.__mydb.cursor()
        s = "select course_id ,status,type,credits from selected_courses where roll_no=%s and (status=%s or status=%s)"
        b = (Rollno, "current", "repeat")
        mycursor.execute(s, b)
        data = mycursor.fetchall()
        if len(data) != 0:
            print("your current courses are:")
            t = PrettyTable(['Course_ID', 'Status', 'Type', 'Credits'])
            for i in data:
                t.add_row([i[0], i[1], i[2], i[3]])
            print(t)
            s = "select sum(credits) from selected_courses where roll_no=%s and (status=%s or status=%s)"
            b = (Rollno, "current", "repeat")
            mycursor.execute(s, b)
            credit = mycursor.fetchall()
            print("Total Credits :", credit[0][0])
        else:
            print("Currently not enrolled in any course")



#Application---------------------------------------------------------
class App:
    def __init__(self,mydb):
        self.mydb=mydb

    def load(self,):
        choice = '0'
        while (choice != '3'):
            print("\n\n             Welcome to Student Regestration System         ")
            print("1. press 1 for sign-UP \n2. press 2 for Log_in \n3. press 3 for Exit")
            choice = input("Enter your choice : ")
            if (choice == '1'):
                s = sign_up(self.mydb)
                s.regester_data()

            elif (choice == '2'):
                l=Log_in(self.mydb)
                l.check_authentication()







#Main----------------------------------------------------------------

import mysql.connector as conn
if __name__=='__main__':
    mydb=conn.connect(host="localhost",user="root",passwd="1234",database="oopd_project_data")
    A1=App(mydb)
    A1.load()

