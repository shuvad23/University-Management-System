import json
def removeData(studentData,paymentData,studentfile,paymentfile):
    name=input("Enter Your Name: ")
    student_id=input("Enter Your Student ID: ")
    for studentinfo in studentData:
        if(name==studentinfo['name'] and student_id==studentinfo['student_ID']):
            studentData.remove(studentinfo)

            #******************************************************************************************************************
            for paymentinfo in paymentData:
                if(name==paymentinfo['name'] and student_id==paymentinfo['student_ID']):
                    paymentData.remove(paymentinfo)
                    payment=[]
                    with open(paymentfile,'r') as fpayment:
                        payment=json.load(fpayment)
                        for info in payment:
                            if(info==paymentinfo):
                                del info
                    with open(paymentfile,'w') as fpayment:
                        json.dump(payment,fpayment,indent=4)
                    break

            #************************************************************************************************
            student=[]
            with open(studentfile,'r') as fstudent:
                student=json.load(fstudent)
                for info in student:
                    if(info==studentinfo):
                        del info
            with open(studentfile,'w') as fstudent:
                json.dump(student,fstudent,indent=4)
                
    return studentData,paymentData