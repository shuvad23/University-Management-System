#acadamic history******************************************************
from AutoGetStudentData import getStudentFunction
from GetDataManually import addManualData
from AddFIle import fileData,saveAdmissionInfo_FileData,savePaymentFileData,saveTeacherFileData
from RestoreData import restoreData,restorePaymentData
from UpdateStudentData import updateStudentData
from RemoveData import removeData
#Semester History******************************************************
from AdmissionInfo_tuition import admissionInfo_tuition
from PaymentHistory import paymentHistoryAll
from Payment import paymentInfo
#validation***********************************************************************
from Validation import validate_json_data
#export data********************************************************************
from export_data import export_to_csv,export_to_excel
#teacher data**********************************************************************
from teacher_info import getTeacherData
#view data**************************************************************************
from view_data import viewStudentData,viewTeacherData,viewSingleTeacherData,GetSemesterData,GetPaymentData

all_students=[]
admission_infoData=[]
payment_history=[]
teacher_infoData=[]
Filename="data/Student_info.json"
admissionFile="data/admission_info.json"
paymentFile="data/payment_info.json"
teacher_info_file="data/teacher_info.json"

# Base class: Person
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"
    
# Derived class: Student***********************************************************************************************************************
class Student(Person):
    def __init__(self, name, age,email,phone,student_ID,department,section,running_semester,total_course,subjects,grade,status):
        super().__init__(name, age)
        self.email=email
        self.phone=phone
        self.student_ID=student_ID
        self.department=department
        self.section=section
        self.running_semester=running_semester
        self.total_course=total_course
        self.subjects=subjects
        self.grade=grade
        self.status=status

    def display_info(self):
        base_info= super().display_info()
        return f"{base_info},Email: {self.email},Phone: {self.phone}, Student ID: {self.student_ID}, Department: {self.department}, Section: {self.section}, Semester: {self.running_semester}, Total Course: {self.total_course}, Grade: {self.grade}"
    def student_status(self):
        print(f"\n{self.name} Status :")
        print(f"\t {self.name} ({self.department},Section: {self.section},Running Semester: {self.running_semester})")
        print(f"\t*{self.name} belongs to {self.status}")
    def subjects_list(self):
        print(f"\n{self.name} Subject List :")
        # print(f"\t{self.subjects}")
        for view_data in self.subjects:
            print(f"\t{view_data} ({self.subjects[view_data]})")
    def single_view(self):
        print(f"{'*'*20} Single Information View {'*'*20}")
        print(f"*\t\t Name: {self.name}\t\t\tDepartment: {self.department}"
              f"\n*\t\t Age: {self.age}\t\t\t\tSection: {self.section}"
              f"\n*\t\t Email: {self.email}\t\tRunning Semester: {self.running_semester}"
              f"\n*\t\t Phone: {self.phone}\t\t\tTotal Courses: {self.total_course}"
              f"\n*\t\t Student ID: {self.student_ID}\t\t\tStatus: {self.status}")
        print("**************************** Subjects ***************************")
        for data in self.subjects:
            print(f"*\t{data}\t: {self.subjects[data]}")
        print("******************************************************************")
        
            
# Derived class: Teacher******************************************************************************************

class Teacher(Person):
    def __init__(self, name, age,gender,subject,department,expertise,salary,employment,experience):
        super().__init__(name, age)
        self.gender=gender
        self.subject=subject
        self.department=department
        self.expertise=expertise
        self.salary=salary
        self.employment=employment
        self.experience=experience
    def display_info(self):
        base_info= super().display_info()
        return f"{base_info}, Gender: {self.gender}, Subject: {self.subject}, Department: {self.department}, Expertise: {self.expertise}, Salary: {self.salary}, Employment Type: {self.employment}, Experience: {self.experience}"

#admission class****************************************************************
class Admission:
    def __init__(self,department,program_type,admission_fees,tuition_fees_per_year,tuition_fees_per_credit,semester_fees,additional_fees,scholarship_percentage):
        self.department=department
        self.program_type=program_type
        self.admission_fees=admission_fees
        self.tuition_fees_per_year=tuition_fees_per_year
        self.tuition_fees_per_credit=tuition_fees_per_credit
        self.semester_fees=semester_fees
        self.additional_fees=additional_fees
        self.scholarship_percentage=scholarship_percentage
    def semester_tuition_fees(self):
        print(f"*\t{self.department}: \t{self.program_type} \t TK.{self.admission_fees}/- \t\t TK.{self.tuition_fees_per_year}/- \t\t Tk.{self.tuition_fees_per_credit}/- \t\t TK.{self.semester_fees}/- \t  TK.{self.additional_fees}/- \t  {self.scholarship_percentage}%")

