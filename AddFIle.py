import json
#save student file data************************************************************
def fileData(studentData,filename):
    with open(filename,'w') as fname:
        json.dump(studentData,fname,indent=4)
#save admission file data************************************************************************************************************
def saveAdmissionInfo_FileData(admission_filedata,admission_filename):
    with open(admission_filename,'w') as fadmission:
        json.dump(admission_filedata,fadmission,indent=4)

#save payment file data************************************************************************************************************

def savePaymentFileData(payment_filedata,payment_filename):
    with open(payment_filename,'w') as fpayment:
        json.dump(payment_filedata,fpayment,indent=4)

#save teacher file data***************************************************************
def saveTeacherFileData(teacher_filedata,teacher_filename):
    with open(teacher_filename,'w') as f:
        json.dump(teacher_filedata,f,indent=4)
    