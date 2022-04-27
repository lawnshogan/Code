import pandas as pd
import os

missing_grades_load = os.path.join("Resources", "missing_grades.csv")
missing_grade_df = pd.read_csv(missing_grades_load)
missing_grade_df

# Fill in the empty rows (NaN) with "85".
missing_grade_df.fillna(85)

# Drop the NaNs.
missing_grade_df.dropna()

# Get list of student names with using tolist method to add names to list
student_data_to_load = os.path.join("Resources", "students_complete.csv")
student_data_df = pd.read_csv(student_data_to_load)
student_data_df.head()

student_names = student_data_df["student_name"].tolist()
student_names

# Split method
name = "Mrs. Linda Santiago"
print(name)
name.split()
len(name.split())

# Split student name and determine length of name - If length = 3 we need to inspect it for (Mrs, Dr, Mr, etc)
for name in student_names:
    print(name.split(), len(name.split()))

students_to_fix = []
for name in student_names:
    if len(name.split()) >= 3:
        students_to_fix.append(name)
len(students_to_fix)

# extract suffixes (less than or equal to 3) to new list
# extract prefixes (Less than or equal to 4) to new list
suffixes = []
for name in students_to_fix:
    if len(name.split()[-1]) <= 3:
        suffixes.append(name.split()[-1])
print(suffixes)

prefixes = []
for name in students_to_fix:
    if len(name.split()[0]) <= 4:
        prefixes.append(name.split()[0])

print(prefixes)

# Get unique items in each list
set(prefixes)

set(suffixes)

# Strip "M" "r" or "s" or "." from the student names
for name in students_to_fix:
    print(name.strip("Mrs."))

# Replace "Dr." with an empty string.
name = "Dr. Linda Santiago"
name.replace("Dr. ", "")

# Add each prefix and suffix to remove to a list.
prefixes_suffixes = ["Dr. ", "Mr. ","Ms. ", "Mrs. ", "Miss ", " MD", " DDS", " DVM", " PhD"]
# Convert to string for replace
for word in prefixes_suffixes:
    student_data_df["student_name"] = student_data_df["student_name"].str.replace(word,"")
student_data_df.head(10)

# add names to list, iterate through student_names for length greater than or equal to 3
student_names = student_data_df["student_name"].tolist()
students_fixed = []

for name in student_names:
    if len(name.split()) >= 3:
        students_fixed.append(name)
        
len(students_fixed)