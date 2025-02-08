import random
def getStudentFunction(studentdata):
    names = [
        "AaravChandhu", "AnikaRajnath", "AdityaShraya", "AyeshaKumarra",
        "BhavnaPatelm", "ChiragJoshiia", "DishaMehtany", "EshanKapooru",
        "FirozNairram", "GaneshVarma", "HimaniSharma", "IshaniPandey",
        "JasminRathor", "KabirYadavvi", "LakshyaDesai", "MitaliKohlan",
        "NishaVermaaa", "OmkarChowlaa", "PoojaSinghal", "RahulDhanera",
        "SnehaPavithr", "TarunMishram", "UrvashiMahol", "VarunPandyan",
        "YaminiGosala", "ZareenSalhni", "AshwinJadavr", "BhumiSundari",
        "ChitraPalany", "DeepakTiwary", "ElinaRoydhan", "FalguniSahoo",
        "GauravJindal", "HarshaBhatam", "InayaGargili", "JayeshPattna",
        "KritiTandonl", "LavanyaPanae", "MohiniSrivae", "NikhilPateln",
        "OjaswiniSha", "ParthReddyan", "RiyaBalrajam", "SwatiTripath",
        "TanviVikrami", "UrjaSinghan", "VinayMittalr", "YashikaPrajm",
        "ZubinMaheshy", "ArjunRatnal"
    ]

    ages = [18, 20, 22, 19, 21, 23, 25, 24, 26, 27]
    phone_numbers = [
    "123-456-7890", "234-567-8901", "345-678-9012", "456-789-0123", "567-890-1234",
    "678-901-2345", "789-012-3456", "890-123-4567", "901-234-5678", "012-345-6789",
    "111-222-3333", "222-333-4444", "333-444-5555", "444-555-6666", "555-666-7777",
    "666-777-8888", "777-888-9999", "888-999-0000", "999-000-1111", "000-111-2222",
    "123-123-1234", "234-234-2345", "345-345-3456", "456-456-4567", "567-567-5678",
    "678-678-6789", "789-789-7890", "890-890-8901", "901-901-9012", "012-012-0123",
    "135-246-3579", "246-357-4680", "357-468-5791", "468-579-6802", "579-680-7913",
    "680-791-8024", "791-802-9135", "802-913-0246", "913-024-1357", "024-135-2468",
    "101-202-3030", "202-303-4040", "303-404-5050", "404-505-6060", "505-606-7070",
    "606-707-8080", "707-808-9090", "808-909-0101", "909-010-1112", "010-111-2223"
    ]

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
    sections = ["A", "B", "C", "D", "E"]
    running_semesters = ["1st Semester", "2nd Semester", "3rd Semester", "4th Semester", 
                     "5th Semester", "6th Semester", "7th Semester", "8th Semester"]
    total_courses=[5, 6, 4, 7, 3, 8, 5, 6]
    cgpa_list = [
    3.75, 3.60, 3.90, 3.85, 3.50, 
    3.80, 3.95, 3.70, 3.65, 3.55, 
    3.88, 3.92, 3.45, 3.78, 3.68, 
    3.89, 3.74, 3.81, 3.67, 3.93
    ]
    student_status_list = [
    "1st Year (Freshman)", "2nd Year (Sophomore)", "3rd Year (Junior)", "4th Year (Senior)",
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

    def generate_studentData():
        departmentvalue=random.choice(departments)
        totalcoursesvalue=random.choice(total_courses)
        name=random.choice(names)
        subResult,cgpaResult=subjectFunction(departmentvalue,totalcoursesvalue,department_subjects)
        return {
            "name":name,
            "age": random.choice(ages),
            "email": name.replace(" ","").lower()+str(random.randint(456,987))+"@outlook.com",
            "phone":random.choice(phone_numbers),
            "student_ID": random.choice(student_ids),
            "department": departmentvalue,
            "section": random.choice(sections),
            "running_semester": random.choice(running_semesters),
            "total_course": totalcoursesvalue,
            "subjects": subResult,
            "grade": round(cgpaResult,2) ,
            "status":random.choice(student_status_list),

        }
    demmy_data=generate_studentData()
    studentdata.append(demmy_data)
    return studentdata