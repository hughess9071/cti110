# CTI-110
# P2HW2 - List
# Stphen Hughes
# 10/24/2023
#

# All modules
Mod_1 = float(input('Enter grade for Module 1: ')) 
Mod_2 = float(input('Enter grade for Module 2: ')) 
Mod_3 = float(input('Enter grade for Module 3: ')) 
Mod_4 = float(input('Enter grade for Module 4: ')) 
Mod_5 = float(input('Enter grade for Module 5: ')) 
Mod_6 = float(input('Enter grade for Module 6: ')) 
# Sum of all modules
Module_Numbers = [Mod_1, Mod_2, Mod_3, Mod_4, Mod_5, Mod_6]
# This get the number of modules in Module_Grades
sum_lst = sum(Module_Numbers)
# This sets the average by taking the sum and divide by the number of modules
lst_avg = sum_lst/len(Module_Numbers)
# Results
print()
print('---------------Results-----------------')
print(f'Lowest Grade:        {min(Module_Numbers)}')
print(f'Highest Grade:       {max(Module_Numbers)}')
print(f'Sum of Grades:       {sum(Module_Numbers)}')
print('Average:            ',round(lst_avg,2))
print('----------------------------------------')
print()
