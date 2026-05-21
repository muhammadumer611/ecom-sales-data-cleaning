# import pandas as pd
# company_employees = {
#      "Employee_ID":[101,202,303,304],
#      "Employee_Name":['John','Smith','Alice','Bob'],
#      "Salary":[50000,60000,55000,45000]

# }
# df = pd.DataFrame(company_employees)
# df.to_csv("company_employees.csv",index =False)
# print("File Saved")
# print(df)


# df = pd.read_csv("company_employees.csv")
# print(df)
import pandas as pd
# company_employees ={
#     "Employee_ID":[101,202,303,304],
#      "Employee_Name":['John','Smith','Alice','Bob'],
#      "Salary":[50000,60000,55000,45000]
# }
# df= pd.DataFrame(company_employees)
# df.to_excel("Company_employees.xlsx",index=False)
# print(df)
df = pd.read_excel("Company_employees.xlsx")
df["Salary"]= df["Salary"]+ 5000
john_data = df[df["Employee_Name"]=="John"]
print(john_data)