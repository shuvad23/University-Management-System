import random
import json
def getTeacherData(teacherData):
    teacher_information={
    "Computer Science": [
        {"name": "Alice Johnson", "age": 35, "gender": "Female", "subject": "AI", "department": "Computer Science", "expertise": "Machine Learning", "salary": 85000, "employment": "Full-time", "experience": 10},
        {"name": "Bob Smith", "age": 42, "gender": "Male", "subject": "Data Structures", "department": "Computer Science", "expertise": "Algorithms", "salary": 90000, "employment": "Full-time", "experience": 15},
        {"name": "Charlie Brown", "age": 38, "gender": "Male", "subject": "Cybersecurity", "department": "Computer Science", "expertise": "Network Security", "salary": 88000, "employment": "Full-time", "experience": 12},
        {"name": "Diana Prince", "age": 29, "gender": "Female", "subject": "Web Development", "department": "Computer Science", "expertise": "Front-end", "salary": 78000, "employment": "Full-time", "experience": 6},
        {"name": "Ethan Hunt", "age": 45, "gender": "Male", "subject": "Operating Systems", "department": "Computer Science", "expertise": "Kernel Design", "salary": 92000, "employment": "Full-time", "experience": 18},
        {"name": "Fiona Clark", "age": 33, "gender": "Female", "subject": "Database Systems", "department": "Computer Science", "expertise": "SQL", "salary": 81000, "employment": "Full-time", "experience": 9},
        {"name": "George White", "age": 37, "gender": "Male", "subject": "Software Engineering", "department": "Computer Science", "expertise": "Agile Development", "salary": 86000, "employment": "Full-time", "experience": 11},
        {"name": "Hannah Lee", "age": 31, "gender": "Female", "subject": "Cloud Computing", "department": "Computer Science", "expertise": "AWS", "salary": 83000, "employment": "Full-time", "experience": 8},
        {"name": "Ian Black", "age": 40, "gender": "Male", "subject": "Networking", "department": "Computer Science", "expertise": "Cisco", "salary": 89000, "employment": "Full-time", "experience": 13},
        {"name": "Jessica Green", "age": 34, "gender": "Female", "subject": "Programming Languages", "department": "Computer Science", "expertise": "Python", "salary": 82000, "employment": "Full-time", "experience": 10}
    ],
    "Electrical Engineering": [
        {"name": "Kevin Hart", "age": 39, "gender": "Male", "subject": "Circuit Analysis", "department": "Electrical Engineering", "expertise": "Analog Circuits", "salary": 87000, "employment": "Full-time", "experience": 14},
        {"name": "Laura King", "age": 36, "gender": "Female", "subject": "Power Systems", "department": "Electrical Engineering", "expertise": "Renewable Energy", "salary": 86000, "employment": "Full-time", "experience": 12},
        {"name": "Michael Scott", "age": 42, "gender": "Male", "subject": "Control Systems", "department": "Electrical Engineering", "expertise": "Automation", "salary": 91000, "employment": "Full-time", "experience": 16},
        {"name": "Natalie Wright", "age": 30, "gender": "Female", "subject": "Digital Systems", "department": "Electrical Engineering", "expertise": "FPGA", "salary": 80000, "employment": "Full-time", "experience": 7},
        {"name": "Oscar Lopez", "age": 41, "gender": "Male", "subject": "Microelectronics", "department": "Electrical Engineering", "expertise": "Semiconductors", "salary": 90000, "employment": "Full-time", "experience": 15},
        {"name": "Paula Adams", "age": 35, "gender": "Female", "subject": "Signal Processing", "department": "Electrical Engineering", "expertise": "DSP", "salary": 87000, "employment": "Full-time", "experience": 11},
        {"name": "Quentin Blake", "age": 39, "gender": "Male", "subject": "Electromagnetics", "department": "Electrical Engineering", "expertise": "RF Design", "salary": 88000, "employment": "Full-time", "experience": 13},
        {"name": "Rachel Stone", "age": 29, "gender": "Female", "subject": "Embedded Systems", "department": "Electrical Engineering", "expertise": "IoT", "salary": 79000, "employment": "Full-time", "experience": 6},
        {"name": "Samuel Grant", "age": 43, "gender": "Male", "subject": "Wireless Communications", "department": "Electrical Engineering", "expertise": "5G", "salary": 93000, "employment": "Full-time", "experience": 17},
        {"name": "Tina Bell", "age": 37, "gender": "Female", "subject": "Power Electronics", "department": "Electrical Engineering", "expertise": "EV Systems", "salary": 85000, "employment": "Full-time", "experience": 10}
    ],
    "Mechanical Engineering": [
        {"name": "Mark Taylor", "age": 40, "gender": "Male", "subject": "Thermodynamics", "department": "Mechanical Engineering", "expertise": "Heat Transfer", "salary": 88000, "employment": "Full-time", "experience": 14},
        {"name": "Sarah Johnson", "age": 38, "gender": "Female", "subject": "Fluid Mechanics", "department": "Mechanical Engineering", "expertise": "CFD", "salary": 86000, "employment": "Full-time", "experience": 12},
        {"name": "John Carter", "age": 42, "gender": "Male", "subject": "Machine Design", "department": "Mechanical Engineering", "expertise": "Solid Mechanics", "salary": 89000, "employment": "Full-time", "experience": 16},
        {"name": "Emily White", "age": 30, "gender": "Female", "subject": "Manufacturing Processes", "department": "Mechanical Engineering", "expertise": "CNC", "salary": 81000, "employment": "Full-time", "experience": 8},
        {"name": "Robert King", "age": 45, "gender": "Male", "subject": "Automobile Engineering", "department": "Mechanical Engineering", "expertise": "EV Technology", "salary": 92000, "employment": "Full-time", "experience": 18},
        {"name": "Nancy Green", "age": 34, "gender": "Female", "subject": "Robotics", "department": "Mechanical Engineering", "expertise": "Mechatronics", "salary": 85000, "employment": "Full-time", "experience": 10},
        {"name": "Paul Harris", "age": 37, "gender": "Male", "subject": "HVAC Systems", "department": "Mechanical Engineering", "expertise": "Refrigeration", "salary": 87000, "employment": "Full-time", "experience": 11},
        {"name": "Jessica Adams", "age": 31, "gender": "Female", "subject": "Engineering Materials", "department": "Mechanical Engineering", "expertise": "Metallurgy", "salary": 83000, "employment": "Full-time", "experience": 7},
        {"name": "Eric Brown", "age": 39, "gender": "Male", "subject": "Dynamics", "department": "Mechanical Engineering", "expertise": "Kinematics", "salary": 88000, "employment": "Full-time", "experience": 13},
        {"name": "Olivia Scott", "age": 35, "gender": "Female", "subject": "Structural Analysis", "department": "Mechanical Engineering", "expertise": "Finite Element Analysis", "salary": 84000, "employment": "Full-time", "experience": 9}
    ],
    "Civil Engineering": [
    {"name": "Adam Carter", "age": 41, "gender": "Male", "subject": "Structural Analysis", "department": "Civil Engineering", "expertise": "Bridge Design", "salary": 88000, "employment": "Full-time", "experience": 15},
    {"name": "Bethany Adams", "age": 36, "gender": "Female", "subject": "Construction Management", "department": "Civil Engineering", "expertise": "Project Planning", "salary": 86000, "employment": "Full-time", "experience": 12},
    {"name": "Chris Evans", "age": 39, "gender": "Male", "subject": "Geotechnical Engineering", "department": "Civil Engineering", "expertise": "Soil Mechanics", "salary": 87000, "employment": "Full-time", "experience": 14},
    {"name": "Daisy Johnson", "age": 30, "gender": "Female", "subject": "Transportation Engineering", "department": "Civil Engineering", "expertise": "Traffic Flow", "salary": 80000, "employment": "Full-time", "experience": 7},
    {"name": "Edward Norton", "age": 45, "gender": "Male", "subject": "Hydraulic Engineering", "department": "Civil Engineering", "expertise": "Water Resources", "salary": 92000, "employment": "Full-time", "experience": 18},
    {"name": "Felicity Brown", "age": 33, "gender": "Female", "subject": "Environmental Engineering", "department": "Civil Engineering", "expertise": "Sustainability", "salary": 83000, "employment": "Full-time", "experience": 9},
    {"name": "George Martin", "age": 38, "gender": "Male", "subject": "Concrete Technology", "department": "Civil Engineering", "expertise": "Material Science", "salary": 86000, "employment": "Full-time", "experience": 11},
    {"name": "Holly Wright", "age": 29, "gender": "Female", "subject": "Urban Planning", "department": "Civil Engineering", "expertise": "City Development", "salary": 79000, "employment": "Full-time", "experience": 6},
    {"name": "Ian Thomas", "age": 42, "gender": "Male", "subject": "Surveying", "department": "Civil Engineering", "expertise": "Land Mapping", "salary": 90000, "employment": "Full-time", "experience": 16},
    {"name": "Julia Roberts", "age": 34, "gender": "Female", "subject": "Structural Design", "department": "Civil Engineering", "expertise": "Steel Structures", "salary": 82000, "employment": "Full-time", "experience": 10}
    ],
    "Business Administration": [
        {"name": "Alan Johnson", "age": 40, "gender": "Male", "subject": "Finance", "department": "Business Administration", "expertise": "Corporate Finance", "salary": 89000, "employment": "Full-time", "experience": 15},
        {"name": "Barbara Smith", "age": 35, "gender": "Female", "subject": "Marketing", "department": "Business Administration", "expertise": "Digital Marketing", "salary": 86000, "employment": "Full-time", "experience": 12},
        {"name": "Charles Davis", "age": 42, "gender": "Male", "subject": "Operations Management", "department": "Business Administration", "expertise": "Supply Chain", "salary": 91000, "employment": "Full-time", "experience": 16},
        {"name": "Debra Wilson", "age": 31, "gender": "Female", "subject": "Human Resources", "department": "Business Administration", "expertise": "Talent Acquisition", "salary": 80000, "employment": "Full-time", "experience": 8},
        {"name": "Edward Carter", "age": 45, "gender": "Male", "subject": "Entrepreneurship", "department": "Business Administration", "expertise": "Startup Management", "salary": 93000, "employment": "Full-time", "experience": 18},
        {"name": "Fiona Parker", "age": 34, "gender": "Female", "subject": "International Business", "department": "Business Administration", "expertise": "Global Markets", "salary": 82000, "employment": "Full-time", "experience": 10},
        {"name": "George Adams", "age": 39, "gender": "Male", "subject": "Business Ethics", "department": "Business Administration", "expertise": "Corporate Social Responsibility", "salary": 87000, "employment": "Full-time", "experience": 13},
        {"name": "Helen Brown", "age": 28, "gender": "Female", "subject": "Strategic Management", "department": "Business Administration", "expertise": "Business Strategy", "salary": 78000, "employment": "Full-time", "experience": 5},
        {"name": "Ian Roberts", "age": 41, "gender": "Male", "subject": "Organizational Behavior", "department": "Business Administration", "expertise": "Leadership Development", "salary": 88000, "employment": "Full-time", "experience": 14},
        {"name": "Jessica White", "age": 33, "gender": "Female", "subject": "Project Management", "department": "Business Administration", "expertise": "Agile Methodologies", "salary": 81000, "employment": "Full-time", "experience": 9}
    ],
    "Physics": [
        {"name": "Albert Newton", "age": 45, "gender": "Male", "subject": "Quantum Mechanics", "department": "Physics", "expertise": "Quantum Computing", "salary": 92000, "employment": "Full-time", "experience": 18},
        {"name": "Brenda Maxwell", "age": 37, "gender": "Female", "subject": "Thermodynamics", "department": "Physics", "expertise": "Heat Transfer", "salary": 88000, "employment": "Full-time", "experience": 12},
        {"name": "Carl Sagan", "age": 50, "gender": "Male", "subject": "Astrophysics", "department": "Physics", "expertise": "Cosmology", "salary": 94000, "employment": "Full-time", "experience": 20},
        {"name": "Diana Foster", "age": 33, "gender": "Female", "subject": "Electromagnetism", "department": "Physics", "expertise": "Maxwell's Equations", "salary": 84000, "employment": "Full-time", "experience": 10},
        {"name": "Ethan Hawke", "age": 41, "gender": "Male", "subject": "Classical Mechanics", "department": "Physics", "expertise": "Newtonian Physics", "salary": 87000, "employment": "Full-time", "experience": 14},
        {"name": "Felicity Harper", "age": 29, "gender": "Female", "subject": "Particle Physics", "department": "Physics", "expertise": "Collider Experiments", "salary": 80000, "employment": "Full-time", "experience": 6},
        {"name": "George Lucas", "age": 39, "gender": "Male", "subject": "Nuclear Physics", "department": "Physics", "expertise": "Radioactive Decay", "salary": 88000, "employment": "Full-time", "experience": 13},
        {"name": "Hannah Drake", "age": 35, "gender": "Female", "subject": "Optics", "department": "Physics", "expertise": "Laser Physics", "salary": 86000, "employment": "Full-time", "experience": 9},
        {"name": "Ian Wright", "age": 44, "gender": "Male", "subject": "Solid State Physics", "department": "Physics", "expertise": "Crystal Structures", "salary": 90000, "employment": "Full-time", "experience": 16},
        {"name": "Jessica Ray", "age": 30, "gender": "Female", "subject": "Fluid Dynamics", "department": "Physics", "expertise": "Turbulence", "salary": 82000, "employment": "Full-time", "experience": 7}
    ],
    "Mathematics": [
        {"name": "Alan Turing", "age": 45, "gender": "Male", "subject": "Algebra", "department": "Mathematics", "expertise": "Abstract Algebra", "salary": 89000, "employment": "Full-time", "experience": 18},
        {"name": "Beatrice Nash", "age": 38, "gender": "Female", "subject": "Calculus", "department": "Mathematics", "expertise": "Differential Equations", "salary": 85000, "employment": "Full-time", "experience": 12},
        {"name": "Charles Gauss", "age": 50, "gender": "Male", "subject": "Number Theory", "department": "Mathematics", "expertise": "Prime Numbers", "salary": 93000, "employment": "Full-time", "experience": 20},
        {"name": "Diana Euler", "age": 32, "gender": "Female", "subject": "Statistics", "department": "Mathematics", "expertise": "Probability Theory", "salary": 81000, "employment": "Full-time", "experience": 8},
        {"name": "Ethan Klein", "age": 40, "gender": "Male", "subject": "Topology", "department": "Mathematics", "expertise": "Knot Theory", "salary": 87000, "employment": "Full-time", "experience": 14},
        {"name": "Fiona Taylor", "age": 36, "gender": "Female", "subject": "Geometry", "department": "Mathematics", "expertise": "Euclidean Spaces", "salary": 83000, "employment": "Full-time", "experience": 10}
    ],
    "Chemistry": [
        {"name": "Alice Carter", "age": 40, "gender": "Female", "subject": "Organic Chemistry", "department": "Chemistry", "expertise": "Natural Products", "salary": 89000, "employment": "Full-time", "experience": 15},
        {"name": "Brian Adams", "age": 38, "gender": "Male", "subject": "Inorganic Chemistry", "department": "Chemistry", "expertise": "Metal Complexes", "salary": 87000, "employment": "Full-time", "experience": 12},
        {"name": "Catherine Foster", "age": 45, "gender": "Female", "subject": "Analytical Chemistry", "department": "Chemistry", "expertise": "Chromatography", "salary": 91000, "employment": "Full-time", "experience": 18},
        {"name": "David White", "age": 50, "gender": "Male", "subject": "Physical Chemistry", "department": "Chemistry", "expertise": "Quantum Chemistry", "salary": 95000, "employment": "Full-time", "experience": 20},
        {"name": "Emma Johnson", "age": 32, "gender": "Female", "subject": "Biochemistry", "department": "Chemistry", "expertise": "Enzymology", "salary": 83000, "employment": "Full-time", "experience": 8}
    ],
    "Biology": [
        {"name": "Alice Morgan", "age": 42, "gender": "Female", "subject": "Genetics", "department": "Biology", "expertise": "Genomics", "salary": 91000, "employment": "Full-time", "experience": 15},
        {"name": "Ben Smith", "age": 39, "gender": "Male", "subject": "Microbiology", "department": "Biology", "expertise": "Pathogens", "salary": 89000, "employment": "Full-time", "experience": 13},
        {"name": "Catherine Black", "age": 47, "gender": "Female", "subject": "Botany", "department": "Biology", "expertise": "Plant Ecology", "salary": 93000, "employment": "Full-time", "experience": 18},
        {"name": "Daniel Green", "age": 35, "gender": "Male", "subject": "Zoology", "department": "Biology", "expertise": "Animal Behavior", "salary": 85000, "employment": "Full-time", "experience": 10},
        {"name": "Eva Brown", "age": 29, "gender": "Female", "subject": "Ecology", "department": "Biology", "expertise": "Conservation Biology", "salary": 82000, "employment": "Full-time", "experience": 7}
    ],
    "Economics": [
        {"name": "Arthur Keynes", "age": 45, "gender": "Male", "subject": "Macroeconomics", "department": "Economics", "expertise": "Fiscal Policy", "salary": 92000, "employment": "Full-time", "experience": 16},
        {"name": "Barbara Johnson", "age": 38, "gender": "Female", "subject": "Microeconomics", "department": "Economics", "expertise": "Consumer Behavior", "salary": 88000, "employment": "Full-time", "experience": 12},
        {"name": "Charles Friedman", "age": 50, "gender": "Male", "subject": "International Economics", "department": "Economics", "expertise": "Global Trade", "salary": 95000, "employment": "Full-time", "experience": 20},
        {"name": "Diana Scott", "age": 33, "gender": "Female", "subject": "Behavioral Economics", "department": "Economics", "expertise": "Decision Making", "salary": 83000, "employment": "Full-time", "experience": 9},
        {"name": "Edward Nash", "age": 40, "gender": "Male", "subject": "Econometrics", "department": "Economics", "expertise": "Statistical Models", "salary": 89000, "employment": "Full-time", "experience": 14}
    ],
    "Psychology": [
        {"name": "Alice Parker", "age": 39, "gender": "Female", "subject": "Clinical Psychology", "department": "Psychology", "expertise": "Mental Health", "salary": 89000, "employment": "Full-time", "experience": 14},
        {"name": "Brian Taylor", "age": 44, "gender": "Male", "subject": "Cognitive Psychology", "department": "Psychology", "expertise": "Neuroscience", "salary": 91000, "employment": "Full-time", "experience": 17},
        {"name": "Catherine Harris", "age": 36, "gender": "Female", "subject": "Developmental Psychology", "department": "Psychology", "expertise": "Child Development", "salary": 85000, "employment": "Full-time", "experience": 10},
        {"name": "Daniel Cooper", "age": 41, "gender": "Male", "subject": "Social Psychology", "department": "Psychology", "expertise": "Group Behavior", "salary": 88000, "employment": "Full-time", "experience": 13},
        {"name": "Emma Foster", "age": 30, "gender": "Female", "subject": "Behavioral Psychology", "department": "Psychology", "expertise": "Cognitive Therapy", "salary": 82000, "employment": "Full-time", "experience": 7}
    ],
    "Sociology": [
        {"name": "Adam White", "age": 46, "gender": "Male", "subject": "Cultural Sociology", "department": "Sociology", "expertise": "Social Norms", "salary": 92000, "employment": "Full-time", "experience": 18},
        {"name": "Barbara King", "age": 40, "gender": "Female", "subject": "Urban Sociology", "department": "Sociology", "expertise": "City Planning", "salary": 88000, "employment": "Full-time", "experience": 12},
        {"name": "Charlie Evans", "age": 35, "gender": "Male", "subject": "Sociological Theory", "department": "Sociology", "expertise": "Social Structures", "salary": 86000, "employment": "Full-time", "experience": 9},
        {"name": "Diana Lopez", "age": 43, "gender": "Female", "subject": "Gender Studies", "department": "Sociology", "expertise": "Gender Inequality", "salary": 90000, "employment": "Full-time", "experience": 14},
        {"name": "Ethan Clark", "age": 32, "gender": "Male", "subject": "Social Change", "department": "Sociology", "expertise": "Activism", "salary": 83000, "employment": "Full-time", "experience": 8}
    ],
    "Political Science": [
        {"name": "Anthony Brown", "age": 48, "gender": "Male", "subject": "Comparative Politics", "department": "Political Science", "expertise": "Government Systems", "salary": 94000, "employment": "Full-time", "experience": 20},
        {"name": "Brenda Wilson", "age": 37, "gender": "Female", "subject": "International Relations", "department": "Political Science", "expertise": "Diplomacy", "salary": 87000, "employment": "Full-time", "experience": 11},
        {"name": "Carlos Martinez", "age": 41, "gender": "Male", "subject": "Public Policy", "department": "Political Science", "expertise": "Legislation", "salary": 89000, "employment": "Full-time", "experience": 13},
        {"name": "Daisy Anderson", "age": 34, "gender": "Female", "subject": "Political Theory", "department": "Political Science", "expertise": "Political Philosophy", "salary": 85000, "employment": "Full-time", "experience": 9},
        {"name": "Edward Johnson", "age": 39, "gender": "Male", "subject": "Public Administration", "department": "Political Science", "expertise": "Governance", "salary": 88000, "employment": "Full-time", "experience": 12}
    ],
    "Architecture": [
        {"name": "Alice Davidson", "age": 42, "gender": "Female", "subject": "Urban Design", "department": "Architecture", "expertise": "City Planning", "salary": 91000, "employment": "Full-time", "experience": 15},
        {"name": "Brian Thompson", "age": 38, "gender": "Male", "subject": "Sustainable Architecture", "department": "Architecture", "expertise": "Green Building", "salary": 88000, "employment": "Full-time", "experience": 12},
        {"name": "Catherine Miller", "age": 35, "gender": "Female", "subject": "Interior Design", "department": "Architecture", "expertise": "Space Planning", "salary": 85000, "employment": "Full-time", "experience": 10},
        {"name": "David Johnson", "age": 45, "gender": "Male", "subject": "Structural Design", "department": "Architecture", "expertise": "Building Materials", "salary": 92000, "employment": "Full-time", "experience": 17},
        {"name": "Emily Carter", "age": 30, "gender": "Female", "subject": "Landscape Architecture", "department": "Architecture", "expertise": "Outdoor Spaces", "salary": 81000, "employment": "Full-time", "experience": 7}
    ],
    "Environmental Science": [
        {"name": "Alan Green", "age": 44, "gender": "Male", "subject": "Ecology", "department": "Environmental Science", "expertise": "Ecosystem Management", "salary": 89000, "employment": "Full-time", "experience": 16},
        {"name": "Bethany Roberts", "age": 37, "gender": "Female", "subject": "Climate Change", "department": "Environmental Science", "expertise": "Global Warming", "salary": 87000, "employment": "Full-time", "experience": 12},
        {"name": "Charles Wilson", "age": 40, "gender": "Male", "subject": "Environmental Policy", "department": "Environmental Science", "expertise": "Regulations", "salary": 86000, "employment": "Full-time", "experience": 14},
        {"name": "Diana Morgan", "age": 32, "gender": "Female", "subject": "Renewable Energy", "department": "Environmental Science", "expertise": "Solar and Wind", "salary": 82000, "employment": "Full-time", "experience": 8},
        {"name": "Ethan Scott", "age": 39, "gender": "Male", "subject": "Sustainability", "department": "Environmental Science", "expertise": "Sustainable Development", "salary": 88000, "employment": "Full-time", "experience": 13}
    ]
    }
    
    teacherData.append(teacher_information)
    return teacherData