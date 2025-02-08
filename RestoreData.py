import json
def restoreData(studentData,filename,admissionData,admissionfile):
    with open(filename,'r') as fData:
        studentData=json.load(fData)
    with open(admissionfile,'r') as fadmissiondata:
        admissionData=json.load(fadmissiondata)
    return studentData,admissionData
#restore payment data***********************************************************************************************8
def restorePaymentData(paymentData,paymentfile):
    with open(paymentfile,'r') as fpayment:
        paymentData=json.load(fpayment)
    return paymentData