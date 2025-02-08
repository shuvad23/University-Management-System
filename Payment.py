from datetime import datetime
def paymentInfo(payList):
    name=input("Enter Your Name: ")
    student_id=input("Enter Your Student ID: ")
    count=0
    for pay in payList:
        if(name==pay['name'] and student_id==pay['student_ID']):    
            if(pay['payment_due']!=0):
                print(f"hello {pay['name']} you have a payment pending of TK.{pay['payment_due']}")
                total_fee=pay['total_fees']
                pay_due=pay['payment_due']
                while True:
                    pay_value=int(input("Plz enter your payment value: "))
                    if(pay_value<=pay_due):
                        pay['payment']=pay['payment']+pay_value
                        pay['payment_due']=pay['payment_due']-pay_value
                        print(f"****************Thanks {pay['name']} for your payment ************************")
                        print(f"You paid today : TK.{pay_value}"
                            f"\nYou have already paid : Tk.{pay['payment']}"
                            f"\nYou have a payment pending : TK.{pay['payment_due']}")
                        print(f"{'*'*100}")
                        count=0
                        break
                    else:
                        print(f"plz enter a value less than or equal to TK.{pay_due}")
                        continue
                pay['payment_date']=datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
                break
            else:
                count=0
                print("Your Don't have any Due payment***********")
                print("You paid today : TK.0"
                    f"\nYou have already paid : Tk.{pay['payment']}"
                    f"\nYou have a payment pending : TK.{pay['payment_due']}")
                break
        else:
            count+=1
    if(count>=1):
        print("Your name and Student ID do not match our database/ plz try again**********************")
    return payList