#====================================Data section==============================================
student_ids = [
    "S101", "S102", "S103", "S104", "S105", 
    "S106", "S107", "S108", "S109", "S110",
    "S111", "S112", "S113", "S114", "S115",
    "S116", "S117", "S118", "S119", "S120",
    "S121", "S122", "S123", "S124", "S125",
    "S126", "S127", "S128", "S129", "S130",
    "S131", "S132", "S133", "S134", "S135",
    "S136", "S137", "S138", "S139", "S140",
    "S141", "S142", "S143", "S144", "S145",
    "S146", "S147", "S148", "S149", "S150"
    ]
running_semesters = ["1st Semester", "2nd Semester", "3rd Semester", "4th Semester", 
                     "5th Semester", "6th Semester", "7th Semester", "8th Semester"]
cgpa_list = [
    3.75, 3.60, 3.90, 3.85, 3.50, 
    3.80, 3.95, 3.70, 3.65, 3.55, 
    3.88, 3.92, 3.45, 3.78, 3.68, 
    3.89, 3.74, 3.81, 3.67, 3.93
    ]
student_status_list = [
    "1st Year (Freshman)", "2nd Year (Sophomore)", "3rd Year (Junior)", "4th Year (Senior)",
    ]
departments = [
    "Computer Science",
    "Electrical Engineering",
    "Mechanical Engineering",
    "Civil Engineering",
    "Business Administration",
    "Physics",
    "Mathematics",
    "Chemistry",
    "Biology",
    "Economics",
    "Psychology",
    "Sociology",
    "Political Science",
    "Architecture",
    "Environmental Science"
    ]
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

#===============================================================================================================================

import random
def addManualData(all_studentsData):
    name=None
    age=None
    email=None
    phone=None
    student_ID=None
    department=None
    section=None
    running_semester=None
    total_course=None
    subjects=None
    grade=None
    status=None
    semester=None
    #Name,email,phone,department,section,running_semester,status------------------------------
    while True:
        try:
            name=input("=>Enter Your Name: ")
            email=input("Enter Your Email: ")
            phone=input("=>Enter Your Phone Number: ")
            print(f"Choice Your Department: {departments}")
            department=input("Enter Your Department Name: ")
            section=input("Enter Your Section (['A', 'B'', 'C', 'D', 'E']): ")
            break
        except ValueError:
            print("Name,Email,Phone,Department and Section must be String.Plz enter the correct datatype....")      
    #age,student_ID,total_courses,running semester------------------------------------------------------
    while True:
        try :
            age=int(input("=>Enter Your Age: "))
            student_ID=random.choice(student_ids)
            total_course=int(input("Enter Number of Courses You Want (2,8): "))
            semester=int(input("Enter Your Running Semester (1,8): "))
            running_semester=running_semesters[semester-1]
            break
        except ValueError:
            print("age,student ID,total course and running semester must be an integer.Plz enter the correct datatype....")
    
    #status section--------------------------------------
    if(semester<=2):
        status=student_status_list[0]
    elif(2<semester and semester<=4):
        status=student_status_list[1]
    elif(4<semester and semester<=6):
        status=student_status_list[2]
    elif(6<semester and semester<=8):
        status=student_status_list[3]


    #subject and grade=================================================================
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

    subjectresult,graderesult=subjectFunction(department,total_course,department_subjects)

    #dictonary=============================================================================
    dicData={
            "name":name,
            "age": age,
            "email":email,
            "phone":phone,
            "student_ID": student_ID,
            "department": department,
            "section": section,
            "running_semester":running_semester,
            "total_course": total_course,
            "subjects": subjectresult,
            "grade": graderesult,
            "status":status,
    }
    
    all_studentsData.append(dicData)
    return all_studentsData
    
    #save in a file-----------------------------------------------------------------------
