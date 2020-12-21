
import mysql.connector as conn

#SignIn Module
def regester_data(mydb):
    mycursor = mydb.cursor()
    roll_no = input('Enter User_Rollno = ')
    user_name = input('Enter your name = ')
    semester = input('Enter your semester = ')
    password = input('Enter Password = ')
    s1="select * from student_info where roll_no=%s"
    b1=(roll_no,)
    mycursor.execute(s1, b1)
    validate=mycursor.fetchall()
    if(len(validate)==0):
        s2 = "insert into student_info values(%s,%s,%s,%s)"
        b2 = (roll_no, user_name , semester, password)
        mycursor.execute(s2, b2)
        print("You have register successfully now you can enter the system by log-in")
        mydb.commit()
    else:
        print("You are already registered...")


#LoGIN Module___________________________________________________________
def check_authentication(mydb):
    roll_no = input('Enter User_Rollno = ')
    password = input('Enter Password = ')
    mycursor = mydb.cursor()
    s = "select * from student_info where roll_no=%s and pwd=%s"
    b1 = (roll_no, password)
    mycursor.execute(s, b1)
    validate =mycursor.fetchall()
    if(len(validate)!=0):
        print("Hi ",roll_no," you logged_in successfully in the system!!!!")
        choice='0'
        while(choice!='8'):
            print('1. press 1 for Select Courses \n2. press 2 for Drop Courses \n3. press 3 for Dashboard '
                  '\n4. press 4 for View Transcript \n5. press 5 for Examination \n6. press 6 for View Attendance '
                  '\n7. press 7 for View current courses ' '\n8. press 8 for Exit')
            choice=input("Enter your choice = ")
            if(choice =='1'):
                select_courses(roll_no,mydb)
            elif (choice=='2'):
                drop(roll_no,mydb)
            elif(choice=='3'):
                display_dashboard(roll_no,mydb)
            elif(choice=='4'):
                show_transcript(roll_no,mydb)
            elif (choice == '5'):
                show_eligibility(roll_no, mydb)
            elif (choice == '6'):
                show_attendence(roll_no, mydb)
            elif (choice == '7'):
                show_courses(roll_no, mydb)



    else:
        print('Invalid username or password. try again')

#1Select_courses Module___________________________________________________________

from datetime import datetime
def select_courses(roll_no,mydb):
   #check deadline i.e 30th october
    today = datetime.now()
    if today < datetime(2020, 10, 30):
        mycursor = mydb.cursor()
        s="select * from  courses_info"
        mycursor.execute(s)
        courses=mycursor.fetchall()
        print("Available courses for you : ")
        print("course_id  course_name Department  type credits")

        for row in courses:
            print(row)
        course_id=input("Enter the course id which you want to register for = ")
        try:
            s1= "select credits from selected_courses where roll_no=%s and (status=%s or status=%s)"
            b=(roll_no,"current","repeat")
            mycursor.execute(s1,b)
            count=mycursor.fetchall()
            sum=0
            for i in count:
                sum+=i[0]

            s1 = "select credits from courses_info where course_id=%s"
            b = (course_id,)
            mycursor.execute(s1, b)
            count = mycursor.fetchall()
            sum+=count[0][0]
            print("current credit is", sum)
            # checks that total credit exceed the maximum credit or not
            if sum <= 14:
                s2="select * from selected_courses where roll_no = %s and course_id=%s"
                b=(roll_no,course_id)
                mycursor.execute(s2, b)
                validate=mycursor.fetchall()
                # checks course is already taken or not
                if(len(validate)==0):
                    s3="select type,credits from courses_info where course_id=%s"
                    b=(course_id,)
                    mycursor.execute(s3,b)
                    ty_cr=mycursor.fetchall()
                    s3="insert into selected_courses values(%s,%s,%s,%s,%s,%s,%s)"
                    b = (roll_no, course_id, 0, 'NULL', ty_cr[0][0], 'current',ty_cr[0][1])
                    mycursor.execute(s3, b)
                    mydb.commit()

                else:
                    s="select status from selected_courses where roll_no=%s and course_id=%s"
                    b=(roll_no,course_id)
                    mycursor.execute(s, b)
                    status=mycursor.fetchall()
                    if status[0][0]=="completed":
                        print(" You have already completed this course")
                        v=input("Do you want to repeat the course again??Enter Y or N")
                        if v=="Y":
                            s3 = "select type,credits from courses_info where course_id=%s"
                            b = (course_id,)
                            mycursor.execute(s3, b)
                            ty_cr = mycursor.fetchall()
                            s3 = "insert into selected_courses values(%s,%s,%s,%s,%s,%s,%s)"
                            b1 = (roll_no, course_id, 0, 'NULL', ty_cr[0][0], 'repeat',ty_cr[0][1])
                            mycursor.execute(s3, b1)
                            mydb.commit()
                        else:
                            pass
                    else:
                            print("you already dropped or repeated or already taken this course in current sem")
            else :
                print("you have exceeded the maximum credit limit")
        except:
            print("enter valid course id")
    else:
        print("Deadline is over for Add/Drop Week")



