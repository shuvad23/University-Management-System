import pandas as pd

def export_to_csv():
    student_data=pd.read_json('data/Student_info.json')
    student_data.to_csv('output/student_info.csv',index=False)
    admission_data=pd.read_json('data/admission_info.json')
    admission_data.to_csv('output/admission_info.csv',index=False)
    payment_data=pd.read_json('data/payment_info.json')
    payment_data.to_csv('output/payment_info.csv',index=False)
    print("Data exported to csv successfully.")
def export_to_excel():
    student_data=pd.read_json('data/Student_info.json')
    student_data.to_excel('output/student_info.xlsx',index=False)
    admission_data=pd.read_json('data/admission_info.json')
    admission_data.to_excel('output/admission_info.xlsx',index=False)
    payment_data=pd.read_json('data/payment_info.json')
    payment_data.to_excel('output/payment_info.xlsx',index=False)
    print("Data exported to excel successfully.")