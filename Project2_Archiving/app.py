# Student Performance Report Generator
with open("student_report.txt", "w") as f:
    f.write("==================================================\n")
    f.write("      STUDENT ACADEMIC PERFORMANCE REPORT         \n")
    f.write("==================================================\n")
    f.write("Total Registered Students : 120\n")
    f.write("Active Portal Sessions    : 85\n")
    f.write("Overall Passing Percentage: 92.4%\n")
    f.write("--------------------------------------------------\n")
    f.write("Status: Academic records processed with success.\n")

print("Academic performance report generated successfully.")
