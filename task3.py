Employee_name = input("Enter employee name : ")
hour_worked = int(input("Enter the hour worked : "))
pay_rate = float(input("Enter pay rate : "))
if hour_worked <=  40 : 
    gross_pay = hour_worked * pay_rate
    print(f"The gross pay is : {gross_pay:.2f}")
    print(f"The employee name  is : {Employee_name}")
else:
    extra_hour = hour_worked - 40
    overtime_pay = extra_hour * 1.56 * pay_rate
    gross_pay = overtime_pay + ( 40 * pay_rate)
    print(f"overtime pay : {overtime_pay}")
    print("The gross pay is : {gross_pay}")
    print(f"The employee name  is : {Employee_name}")