class Payment:
    def __init__(self,name,student_ID,total_course,department,grade,tuition_fees_per_credit,total_fees,payment,payment_due,payment_date):
        self.name=name
        self.student_ID=student_ID
        self.total_course=total_course
        self.department=department
        self.grade=grade
        self.tuition_fees_per_credit=tuition_fees_per_credit
        self.total_fees=total_fees
        self.payment=payment
        self.payment_due=payment_due
        self.payment_date=payment_date
    def display_info(self):
        print(f"*{self.department}: {self.name} \t\t{self.student_ID} \t\t\t{self.total_course} \t{self.grade} \t\t TK.{self.tuition_fees_per_credit}/- \t TK.{self.total_fees}/- \t Tk.{self.payment}/- \t TK.{self.payment_due}/- \t{self.payment_date}")





#main function*******************************************************************************************************************************
if __name__=="__main__":
    all_students,admission_infoData=restoreData(all_students,Filename,admission_infoData,admissionFile)
    payment_history=restorePaymentData(payment_history,paymentFile)
    while True:
        print(f"{'-'*50} University Management System {'-'*50}")
        print("\t\t  Student Information                          \tTuition and Payment History                  Teacher Information"
              "\n\t\t*************************                   *************************************         *************************"
              "\n\t\t 1. Get Data Automatically             *    \t a. Tuition And Fees                         11. Add Teacher info "
              "\n\t\t 2. Get Data Manually                  *    \t b. Payment History(All)                     12. View all teacher list"
              "\n\t\t 3. View All Data                      *    \t c. Payment History(Single)                  13. View Department teacher list"
              "\n\t\t 4. View Single Data                   *    \t d. Scholarship History"
              "\n\t\t 5. Total Data in 'Student Info' File  *    \t e. Payment"
              "\n\t\t 6. Update Student Data                *    \t f. Validate Json Data"
              "\n\t\t 7. Remove Student Data                *    \t g. ******************"
              "\n\t\t 8. Export to csv                      *    \t h. ******************"
              "\n\t\t 9. Export to Excel                    *    \t i. ******************"
              "\n\t\t 0. Exit() "
              f"\n{"-"*130}")
        
        # match /case *****************************************************************************************************
        option=input("Enter Your Option: ")
        match option:
            case '1':
                all_students=getStudentFunction(all_students)
                fileData(all_students,Filename)
                print(f"{'*'*50} Added Data Automatically Successfully {'*'*50}")
            
            case '2':
                all_students=addManualData(all_students)
                fileData(all_students,Filename)
                print(f"{'*'*50} Added Data Manually Successfully {'*'*50}")
            
            case '3':
                print(f"{'*'*50} View All Data {'*'*50}")
                viewStudentData(all_students)
            
            case '4':
                print(f"{'*'*50} View Single Data {'*'*50}")
                name=input("Enter Your Name: ")
                student_id=input("Enter Your Student ID: ")
                for singledata in all_students:
                    if(name==singledata['name'] and student_id==singledata['student_ID']):
                        student1=Student(singledata['name'], singledata['age'], singledata['email'], singledata['phone'], singledata['student_ID'], singledata['department'], singledata['section'],singledata['running_semester'], singledata['total_course'],singledata['subjects'],singledata['grade'],singledata['status'])
                        student1.single_view()
                        break

            case '5':
                print(f"Total Data in 'Student Info' File: {len(all_students)} ")
            
            case '6':
                all_students=updateStudentData(all_students)
                fileData(all_students,Filename)
                print(f"{'*'*50} Updated Data Successfully {'*'*50}")
            
            case '7':
                all_students,payment_history=removeData(all_students,payment_history,Filename,paymentFile)
                fileData(all_students,Filename)
                savePaymentFileData(payment_history,paymentFile)
                print(f"{'*'*50} Remove Data Successfully {'*'*50}")
            case '8':
                export_to_csv()

            case '9':
                export_to_excel()
            
            case '11':
                if(teacher_infoData==[]):
                    teacher_infoData=getTeacherData(teacher_infoData)
                    saveTeacherFileData(teacher_infoData,teacher_info_file)
                    print("Teacher Data added successfully.................")
                else:
                    print("Already added *****")
            case '12':
                viewTeacherData(teacher_infoData)
            case '13':
                department_name=input("Enter the Department name: ")
                viewSingleTeacherData(teacher_infoData,department_name)
            case 'a':
                if(admission_infoData==[]):
                    admission_infoData=admissionInfo_tuition(admission_infoData)
                    saveAdmissionInfo_FileData(admission_infoData,admissionFile)
                    GetSemesterData(admission_infoData)
                else:
                    GetSemesterData(admission_infoData)

                    #***************************For Update Section**********************************
                    # updatedata=input("Would you update admission information ?(y/n): ").lower()
                    # if(updatedata=='y'):
                    #     admission_infoData=[]
                    #     admission_infoData=semesterInfo_tuition(admission_infoData,admissionFile)
                    #     GetSemesterData(admission_infoData)

            case 'b':
                if(len(all_students)==len(payment_history)):
                    GetPaymentData(payment_history)
                else:
                    payment_history=paymentHistoryAll(all_students,admission_infoData,payment_history)
                    savePaymentFileData(payment_history,paymentFile)
                    GetPaymentData(payment_history)
            
            case 'c':
                payment_history=paymentHistoryAll(all_students,admission_infoData,payment_history)
                name=input("Enter Your Name: ")
                student_id=input("Enter Your Student ID: ")
                for singledata in payment_history:
                    if(name==singledata['name'] and student_id==singledata['student_ID']):
                        print(f"{'*'*80} Payment History ({singledata['name']}) {'*'*70}")
                        print("\tDepartment\t\t  Name\t\tStudent ID\tTotal Course\tGrade\tTuition Fee(Per Credit)\tTotal Fee\tPayment \tPayment Due\tPayment Date")
                        payment_info=Payment(singledata['name'],singledata['student_ID'], singledata['total_course'], singledata['department'], singledata['grade'], singledata['tuition_fees_per_credit'], singledata['total_fees'], singledata['payment'],singledata['payment_due'],singledata['payment_date'])
                        payment_info.display_info()
                        print("*"*180)
                        break

            case 'd':
                print(f"{"*"*50} Scholarship Recored {"*"*50}")
                for data in payment_history:
                    scholarship=0
                    if(data['grade']>=3.50):
                        for admissiondata in admission_infoData:
                            if(data['department'] in admissiondata['department']):
                                scholarship=admissiondata['scholarship_percentage']
                    print(f"* Department:{data['department']} Name: {data['name']}\tStudent_ID: {data['student_ID']} \tGrade: {data['grade']} \tScholarship: {scholarship}%")
                print(f"{'*'*100}")

            case 'e':
                payment_history=paymentInfo(payment_history)
                savePaymentFileData(payment_history,paymentFile)

            case 'f':
                validate_json_data()   

            case '0':
                print(f"{'*'*50} Thanks for using this Management system {'*'*50}")
                break           

            case _:
                print("Invaild Input")
                break