#2DropCourses------------------------------------------------------------------------------
from datetime import datetime
def drop(roll_no,mydb):
    today = datetime.now()
    if today < datetime(2020, 10, 30):
        mycursor = mydb.cursor()
        print("Enter Course_id which you want to drop")
        c_id = input()
        s=" select * from selected_courses where course_id=%s and roll_no=%s and (status!=%s and status!=%s)"
        b=(c_id,roll_no,"completed","dropped")
        mycursor.execute(s,b)
        data=mycursor.fetchall()
        if len(data)!=0:
            s = "update selected_courses set status=%s where roll_no=%s and course_id=%s "
            b = ("dropped",roll_no,c_id)
            mycursor.execute(s, b)
            mydb.commit()
            print("Dropped Successfully")
        else:
            print("You have not enrolled in this course OR You have completed the course")
    else:
        print("Deadline is over for Add/Drop Week")

#3DashBoard Module___________________________________________________________________
from prettytable import PrettyTable


def display_dashboard(roll_no, mydb):
    s = 'select * from student_info where roll_no=%s'
    b = (roll_no,)
    mycursor = mydb.cursor()
    mycursor.execute(s, b)
    data = mycursor.fetchall()
    t = PrettyTable(['Rollno', 'Student-Name', 'Semester', 'Password'])
    for i in data:
        t.add_row([i[0], i[1], i[2], i[3]])
    print(t)
    v = input("Do You want to change password? Enter Y or N ")
    if v == "Y":
        pwd = input("enter new password")
        s = "update student_info set pwd=%s where roll_no=%s  "
        b = (pwd, roll_no)
        mycursor.execute(s, b)
        mydb.commit()
        print("Password changed Successfully !!!")
    else:
        pass


#4TranscriptModule------------------------------------------------------------------

from prettytable import PrettyTable
def show_transcript(roll_no,mydb):
    mycursor = mydb.cursor()
    s="select course_id,grade,status from selected_courses where roll_no=%s"
    b=(roll_no,)
    mycursor.execute(s,b)
    data=mycursor.fetchall()
    if len(data) != 0:

        t = PrettyTable(['CoursID', 'Grade','Status'])
        for i in data:
            t.add_row([i[0], i[1], i[2]])
        print(t)

    else:
        print("Currrently not enrolled to any course")
#5Examination________________________________________________________________________________
def show_eligibility(roll_no,mydb):
    mycursor = mydb.cursor()
    s = "select course_id from selected_courses where roll_no=%s and (type=%s or type=%s) and attendence>%s"
    b = (roll_no,"regular","repeat",70)
    mycursor.execute(s, b)
    data = mycursor.fetchall()
    if len(data)!=0:
        for i in data:
            print(i[0])
        print("______________")
    else:
        print("You are not eligible for exam!")
#6Attendence______________________________________________________________
def show_attendence(roll_no,mydb):
    mycursor = mydb.cursor()
    s = "select attendence,course_id from selected_courses where roll_no=%s and (status=%s or status=%s)"
    b = (roll_no,"current","repeat")
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
def show_courses(roll_no,mydb):
    mycursor = mydb.cursor()
    s="select course_id ,status,type,credits from selected_courses where roll_no=%s and (status=%s or status=%s)"
    b=(roll_no,"current","repeat")
    mycursor.execute(s,b)
    data = mycursor.fetchall()
    if len(data) != 0:
        print("your current courses are:")
        t = PrettyTable(['Course_ID', 'Status', 'Type', 'Credits'])
        for i in data:
            t.add_row([i[0], i[1], i[2], i[3]])
        print(t)
        s="select sum(credits) from selected_courses where roll_no=%s and (status=%s or status=%s)"
        b=(roll_no,"current","repeat")
        mycursor.execute(s,b)
        credit=mycursor.fetchall()
        print("Total Credits :",credit[0][0])
    else:
        print("Currently not enrolled in any course")


#Main----------------------------------------------------------------
if __name__=='__main__':
    choice='0'
    mydb=conn.connect(host="localhost",user="root",passwd="1234",database="oopd_project_data")
    while(choice!='3'):
        print("\n\n             Welcome to Student Regestration System         ")
        print("1. press 1 for sign-UP \n2. press 2 for Log_in \n3. press 3 for Exit")
        choice=input("Enter your choice : ")
        if(choice=='2'):
            check_authentication(mydb)
        elif(choice=='1'):
            regester_data(mydb)
            mydb.commit()