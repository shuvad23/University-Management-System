university_fees = [
    {"admission_fees": 20000, "tuition_fees_per_year": 150000, "tuition_fees_per_credit": 4000, "semester_fees": 10000, "additional_fees": 5000, "scholarship_percentage": 25},
    {"admission_fees": 25000, "tuition_fees_per_year": 180000, "tuition_fees_per_credit": 4500, "semester_fees": 12000, "additional_fees": 7000, "scholarship_percentage": 30},
    {"admission_fees": 22000, "tuition_fees_per_year": 200000, "tuition_fees_per_credit": 5000, "semester_fees": 15000, "additional_fees": 8000, "scholarship_percentage": 20},
    {"admission_fees": 30000, "tuition_fees_per_year": 250000, "tuition_fees_per_credit": 6000, "semester_fees": 20000, "additional_fees": 10000, "scholarship_percentage": 40},
    {"admission_fees": 18000, "tuition_fees_per_year": 120000, "tuition_fees_per_credit": 3500, "semester_fees": 8000, "additional_fees": 4000, "scholarship_percentage": 10},
    {"admission_fees": 28000, "tuition_fees_per_year": 220000, "tuition_fees_per_credit": 5500, "semester_fees": 18000, "additional_fees": 9000, "scholarship_percentage": 35},
    {"admission_fees": 15000, "tuition_fees_per_year": 100000, "tuition_fees_per_credit": 2500, "semester_fees": 6000, "additional_fees": 3000, "scholarship_percentage": 15},
    {"admission_fees": 32000, "tuition_fees_per_year": 270000, "tuition_fees_per_credit": 6500, "semester_fees": 25000, "additional_fees": 12000, "scholarship_percentage": 50},
    {"admission_fees": 20000, "tuition_fees_per_year": 160000, "tuition_fees_per_credit": 4000, "semester_fees": 11000, "additional_fees": 6000, "scholarship_percentage": 20},
    {"admission_fees": 25000, "tuition_fees_per_year": 190000, "tuition_fees_per_credit": 4700, "semester_fees": 14000, "additional_fees": 7500, "scholarship_percentage": 30},
    {"admission_fees": 26000, "tuition_fees_per_year": 210000, "tuition_fees_per_credit": 5200, "semester_fees": 16000, "additional_fees": 8500, "scholarship_percentage": 25},
    {"admission_fees": 30000, "tuition_fees_per_year": 240000, "tuition_fees_per_credit": 6000, "semester_fees": 20000, "additional_fees": 10000, "scholarship_percentage": 40},
    {"admission_fees": 17000, "tuition_fees_per_year": 110000, "tuition_fees_per_credit": 3000, "semester_fees": 7000, "additional_fees": 3500, "scholarship_percentage": 12},
    {"admission_fees": 27000, "tuition_fees_per_year": 230000, "tuition_fees_per_credit": 5800, "semester_fees": 19000, "additional_fees": 9500, "scholarship_percentage": 30},
    {"admission_fees": 19000, "tuition_fees_per_year": 140000, "tuition_fees_per_credit": 3700, "semester_fees": 9000, "additional_fees": 4500, "scholarship_percentage": 18}
]

departments = [
    "Computer Science       ",
    "Electrical Engineering ",
    "Mechanical Engineering ",
    "Civil Engineering      ",
    "Business Administration",
    "Physics                ",
    "Mathematics            ",
    "Chemistry              ",
    "Biology                ",
    "Economics              ",
    "Psychology             ",
    "Sociology              ",
    "Political Science      ",
    "Architecture           ",
    "Environmental Science  "
    ]
import json
def admissionInfo_tuition(semesterData):
    for i in range(len(departments)):
        dict={
            "department":departments[i],
            "program_type":"Undergraduate",
            "admission_fees":university_fees[i]['admission_fees'],
            "tuition_fees_per_year":university_fees[i]['tuition_fees_per_year'],
            "tuition_fees_per_credit":university_fees[i]['tuition_fees_per_credit'],
            "semester_fees":university_fees[i]['semester_fees'],
            "additional_fees":university_fees[i]['additional_fees'],
            "scholarship_percentage":university_fees[i]['scholarship_percentage']
        }
        semesterData.append(dict)
    return semesterData