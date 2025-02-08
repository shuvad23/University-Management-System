from UniversityManagementProject import Student,Teacher,Admission,Payment
# Get student data (main function)**********************************************************************************************************************************************
def viewStudentData(students):    
    students=[Student(**student) for student in students]
    for student in students:
        print(f"{"-"*50}{student.name}{"-"*50}")
        Student(student.name,student.age,student.email,student.phone,student.student_ID,student.department,student.section,student.running_semester,student.total_course,student.subjects,student.grade,student.status)
        print(student.display_info())
        student.subjects_list()
        student.student_status()
        print("-"*110)
#Get Teacher data ***********************************************************************************
def viewTeacherData(teachers_data):
    for datas in teachers_data:
        for i in datas:
            teachers=datas[i]
            teachers=[Teacher(**teacher) for teacher in teachers]
            print(f"{"-"*50}{i}{"-"*50}")
            for teacher in teachers:
                Teacher(teacher.name,teacher.age,teacher.gender,teacher.subject,teacher.department,teacher.expertise,teacher.salary,teacher.employment,teacher.experience)
                print(teacher.display_info())
            print("-"*110)

def viewSingleTeacherData(teachers_data,name):
    for datas in teachers_data:
        for i in datas:
            if(name==i):
                teachers=datas[i]
                teachers=[Teacher(**teacher) for teacher in teachers]
                print(f"{"-"*50}{i}{"-"*50}")
                for teacher in teachers:
                    Teacher(teacher.name,teacher.age,teacher.gender,teacher.subject,teacher.department,teacher.expertise,teacher.salary,teacher.employment,teacher.experience)
                    print(teacher.display_info())
                print("-"*110)
                break
        break
#admission data *****************************************************************************************************************************************************************************
def GetSemesterData(admissionData):
    print(f"{'*'*80} Tuition and Fees {'*'*80}")
    print("\tDepartment \t\t\tProgram Type \tAdmission Fee \tTuition Fee(per year) \tTuition Fee(per Credit) \tSemester Fee \tAdditional Fee \tScholarship")
    admissionData=[Admission(**info) for info in admissionData]
    for info in admissionData:
        Admission(info.department,info.program_type,info.admission_fees,info.tuition_fees_per_year,info.tuition_fees_per_credit,info.semester_fees,info.additional_fees,info.scholarship_percentage)
        info.semester_tuition_fees()
    print("*"*150)

#payment data*************************************************************************************************************************************************
def GetPaymentData(paymentData):
    print(f"{'*'*80} Payment History {'*'*80}")
    print("\tDepartment\t\t  Name\t\tStudent ID\tTotal Course\tGrade\tTuition Fee(Per Credit)\tTotal Fee\tPayment \tPayment Due\tPayment Date")
    paymentData=[Payment(**info) for info in paymentData]
    for info in paymentData:
        Payment(info.department,info.name,info.student_ID,info.total_course,info.grade,info.tuition_fees_per_credit,info.total_fees,info.payment,info.payment_due,info.payment_date)
        info.display_info()
    print("*"*180)
