from datetime import datetime
def paymentHistoryAll(studentData,admissionData,payhistory):
    if(payhistory==[]):
        for data in studentData:
            tuition_credit=0
            additional_fee=0
            scholarship=0
            department=""
            for info in range(len(admissionData)):
                if(data['department'] in admissionData[info]['department']):
                    tuition_credit=admissionData[info]['tuition_fees_per_credit']
                    additional_fee=admissionData[info]['additional_fees']
                    scholarship=admissionData[info]['scholarship_percentage']
                    department=admissionData[info]['department']
            courses=data['total_course']
            cgpa=data['grade']
            total_fees=((3*courses)*tuition_credit)+additional_fee
            if(cgpa>=3.50):
                total_fees=int(total_fees-(total_fees*(scholarship/100)))
            else:
                scholarship=0
            dict={
                "name":data['name'],
                "student_ID":data['student_ID'],
                "total_course":data['total_course'],
                "department":department,
                "grade":round(data['grade'],2),
                "tuition_fees_per_credit":tuition_credit,
                "total_fees":total_fees,
                "payment":0,
                "payment_due":total_fees,
                "payment_date":datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
            }
            payhistory.append(dict)
        return payhistory
    else:
        for data in studentData[len(payhistory)::]:
            tuition_credit=0
            additional_fee=0
            scholarship=0
            department=""
            for info in range(len(admissionData)):
                if(data['department'] in admissionData[info]['department']):
                    tuition_credit=admissionData[info]['tuition_fees_per_credit']
                    additional_fee=admissionData[info]['additional_fees']
                    scholarship=admissionData[info]['scholarship_percentage']
                    department=admissionData[info]['department']
            courses=data['total_course']
            cgpa=data['grade']
            total_fees=((3*courses)*tuition_credit)+additional_fee
            if(cgpa>=3.50):
                total_fees=int(total_fees-(total_fees*(scholarship/100)))
            else:
                scholarship=0
            dict={
                "name":data['name'],
                "student_ID":data['student_ID'],
                "total_course":data['total_course'],
                "department":department,
                "grade":round(data['grade'],2),
                "tuition_fees_per_credit":tuition_credit,
                "total_fees":total_fees,
                "payment":0,
                "payment_due":total_fees,
                "payment_date":datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
            }
            payhistory.append(dict)
        return payhistory
    