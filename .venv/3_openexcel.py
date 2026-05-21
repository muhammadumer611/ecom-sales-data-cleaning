import pandas as pd

# 1. Excel file ka path aur use read karna
file_path = r'D:\Python Pandas\student_result_card.xlsx'  
df_old = pd.read_excel(file_path)

# 2. Naye data ki list aur dictionary
student_subjects = ['subject1', 'subject2', 'subject3', 'subject4', 'subject5']

class_bsse_6th = {
    'Name': ['Ali', 'Sara', 'Ahmed', 'Fatima', 'Hassan'],
    'Roll Number': [1, 2, 3, 4, 5],
    'Subjects': [student_subjects for _ in range(5)],
    'Marks':[[85, 90, 78, 92, 88],
             [80, 85, 82, 88, 90],  
             [78, 82, 80, 85, 87],  
             [90, 92, 88, 95, 91],  
             [82, 88, 85, 90, 89]]
}

# 3. Naye data ko DataFrame mein badalna
df_bsse_6th = pd.DataFrame(class_bsse_6th)

# 4. Calculations karna
df_bsse_6th['Average Marks'] = df_bsse_6th['Marks']
df_bsse_6th['Total Marks'] = df_bsse_6th['Marks'].apply(sum)

# 5. [NEW] Purane aur naye data ko aapas mein jorna
df_updated = pd.concat([df_old, df_bsse_6th], ignore_index=True)

# 6. [NEW] Wapis Excel file mein save karwana
df_updated.to_excel(file_path, index=False)

print("Data kamyabi se append ho kar Excel file mein save ho gaya hai!")
print(df_updated.tail())  # Sirf aakhri naye rows dekhne ke liye
