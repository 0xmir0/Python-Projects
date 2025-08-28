import sys
import sqlite3

########## setting-up DB 
try :
   db = sqlite3.connect("app.db")     
   cr = db.cursor()
   cr.execute("create table if not exists students (user_ID integer ,name text , grade text , paidmonths json ,absentdays intger)")
except :
    print("An error occured in the DB...")

########## dicts to ease access  
months ={1: "january",2 :"february", 3 : "March",4 : "April", 5 : "May", 6 : "June",7 :"July" ,8 :"Augast" ,9 :"September" ,10 :"October" ,11 :"November" ,12 :"December",}
grades_dict = {1: "1-preporatory", 2 : "2-preporatory", 3 : "3-preporatory", 4 : "1-secondary",5 :"2-secondary", 6 : "3-secondary",}

########### absent option : SQL  ###################

def absent_option() :
    try :
        print(" [1] Taking absent for a student.\n [2] Taking absent for a whole class.\n [3] View absent of all students.")
        ch1 = int(input("what do you want ?  : "))
        if ch1 == 1 :
            absent_student()
        elif ch1 == 2 :
            absent_class()
        elif ch1 == 3 :
            absent_class_table()
        else :
            print ("Wrong option....")

    except :
        pass

def absent_class() :
    while True :
        try :
            absent_class_id = int(input("Enter student id : "))
            cr.execute(f"select name,absentdays from students where user_ID = {absent_class_id}")
            absent_data = cr.fetchone()
            cr.execute(f"update students set absentdays = {absent_data[1]+1} where user_ID = {absent_class_id}")
            print(f"Total absent days of {absent_data[0]} is : {absent_data[1]+1}")
        except :
            absent_error_id_q  = input("wrong id number...\n Do you want to try again..[y/N]")
            if absent_error_id_q == "y" :
                continue
            else : break        

def absent_student() :
    while True :
        try :
            absent_student_id = int(input("Enter student id : "))
            cr.execute(f"select name,absentdays from students where user_ID = {absent_student_id}")
            absent_data = cr.fetchone()
            cr.execute(f"update students set absentdays = {absent_data[1]+1} where user_ID = {absent_student_id}")
            print(f"Total absent days of {absent_data[0]} is : {absent_data[1]+1}")
            ch = input("do you want to add another student? [y/N] ")
            if ch == 'y' : 
                absent_student()
            else :
                pass
        except KeyboardInterrupt :
            pass
        except :
            absent_error_id_q  = input("wrong id number...\n Do you want to try again..[y/N]")
            if absent_error_id_q == "y" :
                continue
            else : break     

def absent_class_table() :
    cr.execute(f"select name,absentdays from students")
    absent_data = cr.fetchall()
    for name,absent in absent_data :
        print (f"{name} absent days are {absent}")

############ addind user : SQL #######################

def addUser() :
    name = input("input Student name...: ")
    print("\n[1] 1-preparatory \n[2] 2-preparatory \n[3] 3-preparatory\n[4] 1-secondary \n[5] 2-secondary \n[6] 3-secondary\n[7] Exit to main menu.")
    while True :
        try : 
            try :
                grade_adding_input = int(input("Choose grade  num...: "))
                grade = grades_dict[grade_adding_input]
                paid_months_q = input("Have he paid any months ? [y/N]").lower()
                paid_months = "none"
                if paid_months_q == "y" :
                    paid_months = (input("what months ? [ Hint :please input in this format 1, 2, etc ] :  ")).strip()
                else : pass
                absentdays_q = input("Do you want to add absentdays? [y/N]")
                absentdays = 0
                if absentdays_q == "y" :
                    absentdays = int(input("how many days..? "))
                else : pass
            except :
                print("wrong number chosen..")
                grade_wrong_q = input("do you wanna try again...[y/N]")
                if grade_wrong_q == "y" : continue
                else : break
            try :
                cr.execute("select * from students")
                result = cr.fetchall()
                global new_id 
                new_id = (int(result[-1][0])+1)
            except IndexError : 
                new_id = 1
            try :
                cr.execute(f"insert into students( user_ID, name , grade, paidmonths, absentdays) values({new_id},  '{name}', '{grade}' , '{paid_months}', {absentdays})")
                db.commit()
                print(f"student successfully added with id : {new_id}")
            except :
                print("error adding student...")
            break
        except :
            print("Error adding student")

