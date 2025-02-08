import random

running_semesters = ["1st Semester", "2nd Semester", "3rd Semester", "4th Semester", 
                     "5th Semester", "6th Semester", "7th Semester", "8th Semester"]
department_subjects = {
    "Computer Science": [
        "Data Structures", "Algorithms", "Database Systems", "Operating Systems",
        "Computer Networks", "Artificial Intelligence", "Machine Learning",
        "Software Engineering", "Web Development", "Cybersecurity"
    ],
    "Electrical Engineering": [
        "Circuit Analysis", "Control Systems", "Digital Signal Processing",
        "Electromagnetics", "Power Systems", "Electrical Machines",
        "Microprocessors", "Analog Electronics", "Renewable Energy Systems",
        "Communication Systems"
    ],
    "Mechanical Engineering": [
        "Thermodynamics", "Fluid Mechanics", "Heat Transfer",
        "Machine Design", "Dynamics", "Engineering Mechanics",
        "Manufacturing Processes", "Robotics", "Material Science",
        "Control Systems"
    ],
    "Civil Engineering": [
        "Structural Analysis", "Surveying", "Construction Management",
        "Environmental Engineering", "Geotechnical Engineering",
        "Transportation Engineering", "Hydrology", "Water Resource Engineering",
        "Urban Planning", "Concrete Technology"
    ],
    "Business Administration": [
        "Accounting Principles", "Marketing Management", "Human Resources Management",
        "Business Law", "Operations Management", "Strategic Management",
        "Entrepreneurship", "Financial Management", "International Business",
        "Organizational Behavior"
    ],
    "Physics": [
        "Classical Mechanics", "Quantum Mechanics", "Thermodynamics",
        "Electromagnetism", "Nuclear Physics", "Optics",
        "Statistical Mechanics", "Solid State Physics",
        "Relativity", "Particle Physics"
    ],
    "Mathematics": [
        "Calculus", "Linear Algebra", "Abstract Algebra",
        "Probability and Statistics", "Differential Equations",
        "Real Analysis", "Complex Analysis", "Numerical Methods",
        "Topology", "Discrete Mathematics"
    ],
    "Chemistry": [
        "Organic Chemistry", "Inorganic Chemistry", "Physical Chemistry",
        "Analytical Chemistry", "Biochemistry", "Environmental Chemistry",
        "Polymer Chemistry", "Industrial Chemistry", "Medicinal Chemistry",
        "Nanochemistry"
    ],
    "Biology": [
        "Cell Biology", "Molecular Biology", "Genetics",
        "Evolutionary Biology", "Ecology", "Microbiology",
        "Immunology", "Botany", "Zoology", "Biotechnology"
    ],
    "Economics": [
        "Microeconomics", "Macroeconomics", "Econometrics",
        "International Trade", "Development Economics",
        "Labor Economics", "Public Economics", "Behavioral Economics",
        "Financial Economics", "Economic Policy"
    ],
    "Psychology": [
        "Cognitive Psychology", "Social Psychology", "Abnormal Psychology",
        "Developmental Psychology", "Personality Psychology",
        "Clinical Psychology", "Biological Psychology",
        "Industrial-Organizational Psychology", "Neuropsychology",
        "Health Psychology"
    ],
    "Sociology": [
        "Introduction to Sociology", "Social Theory", "Research Methods",
        "Cultural Sociology", "Gender and Society", "Urban Sociology",
        "Sociology of Education", "Political Sociology", "Criminology",
        "Globalization and Society"
    ],
    "Political Science": [
        "Comparative Politics", "International Relations", "Political Theory",
        "Public Administration", "Policy Analysis", "Political Economy",
        "Constitutional Law", "Political Behavior", "Human Rights",
        "Geopolitics"
    ],
    "Architecture": [
        "Architectural Design", "Building Materials", "Structural Systems",
        "History of Architecture", "Sustainable Design", "Urban Design",
        "Landscape Architecture", "Building Services", "Computer-Aided Design",
        "Construction Management"
    ],
    "Environmental Science": [
        "Environmental Chemistry", "Environmental Biology", "Ecology",
        "Pollution Control", "Environmental Law", "Sustainable Development",
        "Climate Change", "Renewable Energy", "Conservation Biology",
        "Natural Resource Management"
    ]
}
student_status_list = [
    "1st Year (Freshman)", "2nd Year (Sophomore)", "3rd Year (Junior)", "4th Year (Senior)",
    ]