#***********************************************************************************************************************8


#note---------------------


    # #Student objects------
    # student1=Student("Alice Johnson", 20, "S101", "Computer Science", "A", 4, 5, 3.63, "3rd Year (Junior)")
    # student2=Student("Alice Johnson", 20, "S101", "Computer Science", "A", 4, 5, 3.85, "2nd Year (Sophomore)")  
    # student3=Student("Robert Smith", 22, "S102", "Electrical Engineering", "B", 7, 6, 3.60, "4th Year (Senior)")  
    # student4=Student("Emily Davis", 21, "S103", "Business Administration", "C", 6, 5, 3.90, "3rd Year (Junior)")  
    # student5=Student("David Brown", 19, "S104", "Mechanical Engineering", "A", 2, 6, 3.45, "1st Year (Freshman)")  
    # student6=Student("Sophia Wilson", 23, "S105", "Civil Engineering", "B", 8, 4, 3.70, "4th Year (Senior)")  


    # #display_info---------------------
    # print(student1.display_info())
    # print(student2.display_info())
    # print(student3.display_info())
    # print(student4.display_info())
    # print(student5.display_info())
    # print(student6.display_info())

    # #Student_status------------------
    # student6.student_status()

    #Teacher objects-----------------
    # teacher1=Teacher("John Smith", 45, "Male", "Physics", "Science", 75000, "Full-time", 20)
    # teacher2=Teacher("Emily Davis", 38, "Female", "Mathematics", "Mathematics", 68000, "Part-time", 15)

    # #display_info------------------
    # print(teacher1.display_info())