############ searching user : SQL ####################

def search_Student() :
    """searching student through the database by the user id"""
    while True : 
        try :
            ID_search_student = int(input("input student ID : "))
        except :
            print("only numbers accepted..")
            search_student_error_if =input("do you want try again..[y/N]")
            if search_student_error_if == "y" :continue
            else : break
        try :
            cr.execute(f"select * from students where user_ID = {ID_search_student}")
            resutls_of_searching_student = cr.fetchall()
            for id,name,grade,paidmonth,absentdays in resutls_of_searching_student :
                print(f"Student Found \n\n\tName is {name} and id : {id} \n\tpaid months : {paidmonth} \n\tand absentdays : {absentdays}")
            search_student_if_q = input("Do you want to search for another student...[y/N]")
            if search_student_if_q == "y" :
                continue
            else : break
        except :
            no_student_found_search_q = input("Error this id doesnt exist..\n Do you want to add a student..[y/N]")
            if no_student_found_search_q == "y" : addUser()
            else :break

############ Money Section : ####################
def money_section() :
    while True : 
        try :
            print( "##### Money Section #####\n\n [1] Collct Money.\n [2] check if student paid.\n [3] list paid student from spacific grade.\n [4] Exit to main menu\n")
            money_section_choice = int(input("choose what you want ..: "))
            if money_section_choice == 1 :
                collect_money()
            elif money_section_choice == 2 :
                is_student_paid()
            elif money_section_choice == 3 :
                paid_grade()
            elif money_section_choice == 3 :
                break
            else : 
                print("wrong option...")
        except KeyboardInterrupt :
            break
        except :
            print("only number accepted.")
            input("press enter to retry.. ")

def is_student_paid():
    pass
        
def collect_money() :
    pass

def paid_grade() :
    print("\n[1] 1-preporatory \n[2] 2-preporatory \n[3] 3-preporatory\n[4] 1-secondary \n[5] 2-secondary \n[6] 3-secondary\n[7] Exit to main menu.")
    grade_select_whole_listing = int(input("select grade number :"))
    paid_month_choice = input("select month (in numbers): ").strip()
    cr.execute(f"select * from students ")
    results = cr.fetchall()
    for id,name,grade,paidmonth,absent in results :
        if grade == grades_dict[grade_select_whole_listing] :
            if paidmonth == 'none' : continue
            else :
                paid_month_list = paidmonth.split()    
                if paid_month_choice in paid_month_list :
                    print(f"\t{name} with id : {id}")
    input("press enter to continue....")

############ listing a whole grade students : SQL ####################

def whole_grade_viewing() : 
    grade_select_whole_listing = int(input("select grade number :"))
    cr.execute(f"select * from students ")
    results = cr.fetchall()
    for id,name,grade,paidmonth,absent in results :
        if grade == grades_dict[grade_select_whole_listing] :
            print(f"student name : {name} with id : {id}")
    input("press enter to continue....")

############ main function page : SQL ####################

def main_page() :
    while True :
        try : 
            #os.system("clear")
            print ("\n..... Welcome Mr Miro , how are you today ? .....")
            print (" [1] Adding a student.\n [2] searching an existing student.\n [3] viewing a whole grade.\n [4] Paid Students. \n [5] Absent Table. \n [6] Money Section. \n [7] Exit")
            main_page_choice = int(input ("what do you want to ? : "))
            if main_page_choice == 1 :   addUser()
            elif main_page_choice == 2 : search_Student()
            elif main_page_choice == 3 : whole_grade_viewing()
            elif main_page_choice == 4 : collect_money()
            elif main_page_choice == 5 : absent_option()
            elif main_page_choice == 6 : money_section()
            elif main_page_choice == 7 : break
            else :
                #wrong choice 
                print("You should choose the number in the practs")
        except KeyboardInterrupt :
            #os.system("clear")
            break
        except : 
            #os.system("clear")
            print("wrong oprion.gg..")


main_page()