cgpa_list = [
    3.75, 3.60, 3.90, 3.85, 3.50, 
    3.80, 3.95, 3.70, 3.65, 3.55, 
    3.88, 3.92, 3.45, 3.78, 3.68, 
    3.89, 3.74, 3.81, 3.67, 3.93
    ]






#***************************************************Main Program ******************************************************************
def updateStudentData(studentData):
    name=input("Enter Your Name: ")
    student_id=input("Enter Your Student ID: ")
    for studentinfo in studentData:
        if(name==studentinfo['name'] and student_id==studentinfo['student_ID']):
            while True:
                print("What do you want to Change ? ")
                print("\t 1.Name 2.Age 3.Email 4.Phone Number"
                    "\n\t 5.Section 6.Running Semester 7.Total Courses 0.Exit()")
                print("**Note-----Department,Student ID Both are Cannot be Updated ")
                option=int(input("Enter Your Option: "))
                match option:
                    case 1:
                        studentinfo['name']=input("Enter Your Updated Name :")
                        studentinfo['email']=studentinfo['name'].replace(" ","").lower()+str(random.randint(546,987))+"@outlook.com" 
                        print("****************************Name Updated Successfully ***************************")
                        optionAgain=input("Do you want to update any other data ? (y/n): ").lower()
                        if(optionAgain=='n'):
                            break
                        else:
                            continue
                    case 2:
                        studentinfo['age']=input("Enter Your Updated Age :")
                        print("****************************Age Updated Successfully ***************************")
                        optionAgain=input("Do you want to update any other data ? (y/n): ").lower()
                        if(optionAgain=='n'):
                            break
                        else:
                            continue
                    case 3:
                        studentinfo['email']=input("Enter Your Updated Email :")
                        print("****************************Email Updated Successfully ***************************")
                        optionAgain=input("Do you want to update any other data ? (y/n): ").lower()
                        if(optionAgain=='n'):
                            break
                        else:
                            continue
                    case 4:
                        studentinfo['section']=input("Enter Your Updated Phone Number :")
                        print("****************************Phone Number Updated Successfully ***************************")
                        optionAgain=input("Do you want to update any other data ? (y/n): ").lower()
                        if(optionAgain=='n'):
                            break
                        else:
                            continue
                    case 5:
                        studentinfo['phone']=input("Enter Your Updated Section (['A', 'B'', 'C', 'D', 'E']) :")
                        print("****************************Section Updated Successfully ***************************")
                        optionAgain=input("Do you want to update any other data ? (y/n): ").lower()
                        if(optionAgain=='n'):
                            break
                        else:
                            continue
                    case 6:
                        semester=int(input("Enter Your Updated Running Semester (1,8):"))
                        studentinfo['running_semester']=running_semesters[semester-1]
                        #status section--------------------------------------
                        if(semester<=2):
                            studentinfo['status']=student_status_list[0]
                        elif(2<semester and semester<=4):
                            studentinfo['status']=student_status_list[1]
                        elif(4<semester and semester<=6):
                            studentinfo['status']=student_status_list[2]
                        elif(6<semester and semester<=8):
                            studentinfo['status']=student_status_list[3]
                        print("****************************Running Semester (Also Student Status) Updated Successfully ***************************")
                        optionAgain=input("Do you want to update any other data ? (y/n): ").lower()
                        if(optionAgain=='n'):
                            break
                        else:
                            continue
                    case 7:
                        courses=int(input("Enter Your Updated Total Courses (2,8):"))
                        studentinfo['total_course']=courses
                        def subjectFunction(depart,totalCourses,depart_Subject):
                            dict={}
                            count=1
                            total_cgpa=0
                            for subjectData in depart_Subject[depart]:
                                if(count<=totalCourses):
                                    dict[subjectData]=random.choice(cgpa_list)
                                    total_cgpa+=dict[subjectData]
                                    count+=1
                            total_cgpa=round(total_cgpa/totalCourses,2)
                            return dict,total_cgpa
                        subjectresult,graderesult=subjectFunction(studentinfo['department'],courses,department_subjects)
                        studentinfo['subjects']=subjectresult
                        studentinfo['grade']=graderesult
                        print("****************************Running Semester (Also Subjects List and Grade) Updated Successfully ***************************")
                        optionAgain=input("Do you want to update any other data ? (y/n): ").lower()
                        if(optionAgain=='n'):
                            break
                        else:
                            continue
                    case 0:
                        break
                    case _:
                        print("Invalid Input")
                        break
        else:
            print("The Name and Student_ ID are wrong")
    return studentData