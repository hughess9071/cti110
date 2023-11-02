# CTI-110
# P3HW2 - Salary
# Stephen Hughes
# 11/02/2023

# Pseudocode :

''' 
name = Entered is the Employee name
hours = How many hours they work
payrate = How much is paid per hour

set overtime pay = 0.0
set over_time = 0.0

if hours greater than 40 a wk
do the evalution of the overtime pay and regular pay
	over_time = hours_worked - 40 a wk
	ot_payRate = pay_rate + (pay_rate * 0.5)
	overTime_pay = over_time * ot_payRate
	reg_pay = 40 a wk * pay_rate

else
do the evalution of the regular pay
reg_pay = hours_worked * pay_rate


And then calculate the gross pay = regular pay + overtime pay

print is the results
'''
print("--------- Input Info ------------")
# To read data from user
name = input("Enter employee's name: ")
hours_worked= float(input("Enter number of hours worked: "))
pay_rate= float(input("Enter employee's pay rate: "))

# To evaluate total pay(overtime and regular pay)
overTime_pay = 0.0
over_time = 0.0
if hours_worked > 40:
	over_time = hours_worked - 40
	ot_payRate = pay_rate + (pay_rate * 0.5)
	overTime_pay = over_time * ot_payRate
	reg_pay = 40 * pay_rate
else:
	reg_pay = hours_worked * pay_rate

# To calculate gross pay
gross_pay = reg_pay + overTime_pay

# To print 
print()
print("---------------------")
print("Employee name: ",name)
print("---------------------")
print('Pay period week of 11/03/2023')
print("---------------------")
print("Hours Worked \t Pay Rate \t OverTime \t OverTimePay \t RegHour Pay \t Gross Pay")
print("-------------------------------------------------------------------------------------------")
print(hours_worked," \t\t ",pay_rate," \t ",over_time," \t\t ","$",overTime_pay," \t  ","$",reg_pay," \t ","$",gross_pay)
print()