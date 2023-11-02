# CTI-110
# P3HW1 - Debugging
# Stphen Hughes
# 11/02/2023
#
# All modules
mod_1 = float(input("Enter grade for Module 1: "))
mod_2 = float(input("Enter grade for Module 2: "))
mod_3 = float(input("Enter grade for Module 3: "))
mod_4 = float(input("Enter grade for Module 4: "))
mod_5 = float(input("Enter grade for Module 5: "))
mod_6 = float(input("Enter grade for Module 6: "))

# Sum of all modules
Module_Numbers = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# This get the number of modules in Module_Grades
sum_lst = sum(Module_Numbers)
# This sets the average by taking the sum and divide by the number of modules
lst_avg = sum_lst/len(Module_Numbers)

# Results 
print()
print("-----------Results------------")
print(f'Lowest Grade:        {min(Module_Numbers)}')
print(f'Highest Grade:       {max(Module_Numbers)}')
print(f'Sum of Grades:       {sum(Module_Numbers)}')
print('Average:            ',round(lst_avg,2))
print("---------------------------------")

# finding perfect grade based on average
if lst_avg >= 90:
    print("Your grade is: A")
# elif is used not else if 
elif lst_avg > 80:
    print("Your grade is: B")
elif lst_avg > 70:
    print("Your grade is: C")
elif lst_avg > 60:
    print("Your grade is: D")
else:
    print("Your grade is: F")