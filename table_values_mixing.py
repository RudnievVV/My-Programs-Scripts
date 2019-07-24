#! python3
# table_values_mixing.py - is being used to encode, for example, sorted students list into unsorted list that First Letter of Student Name
# cannot be the same as previous and next First Letter of Student accordint to the current Student. Also it gives Student the number which
# cannot be greater or less for '1' to current number.
# It expects the 'A1' cell header in input Excel file for students list.
# File will be saved with unique date time to the current working directory.
# Excel file example, link = https://github.com/RudnievVV/My-Programs-Scripts/blob/master/table_values_mixing_example.xlsx
# Work example:
'''
INPUT:             ---     OUTPUT:
Adele Catoe        ---     Samuel In         ---7
Ahmed Hebb         ---     Nam Burtenshaw    ---2
Anthony Gardin     ---     Tequila Fairfield ---16
Antione Collier    ---     Ahmed Hebb        ---5
Avelina Jaquith    ---     Cathy Ollis       ---11
Cathrine Ohagan    ---     Donnell Leu       ---14
Cathy Ollis        ---     Anthony Gardin    ---19
Donnell Leu        ---     Sammie Bosket     ---10
Drema Buckelew     ---     Cathrine Ohagan   ---17
Eldon Stough       ---     Wilbur Locklin    ---4
Francina Beckman   ---     Drema Buckelew    ---1
Huey Wendling      ---     Maximo Barefoot   ---12
Lillian Wine       ---     Lillian Wine      ---6
Maximo Barefoot    ---     Adele Catoe       ---9
Nam Burtenshaw     ---     Eldon Stough      ---13
Ok Mowers          ---     Huey Wendling     ---8
Sammie Bosket      ---     Antione Collier   ---15
Samuel In          ---     Francina Beckman  ---20
Tequila Fairfield  ---     Avelina Jaquith   ---3
Wilbur Locklin     ---     Ok Mowers         ---18
'''

import datetime, random, openpyxl, os, tkinter, pymsgbox, sys
from tkinter import filedialog


# Predefined lists for Excel values
list_of_students = []
nums = []


# Ask user to select the Excel file
answer = pymsgbox.confirm('Click OK to browse the file, click Cancel to cancel.')
if answer == pymsgbox.OK_TEXT:
    root = tkinter.Tk()
    root.withdraw() #use to hide tkinter window
    currdir = os.getcwd()
    tempfile = filedialog.askopenfilename(parent=root, initialdir=currdir, title='Please select a file.', filetypes=(("Excel files", "*.xlsx"), ("All files", "*")))
else:
    pymsgbox.alert('Program is closed')
    sys.exit()


# Loop if answer is file is not valid
not_valid_answer = 0
while True:
    if os.path.isfile(tempfile) == True and \
       (
        tempfile.endswith('.xlsx') or
        tempfile.endswith('.xlsm') or
        tempfile.endswith('.xltx') or
        tempfile.endswith('.xltm')
    ):
        break
    else:
        not_valid_answer = not_valid_answer + 1
        if not_valid_answer <= 1:
            pymsgbox.alert(text='Please choose valid Excel file!', icon=pymsgbox.STOP)
            tempfile = filedialog.askopenfilename(parent=root, initialdir=currdir, title='Please select a file.', filetypes=(("Excel files", "*.xlsx"), ("All files", "*")))
        else:
            not_valid_answer_choice = pymsgbox.confirm(text='Please choose valid Excel file!\nOr hit Cancel to close the program.', icon=pymsgbox.STOP)
            if not_valid_answer_choice == pymsgbox.OK_TEXT:
                tempfile = filedialog.askopenfilename(parent=root, initialdir=currdir, title='Please select a file.', filetypes=(("Excel files", "*.xlsx"), ("All files", "*")))
            else:
                pymsgbox.alert('Program is closed')
                sys.exit()
                

# Open Excel file
excel_list_of_students = openpyxl.load_workbook(tempfile)
sheet = excel_list_of_students.active


# Fulfilling predefined lists
for excel_student in range(2, sheet.max_row + 1):
    list_of_students.append(sheet['A' + str(excel_student)].value)
for num in range(1, len(list_of_students) + 1):
    nums.append(num)


# Checks students
try_count = 1
random.shuffle(list_of_students)
while True:
    # Checks first and last students
    if list_of_students[0][0] == list_of_students[1][0] or \
       list_of_students[len(list_of_students) - 1][0] == list_of_students[len(list_of_students) - 2][0]:
           try_count = try_count + 1
           random.shuffle(list_of_students)
           continue
        
    checked_students = 2
    # Checks the other students
    for student in range(1, len(list_of_students) - 1):
        if list_of_students[student][0] == list_of_students[student + 1][0] or \
           list_of_students[student][0] == list_of_students[student - 1][0]:
            try_count = try_count + 1
            random.shuffle(list_of_students)
            break
        else:
            checked_students = checked_students + 1
            continue
    
    if checked_students == len(list_of_students):
        break
    else:
        continue
        

# Checks numbers
try_count_nums = 1
random.shuffle(nums)
while True:
    # Checks first and last numbers
    if nums[0] == nums[1] + 1 or \
       nums[len(nums) - 1] == nums[len(nums) - 2] - 1:
        try_count_nums = try_count_nums + 1
        random.shuffle(nums)
        continue
    
    checked_nums = 2
    # Checks the other numbers
    for student_num in range(1, len(nums) - 1):
        if nums[student_num] + 1 == nums[student_num + 1] or \
           nums[student_num] - 1 == nums[student_num + 1]:
            try_count_nums = try_count_nums + 1
            random.shuffle(nums)
            break
        else:
            checked_nums = checked_nums + 1
            continue
        
    if checked_nums == len(nums):
        break
    else:
        continue


#print(f'Surname tries {try_count}\nNum tries {try_count_nums}')                # for test
#for checked_value in range(len(list_of_students)):                             # for test
#    print(list_of_students[checked_value] + '---' + str(nums[checked_value]))  # for test


# Open new Excel file to save the progress
wb = openpyxl.Workbook()
wb_sheet = wb.active
wb_sheet.title = 'Encoded'
wb_sheet['A1'] = 'Students'
wb_sheet['B1'] = 'Numbers'
for checked_value in range(len(list_of_students)):
    wb_sheet['A' + str(checked_value + 2)] = list_of_students[checked_value]
    wb_sheet['B' + str(checked_value + 2)] = nums[checked_value]
current_time = datetime.datetime.now()
wb.save('Encoded_list_of_students-' + str(current_time.year) + str(r'-') + str(current_time.month) + str(r'-') + str(current_time.day) + str(r'__') + \
                        str(current_time.hour) + str(r'-') + str(current_time.minute) + str(r'-') + str(current_time.second) + '.xlsx')


# User notification about successfully completed work
pymsgbox.alert(f'Finished successfully.\nResult has been saved to {currdir} folder.')
sys.exit()
