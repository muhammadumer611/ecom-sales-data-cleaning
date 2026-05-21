# import pandas as pd
# import numpy as np

# # 1. Pehle data banana aur pivot karna (Jo hum ne pehle kiya tha)
# session_CS_B_students = {
#     'StudentID': [70169453, 70169454, 70169455, 70169456, 70169457,
#                   70169458, 70169459, 70169460, 70169461, 70169462],
#     'StudentName': ['Alice', 'Bob', 'Charlie', 'David', 'Eve',
#                     'Frank', 'Grace', 'Heidi', 'Ivan', 'Judy'],
#     'Subject': [['IS','Web Engineering','Data Science','AI','Cybersecurity','Data Mining'] for _ in range(10)],
#     "Marks_of_subjects": [
#        [85, 90, 78, 92, 88, 80], [80, 85, 82, 88, 90, 86],
#        [78, 82, 80, 85, 87, 83], [92, 88, 85, 90, 91, 89],
#        [88, 90, 87, 91, 92, 90], [80, 86, 83, 89, 90, 88],
#        [85, 88, 84, 90, 91, 87], [90, 92, 89, 93, 94, 91],
#        [78, 82, 80, 85, 87, 83], [92, 88, 85, 90, 91, 89]
#     ]
# }

# students_df = pd.DataFrame(session_CS_B_students)
# exploded_df = students_df.explode(['Subject', 'Marks_of_subjects'])

# # Data types ko numbers mein convert karna zaroori hai
# exploded_df['Marks_of_subjects'] = exploded_df['Marks_of_subjects'].astype(int)

# # Pivot karke wide format table banana
# prof_df = exploded_df.pivot(index=['StudentID', 'StudentName'], columns='Subject', values='Marks_of_subjects').reset_index()

# # 2. Total Marks aur Percentage ki calculation
# subjects_list = ['AI', 'Cybersecurity', 'Data Mining', 'Data Science', 'IS', 'Web Engineering']
# total_subjects = len(subjects_list)
# max_marks_per_subject = 100

# # Row-wise sum nikalna (.sum(axis=1))
# prof_df['Total_Obtained'] = prof_df[subjects_list].sum(axis=1)
# prof_df['Percentage'] = (prof_df['Total_Obtained'] / (total_subjects * max_marks_per_subject)) * 100

# # 3. Grade aur GPA ki rules (Conditions) banana
# # Hum percentage ki bunyad par grade aur SGPA nikalenge
# conditions = [
#     (prof_df['Percentage'] > 85),
#     (prof_df['Percentage'] == 85),
#     (prof_df['Percentage'] >= 80) & (prof_df['Percentage'] < 85),
#     (prof_df['Percentage'] < 80)  # Pass ya baqi lower numbers ke liye default
# ]

# grade_choices = ['A+', 'A', 'A-', 'B']
# gpa_choices = [4.0, 4.0, 3.75, 3.0]

# # np.select condition check karta hai aur automatic list match karta hai
# prof_df['Grade'] = np.select(conditions, grade_choices, default='B')
# prof_df['SGPA'] = np.select(conditions, gpa_choices, default=3.0)

# # Round off karna taake format clean rahe
# prof_df['Percentage'] = prof_df['Percentage'].round(2)

# # 4. Final professional excel file save karna
# prof_df.to_excel('professional_result_card.xlsx', index=False)

# print("Professional Grade Sheet and SGPA calculated successfully!")
# print(prof_df[['StudentID', 'StudentName', 'Total_Obtained', 'Percentage', 'Grade', 'SGPA']].head(3))
import pandas as pd

# 1. Match the lengths of subjects and marks (added 80 as the 6th mark)
student_data = {
    "Name": ["Ali"] * 6,  # Repeats the name for all 6 rows
    "Student Id": [70165453] * 6,  # Repeats the ID for all 6 rows
    "Subjects": ["IS", "Web Engineering", "Data Science", "AI", "Cybersecurity", "Data Mining"],
    "Marks": [85, 90, 78, 92, 88, 80]  # Added the 6th mark here
}

# Convert to DataFrame
df = pd.DataFrame(student_data)

# 2. Calculate individual subject percentage (Assuming each subject is out of 100)
df["Percentage"] = (df["Marks"] / 100) * 100

# 3. Define grading logic
def calculate_grade(percentage):
    if percentage >= 85:  # Changed to >= to catch exactly 85 and above
        return "A+"
    elif percentage >= 80:
        return "A-"
    elif percentage >= 75:
        return "B+"
    elif percentage >= 70:
        return "B"
    else:
        return "C"

df["Grade"] = df["Percentage"].apply(calculate_grade)

# 4. Define SGPA logic per subject
def calculate_sgpa(percentage):
    if percentage >= 85:
        return 4.0
    elif percentage >= 80:
        return 3.75
    elif percentage >= 75:
        return 3.5
    elif percentage >= 70:
        return 3.0
    else:
        return 2.0

df["SGPA"] = df["Percentage"].apply(calculate_sgpa)

# Save to Excel
df.to_excel("student_result_card.xlsx", index=False)
print("Student Result Card created successfully!\n")
print(df)

# 5. Optional: Print the overall summary totals for the student
print("\n--- Student Summary ---")
print(f"Total Marks Obtained: {df['Marks'].sum()} / 600")
print(f"Overall GPA: {df['SGPA'].mean():.2f}")
